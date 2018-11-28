#include <cstdio>
#include <cmath>
#include <string>
#include <iostream>

using namespace std;

int main()
{
    int T;
    scanf("%d", &T);
    for (int test=1; test<=T; ++test) {
        int N;
        scanf("%d", &N);
        int Opos = 1;
        int Otime = 0;

        int Bpos = 1;
        int Btime = 0;

        int totaltime = 0;
        for (int i=0; i<N; ++i) {
            char R[5];
            int P;
            scanf("%s%d",R,&P);
            if (R[0] == 'O') {
                int requiredtimetomove = abs(P-Opos);
                
                int availabletime = totaltime - Otime;
                requiredtimetomove -= availabletime;
                if (requiredtimetomove < 0)
                    requiredtimetomove = 0;

                int requiredtimetopress = requiredtimetomove + 1;
                totaltime += requiredtimetopress;
                Otime = totaltime;
                Opos = P;
            }
            else {
                int requiredtimetomove = abs(P-Bpos);
                
                int availabletime = totaltime - Btime;
                requiredtimetomove -= availabletime;
                if (requiredtimetomove < 0)
                    requiredtimetomove = 0;

                int requiredtimetopress = requiredtimetomove + 1;
                totaltime += requiredtimetopress;
                Btime = totaltime;
                Bpos = P;
            }
        }
        printf("Case #%d: %d\n",test, totaltime);
    }
    return 0;
}