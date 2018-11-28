#include <cstdio>
#include <cstdlib>

using namespace std;

int TC = 1, T, N, clk=0, B_pos, O_pos, P, B_rest, O_rest, gap, time;
char C;

int main ()
{
    for (scanf ("%d", &T); TC <= T; TC++)
    {
        N=0; B_pos=1; O_pos=1; B_rest=0; O_rest=0, time=0;
        scanf ("%d", &N);
        while(N--)
        {
            scanf(" %c %d", &C, &P);
            if(C=='O')
            {
                gap=abs(P-O_pos);
                O_pos=P;
                gap-=O_rest;
                if(gap<1)
                    gap=0;
                O_rest=0;
                B_rest+=(gap+1);
                time+=(gap+1);
            }
            if(C=='B')
            {
                gap=abs(P-B_pos);
                B_pos=P;
                gap-=B_rest;
                if(gap<1)
                    gap=0;
                B_rest=0;
                O_rest+=(gap+1);
                time+=(gap+1);
            }
        }
        printf ("Case #%d: %d\n", TC, time);
    }

    return 0;
}
