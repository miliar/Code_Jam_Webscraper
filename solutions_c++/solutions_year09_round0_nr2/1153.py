#include<iostream>
using namespace std;
int xx[5]={0,-1,0,0,1},yy[5]={0,0,-1,1,0};
char color;
        int m,n;
char f[101][101];
int a[101][101];
void deal(int,int);
int main(){
    int T;
    cin >> T;
    for (int i=1;i<=T;++i){
        memset(f,0,sizeof(f));

        cin >> m>>n;
        for (int j=1;j<=m;++j)
            for (int k=1;k<=n;++k) cin >> a[j][k];
        color='a';
        for (int j=1;j<=m;++j)
            for (int k=1;k<=n;++k)
                if (f[j][k]==0) deal(j,k);        
        cout << "Case #"<<i<<":"<<endl;
        for (int j=1;j<=m;++j){
            for (int k=1;k<n;++k) cout << f[j][k]<<" ";
            cout << f[j][n]<<endl;
            }
        }

    }
void deal(int x,int y){
     int dir=0;
     for (int i=1;i<=4;++i){
         int tx=x+xx[i],ty=y+yy[i];
         if (tx>0&&tx<=m&&ty>0&&ty<=n&&a[tx][ty]<a[x+xx[dir]][y+yy[dir]]) dir=i;
         }
     if (dir==0) f[x][y]=color++;
     else{
          if (f[x+xx[dir]][y+yy[dir]]==0) deal(x+xx[dir],y+yy[dir]);
          f[x][y]=f[x+xx[dir]][y+yy[dir]];
          }
     }
