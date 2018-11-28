#include<iostream> 
using namespace std;
const int maxN=100+5,dir[4][2]={-1,0, 0,-1, 0,1, 1,0};
int h[maxN][maxN],opt[maxN*maxN];
char colour[maxN*maxN];
int n,m,total,zz,uu;

void init(){
    scanf("%d%d",&n,&m);
    for (int i=1;i<=n;i++)
    for (int j=1;j<=m;j++) scanf("%d",&h[i][j]);
}
int get(int x,int y,int k){
    x=x+dir[k][0];
    y=y+dir[k][1];
    if ((1<=x)&&(x<=n)&&(1<=y)&&(y<=m)) return h[x][y];
    else return 10000000;
}
char hzz(int x){
     if (colour[x]>='a') return colour[x];
     if (opt[x]==x) {colour[x]='a'+total;total++;return colour[x];}
     colour[x]=hzz(opt[x]);
     return colour[x];
}
void work(){
    for (int i=0;i<=n*m;i++) colour[i]='a'-1;
    int p[5]={-m,-1,1,m,0};
    int min,u,k;
    for (int i=1;i<=n;i++)
    for (int j=1;j<=m;j++){
        min=h[i][j];
        u=4;
        for (k=0;k<=3;k++)
            if (get(i,j,k)<min) {min=get(i,j,k);u=k;}
        opt[(i-1)*m+j]=(i-1)*m+j+p[u];
      //  cout<<(i-1)*m+j<<" "<<(i-1)*m+j+p[u]<<" "<<u<<endl;
    }
    total=0;
    for (int i=1;i<=n*m;i++) hzz(i);
}
void outans(){
    for (int i=1;i<=n;i++){
        for (int j=1;j<=m;j++) cout<<colour[(i-1)*m+j]<<" ";
        cout<<endl;
    }     
}
int main(){
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    cin>>uu;
    for (int zz=1;zz<=uu;zz++){
    init();
    work();
    cout<<"Case #"<<zz<<":"<<endl;
    outans();
    }
    return 0;
}
