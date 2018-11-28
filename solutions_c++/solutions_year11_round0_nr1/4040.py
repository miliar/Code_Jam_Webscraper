#include <stdio.h>
#include <stdlib.h>

#include <iostream>
#include <map>
#include <vector>

using namespace std;
struct Action
{
    char c;
    int b;

    Action(char ch, int bt)
        :c(ch), b(bt)
    {}
    
};
typedef vector< Action > Actions;

int findNext(Actions& acts, int l, char c )
{
    int res=-1;
    for(; l<acts.size(); ++l)
    {
        if ( acts[l].c != c ) return l;
    }    

    return res;
}

int main()
{
    int T;
    scanf("%d", &T);
//    printf("T: %d\n", T);
    for(int k=0;k<T; ++k)
    {
        int N;
        scanf("%d", &N);
//        printf(" N: %d\n", N);
        Actions actions;

        // read the input
        for(int j=0;j<N;++j)
        {
            char C; int B;
            scanf(" %c %d", &C, &B);
//            printf("  A: %c %d\n", (char)C, B);
            actions.push_back( Action((char)C, B) );
        }

        // start simulation
        int pos[2] = {1,1};
        int totaltime=0;
        for(int l=0; l<actions.size(); ++l)
        {
            int interval=0;
            Action& act = actions[l];
            bool orang = (act.c == 'O');

            interval = abs( act.b - pos[orang] ) + 1;
            pos[orang] = act.b;
            totaltime += interval;

            int oth = findNext(actions, l+1, act.c);
            if (oth == -1) 
            {
            // printf("%d: B%d O%d interval%d\n", l+1, 
            //        pos[!orang], pos[orang], interval);
                continue;
            }

            int delta = actions[oth].b - pos[!orang];
            int dist = abs( delta );
            if (dist <= interval) 
                pos[!orang] = actions[oth].b;
            else
            { 
                if ( delta < 0 )                     
                    pos[!orang] -= interval;                    
                else
                    pos[!orang] += interval;
            }

            // printf("%d: B%d O%d interval%d\n", l+1, 
            //        pos[!orang], pos[orang], interval);

        }
        printf("Case #%d: %d\n", k+1, totaltime);
    }

    return 0;
}
