#include <iostream>
#include <cmath>
using namespace std;
int main()
{
   // printf("%d\n",1<<1);
   freopen("alarge.in","r",stdin);
    freopen("large.txt","w",stdout);
    int T;
    scanf("%d",&T);
    for(int t=1;t<=T;t++)
    {
        int n,x=1,y=1;
        scanf("%d",&n);
        char c;
        int pos;
        int tx[128],ty[128];
        int nx,ny;
        nx=0;
        ny=0;
        int col[128];
        int res=0;
        for(int i=0;i<n;i++)
        {
            scanf(" %c %d",&c,&pos);
            if(c=='O')
            {
                tx[nx++]=pos;
                col[i]=1;
            }
            else
            {
                ty[ny++]=pos;
                col[i]=0;
            }
        }
        int nowx=0,nowy=0;
        int disx,disy;
        for(int i=0;i<n;i++)
        {
            disx=abs(x-tx[nowx]);
            disy=abs(y-ty[nowy]);
            if(col[i]==1)
            {
                res+=(disx+1);
                x=tx[nowx];
                nowx++;
                if(disy<=disx+1)
                {
                    y=ty[nowy];
                }
                else
                {
                    if(y<ty[nowy])
                    {
                        y+=(disx+1);
                    }
                    else
                    {
                        y-=(disx+1);
                    }
                }
            }
            else
            {
                res+=(disy+1);
                y=ty[nowy];
                nowy++;
                if(disx<=disy+1)
                {
                    x=tx[nowx];
                }
                else
                {
                    if(x<tx[nowx])
                    {
                        x+=(disy+1);
                    }
                    else
                    {
                        x-=(disy+1);
                    }
                }
            }
        }
        printf("Case #%d: %d\n",t,res);
    }
	return 0;
}
