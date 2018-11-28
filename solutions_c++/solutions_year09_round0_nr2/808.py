#include<iostream>
#include<vector>
#include<string>
using namespace std;
int grid[200][200];
int vis[200][200];
int cmp=0;
int H,W;
int di[]={-1,0,0,1};
int dj[]={0,-1,1,0};
int dfs(int i,int j)
{ //cout<<i<<" "<<j<<"\n";
  if(vis[i][j]==-1)
  { 
    int pos=-1;
    int ch=grid[i][j];
    for(int k=0;k<4;k++)
    if(i+di[k]>=0&&i+di[k]<H&&j+dj[k]>=0&&j+dj[k]<W&&grid[i+di[k]][j+dj[k]]<ch)
    { ch=grid[i+di[k]][j+dj[k]];
      pos=k;
    }
    if(pos==-1)
    { vis[i][j]=cmp;
      cmp++;
      return vis[i][j];
    }  
    else
    { vis[i][j]=dfs(i+di[pos],j+dj[pos]);
      return vis[i][j];
    }
  }
  else
  return vis[i][j];
}
int main()
{ int T;
  cin>>T;
  for(int t=0;t<T;t++)
  { cmp=0;
    cin>>H>>W;
    for(int i=0;i<H;i++)
    for(int j=0;j<W;j++)
    vis[i][j]=-1;
    for(int i=0;i<H;i++)
    for(int j=0;j<W;j++)
    cin>>grid[i][j];
    cout<<"Case #"<<t+1<<":\n";
    for(int i=0;i<H;i++,cout<<"\n")
    for(int j=0;j<W;j++)
    { cout<<char('a'+dfs(i,j))<<" ";
    }
  }
}  
