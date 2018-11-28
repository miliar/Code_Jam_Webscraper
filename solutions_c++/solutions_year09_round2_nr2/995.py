
#include <stdio.h>
#include <string.h>
#include <map>
#include <list>
#include <set>
#include <string>
#include <vector>

#define MAX_N 30

bool isDecending(char data[])
{
    char*p = data;

    while (*p != '\0')
    {
        if (*p < *(p + 1))
        {
            return false;
        }

        p ++;
    }

    return true;
}

int CharCmp(const void*a, const void*b)
{
    return *(char*)a - *(char*)b;
}

void GCJ_2009Round1B_B(const char*input, const char*output)
{
    FILE* fin = freopen(input, "rb", stdin);
    FILE* fout = freopen(output, "wb", stdout);

    int T, ncase = 0;
    scanf("%d", &T);
    while (ncase ++ < T)
    {
        char data[MAX_N+1] = {0};
        //run one test case
        scanf("%s", data);

        if (isDecending(data))
        {
            int len = strlen(data);
            data[len] = '0';
            data[len + 1] = '\0';
            strrev(data);

            for (int i = 0; i <= len; i ++)
            {
                if (data[i] > '0')
                {
                    data[0] = data[i];
                    data[i] = '0';
                    break;
                }
            }
        }
        else
        {
            int len = strlen(data);
            int i, j;
            int cur_max = len;
          

            for (i = len - 1; i > 0; i --)
            {
                if (data[i] >= data[cur_max])
                {
                    cur_max = i;
                    continue;
                }
                break;
            }

            for (j = len - 1; j > i; j --)
            {
                if (data[j] > data[i])
                {
                    break;
                }
            }

            char tmp = data[i];
            data[i] = data[j];
            data[j] = tmp;

            //qsort data[i+1, len-1];
            qsort(&data[i+1], len - i -1, sizeof(char), CharCmp);
        }

        printf("Case #%d: %s\n", ncase, data);
    }

    fclose(fin);
    fclose(fout);
}

int main(int argc, char** argv)
{
    char*in_file = "gcj.in";
    char*out_file = "gcj.out";

    GCJ_2009Round1B_B(in_file, out_file);


    return 0;
}