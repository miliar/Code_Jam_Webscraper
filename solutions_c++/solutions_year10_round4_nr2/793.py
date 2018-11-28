#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <iostream>
#include <algorithm>
#include <queue>
#include <set>
#include <string>
#include <map>
#include <vector>

using namespace std;


class Team
{
      public : long index;
               long miss;
};


bool cmp(Team a, Team b)
{
     return a.miss<b.miss || (a.miss==b.miss && a.index<b.index);
}

Team m[2000000];
long in, sum, x, y, k, fix[2000][2000], c[2000][2000],test, t, n,N, l, P, O, cnt, path[2000];

int main()
{
    freopen("b-small.in","r",stdin);
    freopen("b-small.out","w",stdout);
    
    
    scanf("%d",&t);
    for (test = 1; test <= t; test ++ )
    {
        printf("Case #%d: ", test);
        scanf("%d",&n);
        N = 1<<n;
        for (l=0; l<N; l++)
        {
            scanf("%d",&m[l].miss); 
            m[l].index = l;
        }
        
        P = N;
        for (l=0; l<n; l++)
        {
            P/=2;
            for (k=0; k<P; k++)
             scanf("%d",&c[l][k]);
        }
        memset(fix,0,sizeof(fix));
        
        sort(m,m+N,cmp);
        sum = 0;
        for (l=0; l<N; l++)
        {
            in = m[l].index; in/=2;
            cnt = 0; 
            for (k=0; k<n; k++) { path[cnt++] = in;  in/=2; }
            
            reverse(path,path+cnt);
            O = m[l].miss;
            x = n-1; y = 0;
            
            for (k=1; k<=cnt; k++)
            {
                if (fix[x][y]==1 || fix[x][y]==-1) {   x--; y = path[k]; continue; }
                if (O>0 && fix[x][y]==0) { fix[x][y] = -1; O--; } else { fix[x][y] = 1; sum += c[x][y]; }
                x--; y = path[k];
            }
            
             
            in = m[l].index;
             
        }
        printf("%d\n",sum);
    }
    return 0;
}
