#include <stdio.h>
#include <math.h>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <stdlib.h>
#include <time.h>
#include <string>
#include <iostream>
#define oo 1000000000
using namespace std;
int surprisescore[200];
int nonsurprisescore[200];
int dp[200][200];
int findit(int pos, int numsurprise, int totsurprise, int p, int N)
{
    if(pos==N)
        return (numsurprise==totsurprise?0:-oo);
    if(dp[pos][numsurprise]!=-2*oo)
        return dp[pos][numsurprise];
    int retval=max(findit(pos+1,numsurprise,totsurprise,p, N)+ (nonsurprisescore[pos]>=p), 
                   findit(pos+1,numsurprise+1,totsurprise,p,N) + (surprisescore[pos] >=p));
    dp[pos][numsurprise]=retval;
    return retval;
    
}

int main()
{
    int T;
    scanf("%d",&T);
    for(int tcase=1;tcase<=T;tcase++)
    {
        int N,S,p;
        scanf("%d",&N);
        scanf("%d",&S);
        scanf("%d",&p);
        for(int i=0;i<=N;i++)
            for(int j=0;j<=N;j++)
                dp[i][j]=-2*oo;
        for(int i=0;i<N;i++)
        {
            int totscore;
            scanf("%d",&totscore);
            surprisescore[i]=-1;
            nonsurprisescore[i]=-1;
            // if surprising
            for(int a=0;a<=min(10,totscore);a++)
                for(int b=a;b<=min(10,totscore-a);b++)
                {
                    int c=totscore-a-b;
                    if(c<b || c>10 || c-a>2)
                        continue;
                    if(c-a==2)
                        surprisescore[i]=max(surprisescore[i], c);
                    else
                        nonsurprisescore[i]=max(nonsurprisescore[i], c);
                    
                }
            
            
        }
        
        printf("Case #%d: %d\n",tcase, findit(0,0,S,p,N));
        
    }
}