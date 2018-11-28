#include<iostream>
using namespace std;
const int d[4][2]={{-1,0},{0,-1},{0,1},{1,0}};
int n,m,col;
int map[200][200],f[200][200],w[200][200];
int go(int x,int y){
    if(map[x][y]!=0)return(map[x][y]);
    int Min=w[0][0];
    int i;
    for(i=0;i<4;i++)
        if(Min>w[x+d[i][0]][y+d[i][1]])
            Min=w[x+d[i][0]][y+d[i][1]];
    if(Min>=w[x][y]){
        if(map[x][y]==0){
            map[x][y]=col;
            col++;
        }
        return(map[x][y]);
    }
    for(i=0;i<4;i++)
        if(Min==w[x+d[i][0]][y+d[i][1]]){
            map[x][y]=go(x+d[i][0],y+d[i][1]);
            break;
        }
    return(map[x][y]);
}
int main(){
    int i,j,t;
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    cin>>t;
    for(int ii=1;ii<=t;ii++){
        cin>>n>>m;
        for(i=1;i<=n;i++)
            for(j=1;j<=m;j++){
                cin>>w[i][j];
                f[i][j]=i*n+j;
            }
        for(i=0;i<=n+1;i++)
            w[i][0]=w[i][m+1]=100000000;
        for(i=0;i<=m+1;i++)
            w[0][i]=w[n+1][i]=100000000;
        col='a';
        memset(map,0,sizeof(map));
        for(i=1;i<=n;i++)
            for(j=1;j<=m;j++)
                go(i,j);
        cout<<"Case #"<<ii<<":"<<endl;
        for(i=1;i<=n;i++){
            for(j=1;j<m;j++)
                cout<<(char)map[i][j]<<" ";
            cout<<(char)map[i][m]<<endl;
        }
    }
    return(0);
}



