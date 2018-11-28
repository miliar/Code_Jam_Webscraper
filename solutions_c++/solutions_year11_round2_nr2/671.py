#include <iostream>
#include<cstdio>

using namespace std;
const int maxn=1100000;

int left[maxn],right[maxn];
struct In
{
    int x,num;
}s[maxn];
int main()
{
    int i,j,k,n,m,x,y,t,l,z,p,ml;
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&t);
    for(l=1;l<=t;l++)
    {
        scanf("%d%d",&n,&m);
        for(i=1;i<=n;i++)
        {
            scanf("%d%d",&s[i].x,&s[i].num);
        }
        p=s[1].x;
        s[1].num--;
        ml=0;
        for(i=1;i<=n;i++)
        {
            while(s[i].num>0)
            {
                p+=m;
                if(s[i].x<p)
                {
                    if(ml<p-s[i].x)ml=p-s[i].x;
                }
                else
                {
                    p=s[i].x;
                }
                s[i].num--;
            }
        }
        printf("Case #%d: %.10lf\n",l,ml*1.0/2.0);
    }
    return 0;
}
