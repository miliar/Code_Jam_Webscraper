#include<iostream>
using namespace std;
int M[100][100];
char Z[100][100];
int dy[]={-1,0,0,1};
int dx[]={0,-1,1,0};
int C,H,W;
char letra;
char recursion(int r,int c)
{
    if(Z[r][c]!=0)return Z[r][c];
    int xm=-1,ym=-1,mn=M[r][c];
    for(int i=0;i<4;i++)
    {
       int x=r+dy[i];
       int y=c+dx[i];
       if(x<0||y<0||x>=H||y>=W)continue;
       if(M[x][y]<mn)
       {
           xm=x;
           ym=y;
           mn=M[x][y];              
       }
    }
    if(xm==-1){
              letra++;
              return Z[r][c]=letra;
              }
    return Z[r][c]=recursion(xm,ym);
}
int main()

{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    cin>>C;
    for(int caso=1;caso<=C;caso++)
    {
           cin>>H>>W;
           letra='a'-1;
           for(int i=0;i<H;i++)for(int j=0;j<W;j++)cin>>M[i][j];
           for(int i=0;i<H;i++)for(int j=0;j<W;j++)Z[i][j]=0;
           for(int i=0;i<H;i++)for(int j=0;j<W;j++)Z[i][j]=recursion(i,j);
           cout<<"Case #"<<caso<<":"<<endl;
           for(int i=0;i<H;i++){for(int j=0;j<W;j++)cout<<Z[i][j]<<" ";cout<<endl;}         
    }
return 0;
}
