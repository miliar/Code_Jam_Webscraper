#include<iostream>
#include<vector>
#include<string>
using namespace std;
int lgrid[10][10];
int sgrid[10][10];
int perm[10];
int ver[20];
int main()
{ int T;
  cin>>T;
  for(int t=0;t<T;t++)
  { int N,M;
    cin>>N;
    for(int i=0;i<10;i++)
    for(int j=0;j<10;j++)
    lgrid[i][j]=sgrid[i][j]=0;
    for(int i=0;i<N-1;i++)
    { int v1,v2;
      cin>>v1>>v2;
      lgrid[v1-1][v2-1]=1;
      lgrid[v2-1][v1-1]=1;
    }
    cin>>M;
    for(int i=0;i<M-1;i++)
    { int v1,v2;
      cin>>v1>>v2;
      sgrid[v1-1][v2-1]=1;
      sgrid[v2-1][v1-1]=1;
    }
    for(int i=0;i<M;i++)
    perm[i]=i;
    for(int i=M;i<N;i++)
    perm[i]=M;
    int res=0;
    do
    { for(int i=0;i<N;i++)
      if(perm[i]<M)
      ver[perm[i]]=i;
      int valid=1;
      for(int i=0;i<M;i++)
      for(int j=0;j<M;j++)
      if(sgrid[i][j]==1&&lgrid[ver[i]][ver[j]]==0)
      { valid=0;
        break;
      }
      if(valid)
      { res=1;
        break;
      }
    }while(next_permutation(perm,perm+N));
    if(res)
    cout<<"Case #"<<t+1<<": YES\n";
    else
    cout<<"Case #"<<t+1<<": NO\n";
  }
}    
      
    
