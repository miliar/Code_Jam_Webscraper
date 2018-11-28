#include<cstdio>
#include<cstring>
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int T;
    scanf("%d",&T);
    for(int tt=1;tt<=T;tt++)
    {
        int n,s,p;
        int t[128];
        scanf("%d%d%d",&n,&s,&p);
        for(int i=0;i<n;i++)
        {
              scanf("%d",&t[i]);
        }
        int ans=0;
        for(int i=0;i<n;i++)
        {
             int x = t[i]/3;
             int y = t[i]%3;
             int maxx = y?x+1:x;
             int minx = x;
             if(maxx>=p) ans++;
             else {
                  if(s)
                  {
                       s --;
                       if(y == 0 || y ==1) {
                            maxx = x+1;
                            minx = x-1;
                       }
                       else {
                            maxx = x+2;
                            minx = x;
                       }
                       if(maxx>=p && maxx<=10 && minx>=0) ans ++;
                       else {
                            s ++;
                       }
                  }
             }
        }
        printf("Case #%d: %d\n",tt,ans);
    }
}
