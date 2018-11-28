
#include <stdio.h>
#include <string.h>
#include <map>
#include <list>
#include <set>
#include <string>
#include <vector>
#include <math.h>

#define MAX_Q 5
int P, Q;
int cells[MAX_Q + 2];
int freed[MAX_Q + 2];
int min_cost;

int GetCost(int p)
{
    int left, right;

    for (int i = p - 1; i >= 0; i --)
    {
        if (freed[i])
        {
            left = i;
            break;
        }
    }

    for (int i = p + 1; i <= Q + 1; i ++)
    {
        if (freed[i])
        {
            right = i;
            break;
        }
    }

    int cost = cells[right] - cells[left] - 2;
    return cost;
}

void ReleasePrisoner(int seq, int cost)
{
    if (seq == Q)
    {
        if (min_cost > cost)
        {
            min_cost = cost;
        }
    }

    for (int i = 1; i <= Q; i ++)
    {
        if (freed[i])
        {
            continue;
        }

        freed[i] = 1;
        ReleasePrisoner(seq + 1, cost + GetCost(i));
        freed[i] = 0;
    }
}

void GCJ_2009Round1C_C(const char*input, const char*output)
{
    FILE* fin = freopen(input, "rb", stdin);
    FILE* fout = freopen(output, "wb", stdout);

    int N, ncase = 0;
    scanf("%d", &N);
    while (ncase ++ < N)
    {
        //run one test case
        scanf("%d%d", &P, &Q);
        for (int i = 1; i <= Q; i ++)
        {
            scanf("%d", &cells[i]);
            freed[i] = 0;
        }
        cells[0] = 0;
        freed[0] = 1;
        cells[Q+1] = P + 1;
        freed[Q+1] = 1;

        min_cost = 0x7fffffff;

        ReleasePrisoner(0, 0);

        printf("Case #%d: %d\n", ncase, min_cost);
    }

    fclose(fin);
    fclose(fout);
}

int main(int argc, char** argv)
{
    char*in_file = "gcj.in";
    char*out_file = "gcj.out";

    GCJ_2009Round1C_C(in_file, out_file);


    return 0;
}