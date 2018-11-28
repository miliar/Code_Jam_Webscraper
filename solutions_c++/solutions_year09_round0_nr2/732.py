#include<iostream>
#include<fstream>
#include<string>
using namespace std;
int H,W;
int B[27];
int M[105][105];
int D[105][105];
int A[105][105];
const int dx[]={-1,0,0,1};
const int dy[]={0,-1,1,0};

void set_dir()
{
 for(int i=0;i<H;++i)
         for(int j=0;j<W;++j)
         {
          int min=M[i][j],sk=-1;
          for(int k=0;k<4;++k)
          {
           int ni=i+dx[k];
           int nj=j+dy[k];
           if(ni<0 || nj<0 || ni>=H || nj>=W || M[ni][nj]>=min)continue;
            min=M[ni][nj];
            sk=k;
          }
          if(sk>=0)D[i][j]=sk;
         }     
}

void dfs(int x,int y,int k)
{
 if(A[x][y]!=-1)return;
 A[x][y]=k;
 for(int i=0;i<4;++i)
 {
  int nx=x+dx[i];
  int ny=y+dy[i];
  if(nx<0 || ny<0 || nx>=H || ny>=W || D[nx][ny]<0)continue;
  if(D[nx][ny]+i==3)dfs(nx,ny,k);
 }     
}

main()
{
 ifstream fin;
 fin.open("C:\\data\\B-large.in");
 ofstream fout;
 fout.open("C:\\data\\B-large.out");
 int T;fin>>T;
 for(int i=1;i<=T;++i)
 {
  fout<<"Case #"<<i<<":"<<endl;
  fin>>H>>W; 
  memset(B,255,sizeof(B));
  for(int j=0;j<H;++j)
          for(int k=0;k<W;++k)
          fin>>M[j][k];
  memset(D,255,sizeof(D));          
  memset(A,255,sizeof(A));
  set_dir();
  int basin=0;
  for(int i=0;i<H;++i)
  for(int j=0;j<W;++j)if(D[i][j]==-1)dfs(i,j,basin++);
  memset(B,255,sizeof(B));
  int C=0;
  for(int i=0;i<H;++i)
  for(int j=0;j<W;++j)if(B[A[i][j]]==-1)B[A[i][j]]=C++;
  for(int i=0;i<H;++i)
  {
   for(int j=0;j<W;++j){
   if(j)fout<<" ";
   fout<<char(B[A[i][j]]+'a');}
   fout<<endl;
  }
 }
 
 fin.close();
 fout.close();      
}
