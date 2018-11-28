#include<iostream>
#include<vector>
#include<string>
using namespace std;
int grid[41];
char arr[100];
int main()
{ int T;
  cin>>T;
  for(int t=0;t<T;t++)
  { int N;
    cin>>N;
    for(int i=0;i<N;i++)
    { cin>>arr;
      int mxp=-1;
      for(int j=0;j<N;j++)
      if(arr[j]=='1')
      mxp=j;
      grid[i]=mxp;
    }
    int res=0;
    for(int i=0;i<N;i++)
    if(grid[i]>i)
    { int pos=-1;
      for(int j=i+1;j<N;j++)
      if(grid[j]<=i)
      { pos=j;
        break;
      }
      res+=(pos-i);
      int val=grid[pos];
      for(int j=pos;j>i;j--)
      grid[j]=grid[j-1];
      grid[i]=val;
    }
     //cout<<i<<" "<<res<<" "<<grid[i]<<"\n";
    //}
    cout<<"Case #"<<t+1<<": "<<res<<"\n";
  }
}  
