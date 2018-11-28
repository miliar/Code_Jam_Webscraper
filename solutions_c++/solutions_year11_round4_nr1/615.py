#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <algorithm>

using namespace std;
struct node{int b,e,w;}in[1000];
double ans;
int vset[1000005];
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int tcases,cases=1;
    int x,s,r,t,n,a,b,w;
    scanf("%d",&tcases);
    double lastt,finalans;
    while(tcases--)
    {
        scanf("%d%d%d%d%d",&x,&s,&r,&t,&n);
        ans=0;
        for(int i=1;i<=x;i++) vset[i]=s;
        for(int i=0;i<n;i++)
        {
            scanf("%d%d%d",&a,&b,&w);
            for(int j=a+1;j<=b;j++)
                vset[j]=s+w;
        }
        sort(vset+1,vset+x+1);
        finalans=0;lastt=t;
        for(int i=1;i<=x;i++)
        {
            if(lastt>0)
            {
                if(lastt>1.0/(r+vset[i]-s))
                {
                    finalans+=1.0/(r+vset[i]-s);
                    lastt-=1.0/(r+vset[i]-s);
                }
                else
                {
                    finalans+=lastt;
                    finalans+=(1.0-lastt*(r+vset[i]-s))/vset[i];
                    lastt=0;
                }
            }
            else finalans+=1.0/vset[i];
        }
        printf("Case #%d: %.6f\n",cases++,finalans);
    }
	return 0;
}
