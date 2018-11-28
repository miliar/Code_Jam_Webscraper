#include<iostream>
using namespace std;
const int Max=1000000;
char ch[200][200];
int hi[200][200];
bool b[200][200];
int n,total,m;
bool cheaks(int x,int y,int xx,int yy){
     if (hi[x][y]>=hi[xx][yy])return false; 
     int a1=Max,a2=Max,a3=Max,a4=Max;
     int b1=1,b2=4,b3=2,b4=3,bb;
     if (xx-1==x&&yy==y) bb=1;else
     if (xx+1==x&&yy==y) bb=4;else
     if (xx==x&&yy-1==y) bb=2;else
     if (xx==x&&yy+1==y) bb=3;
     if (xx-1>0) a1=hi[xx-1][yy];
     if (xx+1<=n) a2=hi[xx+1][yy];
     if (yy-1>0) a3=hi[xx][yy-1];
     if (yy+1<=m) a4=hi[xx][yy+1];
     if ((hi[x][y]<a1||(hi[x][y]==a1&&b1>=bb))&&
         (hi[x][y]<a2||(hi[x][y]==a2&&b2>=bb))&&
         (hi[x][y]<a3||(hi[x][y]==a3&&b3>=bb))&&
         (hi[x][y]<a4||(hi[x][y]==a4&&b4>=bb))) return true;
     return false;
}
bool cheak(int x,int y,int xx,int yy){
     if (cheaks(x,y,xx,yy)) return true;
     if (cheaks(xx,yy,x,y)) return true;
     return false;
}
void foodfill(char c,int x,int y){
     if (x==0||x==n+1) return;
     if (y==0||y==m+1) return;
     ch[x][y]=c;
     b[x][y]=true;
     if (!b[x-1][y]&& cheak(x,y,x-1,y)) foodfill(c,x-1,y);
     if (!b[x+1][y]&& cheak(x,y,x+1,y)) foodfill(c,x+1,y);
     if (!b[x][y-1]&& cheak(x,y,x,y-1)) foodfill(c,x,y-1);
     if (!b[x][y+1]&& cheak(x,y,x,y+1)) foodfill(c,x,y+1);
}
int main(){
    freopen("1.in","r",stdin);
    freopen("1.out","w",stdout);
    cin>>total;
    for (int i=0;i<total;i++){
        cin>>n>>m;
        for (int j=1;j<=n;j++)
        for (int k=1;k<=m;k++)
        cin>>hi[j][k];
        for (int j=0;j<=m+1;j++)
        hi[0][j]=Max;
        for (int j=0;j<=m+1;j++)
        hi[n+1][j]=Max;
        for (int j=0;j<=n+1;j++)
        hi[j][0]=Max;
        for (int j=0;j<=n+1;j++)
        hi[j][m+1]=Max;
        memset(b,0,sizeof(b));
        char chs='a';
        
        for (int j=1;j<=n;j++)
        for (int k=1;k<=m;k++)
        if (!b[j][k]){
        foodfill(chs,j,k);chs++;}
        cout<<"Case #"<<i+1<<": "<<endl;
        for (int j=1;j<=n;j++){
            for (int k=1;k<=m;k++)
            if (k!=m)
            cout<<ch[j][k]<<" ";else
            cout<<ch[j][k];
            cout<<endl;
        }
    }
    return 0;
}
