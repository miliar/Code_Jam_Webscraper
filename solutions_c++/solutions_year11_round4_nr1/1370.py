/*
TASK: <Task>
LANG: C++
*/
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<algorithm>
#define X first
#define Y second
using namespace std;
int N,M,T;
pair<int,int> p[100005];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A.txt","w",stdout);
    int i,j,k;
    scanf("%d",&T);
    int tt=0,x,y,z;
    int X,S,R,t,idx;
    double a,b,c,can_run,ans;
    while(T--)
    {
        tt++;
        ans=0;
        scanf("%d%d%d%d%d",&M,&S,&R,&t,&N);
        for(i=0;i<N;i++)
        {
            scanf("%d%d%d",&x,&y,&p[i].X);
            p[i].Y=y-x;
            M-=p[i].Y;
        }
        can_run=t;
//        idx=0;
        p[N].X=0;
        p[N].Y=M;
        sort(&p[0],&p[N+1]);
        for(i=0;i<=N;i++)
        {
//            printf("%d\n",i);
//            system("pause");
            k=p[i].Y;
            a=(double)k/(R+p[i].X);
            if(a<=can_run)
            {
                ans+=a;
                can_run-=a;
            }
            else
            {
                if(can_run<=0)
                    ans+=((double)k/(S+p[i].X));
                else
                {
                    b=can_run*(R+p[i].X);
                    ans+=can_run;
                    c=k-b;
                    c=c/(S+p[i].X);
                    ans+=c;
                    can_run=0;
                }
            }
//            printf("%d %d %d %lf [%lf]\n",p[i].X,p[i].Y.X,p[i].Y.Y,can_run,ans);
        }
        printf("Case #%d: %lf\n",tt,ans);
    }
}
