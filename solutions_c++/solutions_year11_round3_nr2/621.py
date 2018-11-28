/*

*/
#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <map>
using namespace std;
int Case,l,t,n,c,C[1100],d[1100],ans;
bool h[1100];
int dcmp(double x)
{
    if (fabs(x)<1e-6) return 0;
    return x>0?1:-1;
}
double moni()
{
    double ret=0;
    for (int i=0;i<n;i++) {
        if (!h[i]) ret+=2*d[i];
        else {
            if (dcmp(ret-t)>=0) ret+=d[i];
            else {
                if (dcmp(0.5*(t-ret)-d[i])>=0) {
                    ret+=2*d[i];
                }
                else ret+=(t-ret)+(d[i]-0.5*(t-ret));
            }
        }
    }
    return ret;
}
void dfs(int x,int s)
{
    if (x==n) {
        if (s!=l) return;
        ans=min(ans,(int)moni());
        return;
    }
    if (s<l) {
        h[x]=true;
        dfs(x+1,s+1);
    }
    h[x]=false;
    dfs(x+1,s);
}
void display()
{
    cin>>Case;
    for (int ca=1;ca<=Case;ca++) {
        printf("Case #%d: ",ca);
        scanf("%d%d%d%d",&l,&t,&n,&c);
        for (int i=0;i<c;i++)
            scanf("%d",&C[i]);
        for (int i=0,k=0;i<n;i++,k=(k+1)%c)
            d[i]=C[k];
        ans=0x7fffffff;
        dfs(0,0);
        printf("%d\n",ans);
    }
}
int main()
{
    //freopen("B-small-attempt1.in","r",stdin);
    //freopen("B-small-attempt1.out","w",stdout);
    display();
    return 0;
}

