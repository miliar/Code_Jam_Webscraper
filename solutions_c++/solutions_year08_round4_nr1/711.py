#include<iostream>
#include<vector>
#include<string>
using namespace std;
int nodeval[10001];
int nodegate[10001];
int nodegchange[10001];
int soln[10001][2];
int N;
int startleaf;
int recur(int cur,int val)
{ if(cur>=startleaf)
  { if(nodeval[cur]==val)
    return 0;
    else
    return 100000000;
  }
  if(soln[cur][val]!=-1)
  return soln[cur][val];
  int&res=soln[cur][val];
  res=100000000;
  for(int i=0;i<2;i++)
  for(int j=0;j<2;j++)
  for(int k=0;k<2;k++)
  if(k==1)
  { int temp=(i&&j);
    if(temp==val)
    { int sum=0;
      sum=recur(cur*2+1,i);
      sum+=recur(cur*2+2,j);
      if(nodegate[cur]==k)
      res=min(res,sum);
      else if(nodegchange[cur]==1)
      res=min(res,sum+1);
     }
  }
  else if(k==0)
  { int temp=(i||j);    
    if(temp==val)
    { int sum=0;
      sum=recur(cur*2+1,i);
      sum+=recur(cur*2+2,j);
      if(nodegate[cur]==k)
      res=min(res,sum);
      else if(nodegchange[cur]==1)
      res=min(res,sum+1);
    }
  }
  return res;
}  
int main()
{ int T;
  cin>>T;
  for(int t=0;t<T;t++)
  { int M,V;
    cin>>M>>V;
    N=M;
    for(int i=0;i<(M-1)/2;i++)
    cin>>nodegate[i]>>nodegchange[i];
    startleaf=(M-1)/2;
    for(int i=0;i<(M+1)/2;i++)
    cin>>nodeval[startleaf+i];
    for(int i=0;i<10001;i++)
    for(int j=0;j<2;j++)
    soln[i][j]=-1;
    int res=recur(0,V);
    if(res<100000)
    cout<<"Case #"<<t+1<<": "<<res<<"\n";
    else
    cout<<"Case #"<<t+1<<": IMPOSSIBLE\n";
  }
}
    
