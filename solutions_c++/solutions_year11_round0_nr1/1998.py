#include<iostream>
#include<cstdio>
#include<cmath>
using namespace std;

int myabs(int a)
{
    if(a>=0) return a;
    return -a;
}

int main()
{
    int t,p;
    int d,dt;
    char s[10];
    freopen("A2.in","r",stdin);
    freopen("a2.out","w",stdout);
    scanf("%d",&t);
    int cs=0;
    while(t--)
    {
        scanf("%d",&p);
        int p1=1,p2=1;
        int ans=0;
        int t1=0,t2=0;
        while(p--)
        {
            scanf("%s%d",s,&d);
            if(s[0]=='O')
            {
                dt=myabs(d-p1)+1;
                t1+=dt;
                p1=d;
                ans=max(ans+1,t1);
                if(t1<ans) t1=ans;
            }
            else
            {
                dt=myabs(d-p2)+1;
                t2+=dt;
                p2=d;
                ans=max(ans+1,t2);
                if(t2<ans) t2=ans;
            }
      //      printf("%d\n",ans);
        }
        printf("Case #%d: %d\n",++cs,ans);
    }
    return 0;
}

