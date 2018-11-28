#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <cmath>

using namespace std;

const int MAXM=110;

int N,S,P;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int t,cas;
    scanf("%d",&t);
    for(cas=1;cas<=t;cas++)
    {
        scanf("%d%d%d",&N,&S,&P);
        int i,j,a,b,c,res=0;
        for(i=0;i<N;i++)
        {
            scanf("%d",&j);
            a=b=c=j/3;
            if(j%3>=1) c++;
            if(j%3==2) b++;
            if(c>=P) res++;
            else
            {
                if(j%3==1) continue;
                if(S && b && c+1>=P)
                {
                    S--;
                    res++;
                }
            }
        }
        printf("Case #%d: %d\n",cas,res);
    }
    return 0;
}
