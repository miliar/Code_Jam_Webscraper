#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <map>
#include <string>
#include <vector>

using namespace std;



typedef long long ll;//NOTES:int64
typedef unsigned long long ull;//NOTES:uint64

int q [10] = {1,0,2,3,4,5,6,7,8,9};

int main()
{

    int N;

    // input output streams
    //freopen ("input.txt", "r", stdin);
    freopen ("A-small-attempt2.in", "r", stdin);
    freopen ("output.txt", "w", stdout);

    // number of cases
    scanf ("%d", &N);
    if (N < 1)
        printf ("Error: input file not found\n");

    // for each case
    for (int caseId=1; caseId<=N; caseId++)
    {
        char in [100];
        scanf ("%s", &in);
        //printf ("%s\n", &in);
        //printf ("asdf %d\n", strlen(in));

        map<string, int> m;
        for (int i=0; i<strlen(in); i++)
        {
            string dig = in;
            dig = dig.substr(i, 1);
            m[dig] = -1;
        }
        long long base=0;
        long long c[100];
        for (int i=0; i<strlen(in); i++)
        {
            string dig = in;
            dig = dig.substr(i, 1);
            //printf ("%s", dig.c_str());
            //printf ("%d", m[dig]);
            if(m[dig] < 0)
            {
                //printf ("i %d base %d\n", i, base);
                m[dig] = base;
                c[i] = q[base];
                base++;
            //printf ("%d %s\n", c[i], dig.c_str());
            }
            else
            {
                //printf ("i %d base %d\n", i, m[dig]);
                c[i] = q[m[dig]];
            //printf ("%d %s %d\n", c[i], dig.c_str(), m[dig]);
            }
        }
        if (base < 2) base = 2;
        //printf ("%d", base);
        long long count =0;
        long long basepow = 1;
        for (int i=strlen(in)-1; i>=0; i--)
        {
            count += c[i] * basepow;
            //printf ("%lld %lld %lld %lld\n", c[i], count, basepow, base);
            basepow = base * basepow;

            //printf ("asdf%d", c[i]);
        }

        printf ("Case #%d: %lld\n", caseId, count);
    }

    return 0;
}
