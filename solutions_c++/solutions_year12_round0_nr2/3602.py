#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

typedef struct gs_t
{
    int N;
    int S;
    int p;
    int t[101];
    int ans;
} gs_t;

int main()
{
    ifstream input;
    string line;
    int n;
    int min;

    struct gs_t gs;

    input.open("B-large.in");

    getline(input, line);

    n = atoi(line.c_str());

    for(int i=0; i<n; i++)
    {
        gs.ans = 0;
        input >> gs.N; // number of dancers
        input >> gs.S; // surprising (+/- 2)
        input >> gs.p; // min score

        for(int k=0; k<gs.N; k++)
        {
            input >> gs.t[k];
        }

#if(0)
4
3 1 5 15 13 11
3 0 8 23 22 21
2 1 1 8 0
6 2 8 29 20 8 18 18 21
#endif
        int found = 0;
        for(int j=0; j<gs.N; j++)
        {
            int tmp = gs.t[j];

            if(( ((tmp+2)/3)+0 ) >=gs.p)
            {
                gs.ans++;
                found++;
            }
            else if(gs.S && tmp>=2)
            {
                if((((tmp+4)/3)) >=gs.p)
                {
                    gs.ans++;
                    gs.S--;
                }
            }

        }
#if(0)
        cout << gs.ans << " " << found << " " << gs.ans-found << endl;
#endif
        cout << "Case #" << i+1 << ": " << gs.ans << endl;
    }
    return 0;
}
