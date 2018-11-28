#include<iostream>
#include<vector>
using namespace std;
int user[100][100][2];
void print(int val,int n)
{ for(int i=0;i<n;i++)
  { cout<<((val>>i)&1);
    if(i<n-1)
    cout<<" ";
  }
}
int main()
{ int T;
  cin>>T;
  for(int k=0;k<T;k++)
  { int N,M;
    cin>>N;
    cin>>M;
    for(int i=0;i<100;i++)
    for(int j=0;j<100;j++)
    for(int m=0;m<2;m++)
    user[i][j][m]=0;
    for(int i=0;i<M;i++)
    { int n;
      cin>>n;
      for(int j=0;j<n;j++)
      { int x,y;
        cin>>x;
        cin>>y;
        user[i][x-1][y]=1;
      }
    }  
    int res=N+1;
    int ans=-1;
    for(int i=0;i<(1<<N);i++)
    { int valid=1;
      for(int j=0;j<M;j++)
      { int sat=0;
        for(int m=0;m<N;m++)
        { int fval=((i>>m)&1);
          if(user[j][m][fval])
          { sat=1;
            break;
          }
        }
        if(sat==0)
        { valid=0;
          break;
        }
      }
      if(valid)
      { int mc=0;
        for(int j=0;j<N;j++)
        if((i>>j)&1)
        mc++;
        if(res>mc)
        { res=mc;
          ans=i;
        }
      }
    }
    if(res<=N)
    { cout<<"Case #"<<k+1<<": ";
      print(ans,N);
      cout<<"\n";
    }
    else
    cout<<"Case #"<<k+1<<": "<<"IMPOSSIBLE\n";
  }
}
