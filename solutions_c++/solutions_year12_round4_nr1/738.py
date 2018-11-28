#include<cstdio>

using namespace std;

int tstcss,lp,n,i,fr,rr,dis;
int d[20000],l[20000],q[20000],f[20000];
const int inf=2147482647;
bool fd;

int main()
{
    scanf("%d",&tstcss);
    for (lp=0;lp<tstcss;lp++)
    {
        scanf("%d",&n);
        for (i=0;i<n;i++)
        {
            scanf("%d %d",&d[i],&l[i]);
        }
        scanf("%d",&dis);
        d[n]=dis;l[n]=inf;
        f[0]=d[0];
        fr=0;rr=0;q[rr]=0;
        fd=true;
        for (i=1;i<=n;i++)
        {
            while (f[q[fr]]<d[i]-d[q[fr]])
            {
                fr++;
                if (fr>rr)
                {
                    fd=false;
                    break;
                }
            }
            if (fd==false) break;
            f[i]=d[i]-d[q[fr]];
            if (f[i]>l[i]) f[i]=l[i];
            if (d[q[rr]]+f[q[rr]]<d[i]+f[i])
            {
                rr++;
                q[rr]=i;
            }
        }
        printf("Case #%d: ",lp+1);
        if (fd==true) printf("YES\n");else printf("NO\n");
    }
    return 0;
}
            
    
