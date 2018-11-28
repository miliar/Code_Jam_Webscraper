#include<iostream>
using namespace std;

bool g[100][100];
int n,lmatch[100];
bool visited[100];
bool dfs(int st)
{ if(visited[st]) return false;
  visited[st]=true;
  for(int i=0;i<n;++i) if(g[st][i])
    if(lmatch[i]==-1||dfs(lmatch[i]))
    { lmatch[i]=st;
      return true;
    }
  return false;
}

int maxmatch()
{ int i,j,rv=0;
  for(i=0;i<n;++i) lmatch[i]=-1;
  for(i=0;i<n;++i)
  { for(j=0;j<n;++j) visited[j]=false;
    rv+=dfs(i);
  }
  return rv;
}

void mkgraph(int K,int mat[100][25],int N)
{
  int i,j,k;
  n=N;
  for(i=0;i<n;++i) for(j=0;j<n;++j)
  { for(k=0;k<K;++k) if(mat[i][k]>=mat[j][k]) break;
    g[i][j]=(k==K);
  }
}

int main()
{
  int ci,cn;
  cin>>cn;
  for(ci=1;ci<=cn;++ci)
  { int n,k,i,j,mat[100][25];
    cin>>n>>k;
    for(i=0;i<n;++i) for(j=0;j<k;++j) cin>>mat[i][j];
    mkgraph(k,mat,n);
    cout<<"Case #"<<ci<<": "<<n-maxmatch()<<endl;
  }
}
