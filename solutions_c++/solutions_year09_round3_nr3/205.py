#include<iostream>
using namespace std;
int a[105],f[10005][10005];
int p,q;
bool b[10005];
int work(int x,int y){
     if (f[x][y]!=-1) return f[x][y];
     if (x>y) return 0;
     for (int i=0;i<p;i++){
         if (a[i]>=x&&a[i]<=y){
               int an=work(x,a[i]-1)+work(a[i]+1,y)+(y-x);
               if (an<f[x][y]||f[x][y]==-1) f[x][y]=an;
         }else if (a[i]>y) break;
     }
     if (f[x][y]==-1) f[x][y]=0;
     return f[x][y];
}
int main(){
    freopen("1.in","r",stdin);
    freopen("1.out","w",stdout);
    int t;
    cin>>t;
    for (int tt=1;tt<=t;tt++){
        memset(f,-1,sizeof(f));
        memset(a,0,sizeof(a));
        cin>>p>>q;
        for (int i=0;i<q;i++){
            cin>>a[i];
        }
        int ans=work(1,p);
        cout<<"Case #"<<tt<<": "<<ans<<endl;
    }
    return 0;
}
