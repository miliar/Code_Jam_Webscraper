#include<fstream>
#include<iostream>
#include<algorithm>
using namespace std;
ifstream fin("B.in");
ofstream fout("B.out");
ofstream f2out("B2.out");
bool vis[27];
int flood[105][105],map[105][105],b=0,H,W;
int dh[]={-1,0,0,1};
int dw[]={0,-1,1,0};
int rec(int h,int w)
{
    int i,v=0,ii=-1,jj=-1,minx=map[h][w];
    for(i=0;i<4;i++)
    {
        int nh=h+dh[i],nw=w+dw[i];
        if(nh<0||nh>=H||nw<0||nw>=W)continue;
        if(map[nh][nw]<minx)
        ii=nh,jj=nw,minx=map[nh][nw];
    }
    if(ii==-1&&jj==-1)
    {
       if(flood[h][w]!=-1)return flood[h][w];
       return flood[h][w]=b++;
    }
    return flood[h][w]=rec(ii,jj);
}
int main()
{
    int T;
    fin>>T;
    for(int k=0;k<T;k++)
    {
        b=0;
        fin>>H>>W;
        fout<<"Case #"<<k+1<<":"<<endl;
        memset(flood,-1,sizeof(flood));
        int i,j;
        for(i=0;i<H;i++)
        for(j=0;j<W;j++)
        fin>>map[i][j];
        for(i=0;i<H;i++){
        for(j=0;j<W;j++)
        f2out<<map[i][j]<<" ";
        f2out<<endl;}
        for(i=0;i<H;i++)
        {
           for(j=0;j<W;j++)
           {
              if(flood[i][j]==-1)
              rec(i,j);
           }
        }
        for(i=0;i<H;i++){
        for(j=0;j<W;j++)
        fout<<char(flood[i][j]+'a')<<" ";
        fout<<endl;}
    }
    return 0;
}
