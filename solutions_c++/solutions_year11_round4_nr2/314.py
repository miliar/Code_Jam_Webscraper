#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <cmath>
#include <cstring>

using namespace std;

#define ll long long

const double eps=1E-9;

int T;
int r,c,d;
ll w[510][510];
ll x[510][510];
ll y[510][510];
ll px[510][510];
ll py[510][510];
ll p[510][510];
int ans;
ll qx,qy,qm;
char qqq;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&T);
    for (int k=1;k<=T;k++){
        scanf("%d%d%d ",&r,&c,&d);
        memset(px,0,sizeof(px));
        memset(py,0,sizeof(py));
        memset(p,0,sizeof(p));
        for (int i=1;i<=r;i++)
            for (int j=1;j<=c;j++){
                scanf("%c ",&qqq);
                w[i][j]=d+(qqq-'0');
                x[i][j]=i*w[i][j];
                y[i][j]=j*w[i][j];
                px[i][j]=px[i-1][j]+px[i][j-1]-px[i-1][j-1]+x[i][j];
                py[i][j]=py[i-1][j]+py[i][j-1]-py[i-1][j-1]+y[i][j];
                p[i][j]=p[i-1][j]+p[i][j-1]-p[i-1][j-1]+w[i][j];
            }
        ans=-1;
        for (int l=min(r,c);l>=3;l--){
            if (ans!=-1) break;
            for (int i=1;i<=r-l+1;i++)
                for (int j=1;j<=c-l+1;j++){
                    qx=px[i+l-1][j+l-1]-px[i-1][j+l-1]-px[i+l-1][j-1]+px[i-1][j-1];
                    qx-=x[i][j]+x[i+l-1][j]+x[i][j+l-1]+x[i+l-1][j+l-1];
                    qy=py[i+l-1][j+l-1]-py[i-1][j+l-1]-py[i+l-1][j-1]+py[i-1][j-1];
                    qy-=y[i][j]+y[i+l-1][j]+y[i][j+l-1]+y[i+l-1][j+l-1];
                    qm=p[i+l-1][j+l-1]-p[i-1][j+l-1]-p[i+l-1][j-1]+p[i-1][j-1];
                    qm-=w[i][j]+w[i+l-1][j]+w[i][j+l-1]+w[i+l-1][j+l-1];
                    if (abs(qx*1.0/qm-(i+(l-1)*1.0/2))>eps) continue;
                    if (abs(qy*1.0/qm-(j+(l-1)*1.0/2))>eps) continue;
                    ans=l;
                    break;
                }
        }
        if (ans==-1) printf("Case #%d: IMPOSSIBLE\n",k);
        else printf("Case #%d: %d\n",k,ans);
    }
    return 0;
}
