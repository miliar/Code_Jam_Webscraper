#include<iostream>
#include<cstdio>
#include<cmath>
using namespace std;
const int N = 505;
int a[N][N];
int n,m,d,ans,T;
bool cmp(double a,double b){
    if (fabs(a-b)<1e-6)
    return true; else return false;
}
void check(int x,int y,int k){
  //  cout<<x<<" "<<y<<" "<<k<<endl;
    int sx = 0,sy=0,sum=0;
    for (int i=x;i<=x+k-1;i++) for(int j=y;j<=y+k-1;j++){
        sx = sx + i*a[i][j];
        sy = sy + j*a[i][j];
        sum+=a[i][j];
    }
    sx = sx - x*(a[x][y]+a[x][y+k-1]) - (x+k-1)*(a[x+k-1][y]+a[x+k-1][y+k-1]);
    sy = sy - y*(a[x][y]+a[x+k-1][y]) - (y+k-1)*(a[x+k-1][y+k-1]+a[x][y+k-1]);
    sum=sum-a[x][y]-a[x][y+k-1]-a[x+k-1][y]-a[x+k-1][y+k-1];
    double xx = (double)sx/(sum);
    double yy = (double)sy/(sum);
   // cout<<sx<<" "<<sy<<endl;
   // cout<<xx<<" "<<yy<<endl;

    if (cmp(xx,(x+x+k-1)/2.0) && cmp(yy,(y+y+k-1)/2.0)) {
        ans = max(ans,k); }
    //cout<<x<<" "<<y<<" "<<k<<endl;
}
int main (){
    freopen("B-small-attempt1.in","r",stdin);
    freopen("Bsmall.out","w",stdout);
    cin>>T; int tt=0;
    while (T--){
        scanf("%d%d%d\n",&n,&m,&d);
        for (int i=1;i<=n;i++) {
            for (int j=1;j<=m;j++) {
                char ch = getchar();
                a[i][j] = ch-'0'+d;
                //cout<<a[i][j];
            }
          //  cout<<endl;
            getchar();
        }
        ans = -1;
      //  cout<<1<<endl;
        for (int i=1;i<=n;i++) for (int j=1;j<=m;j++)
        for (int k=3;k<=100;k++) if (i+k-1<=n && j+k-1<=m){
            check(i,j,k);
        }
        printf("Case #%d: ",++tt);
        if (ans>0) cout<<ans<<endl;else cout<<"IMPOSSIBLE"<<endl;
    }
}
