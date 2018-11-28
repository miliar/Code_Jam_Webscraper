// Problem A: Saving the Universe
// Problem's source: Google Code Jam, Qualification Round
// Program by Plamen Petrov (C) 2008
// http://digitalphysics.org/~ppetrov

#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;

const int MAXS=128, MAXQ=1024, MAXLEN=1024;
char s[MAXS][MAXLEN], q[MAXQ][MAXLEN];
int c[MAXS]; //counters of the required switches per search engine

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    
    int i, k, l, test, N, S, Q, min;
    
    //input
    scanf("%d", &N);
    for(test=1; test<=N; test++)
    {
        scanf("%d", &S);
        gets(s[0]); //clear last input
        for(i=0; i<S; i++) gets(s[i]);
        
        scanf("%d", &Q);
        gets(q[0]); //clear last input
        for(i=0; i<Q; i++) gets(q[i]);
        
        //clear counters c
        for(i=0; i<S; i++) c[i]=0;
        
        for(i=Q-1; i>=0; i--)
        {
            //seek for search engine number
            for(k=0; k<S; k++)
            {
                if(strcmp(s[k],q[i])==0) break;
            }
            
            //seek for min among counters not equal to k
            min=MAXQ;
            for(l=0; l<S; l++)
            {
                if(l==k) continue;
                if(min>c[l]) min=c[l];
            }
            c[k] = ++min;
        }
        
        min=*min_element(c, c+S);
        printf("Case #%d: %d\n", test, min);
    }

    return 0;
}
