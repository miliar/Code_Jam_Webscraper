#include<stdio.h>
#include<queue>

using namespace std;


int g[30];

queue<int>Q;

void ini()
{
    while(!Q.empty()) Q.pop();
}
int main()
{
    int tst,x;
    int r,k,n,i,e,j,l;
    int cn;
    freopen("C-small-attempt0.in","rt",stdin);
    freopen("C.txt","w",stdout);

    scanf("%d",&tst);
    for(x=1;x<=tst;x++)
    {
        scanf("%d%d%d",&r,&k,&n);
        ini();
        for(i=1;i<=n;i++)
        {
            scanf("%d",&g[i]);
            Q.push(g[i]);
        }

        e=0;

        for(i=1;i<=r;i++)
        {
            j=0;
            cn=0;
            while(j<=k)
            {
                l=Q.front();
                j+=l;
                if(j<=k) Q.pop(),Q.push(l);
                else
                {
                    j-=l;
                    e+=j;
                    break;
                }
                cn++;
                if(cn==n) {
                    e+=j;
                    break;
                }
            }
        }

        printf("Case #%d: %d\n",x,e);

    }

    return 0;
}
