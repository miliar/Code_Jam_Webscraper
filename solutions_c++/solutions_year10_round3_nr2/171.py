#include <sstream>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int bsearchcount(vector<int> &q, int el)
{
    int a = 0, b = q.size() - 1, c = (a + b) / 2;
    int cnt = 0;

    while(q[c] != el && a <= b)
    {
        if(el > q[c])
            a = c + 1;
        else
            b = c - 1;

        c = (a + b) / 2;

        ++cnt;
    }

    return cnt;
}

int main( int argc, char* argv[] )
{
    FILE *fr = fopen("B-large.in", "r");
    FILE *fw = fopen("B-large.out", "w");

    int T;
    fscanf(fr, "%d", &T);
    for(int t = 0; t < T; ++t)
    {
        int l, p, C;
        fscanf(fr, "%d %d %d", &l, &p, &C);
        long long L = l, P = p;

        if(L * C >= P)
            fprintf(fw, "Case #%d: %d\n", t + 1, 0);
        else
        {
            vector<int> q;
            L *= C;
            while(L < P)
            {
                q.push_back(L);
                L *= C;
            }

            int max = 0;

            for(int i = 0; i < q.size(); ++i)
            {
                int cnt = bsearchcount(q, q[i]);
                if(cnt > max)
                    max = cnt;
            }

            fprintf(fw, "Case #%d: %d\n", t + 1, max + 1);
        }
    }

    fclose(fr);
    fclose(fw);

    return 0;
}