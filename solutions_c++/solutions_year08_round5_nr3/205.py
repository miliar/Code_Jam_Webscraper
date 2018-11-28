#include<iostream>
#include<vector>
using namespace std;
#define MAX 10
int soln[1<<MAX][MAX+1];
int R,C;
char arr[100]="";
vector<string>grid;
int recur(int pstate,int cur)
{ if(cur==R)
  return 0;
  if(soln[pstate][cur]!=-1)
  return soln[pstate][cur];
  int&res=soln[pstate][cur];
  res=0;
  for(int i=0;i<(1<<C);i++)
  if((i&(pstate>>1))||(i&(pstate<<1)))
  ;
  else
  { int valid=1;
    int curc=0;
    for(int j=0;j<C;j++)
    if((i>>j)&1)
    { if(grid[cur][j]=='x')
      valid=0;
      curc++;
    }  
    if(valid)
    for(int j=0;j<C-1;j++)
    if(((i>>j)&1)&&((i>>(j+1))&1))
    { valid=0;
      break;
    }
    if(valid)
    res=max(res,curc+recur(i,cur+1));
  }
  return res;
}  
      
int main()
{ int T;
  cin>>T;
  for(int t=0;t<T;t++)
  { 
    cin>>R>>C;
    for(int i=0;i<(1<<MAX);i++)
    for(int j=0;j<MAX;j++)
    soln[i][j]=-1;
    vector<string>temp;
    for(int i=0;i<R;i++)
    { cin>>arr;
      string str=arr;
      //cerr<<str<<"\n";
      temp.push_back(str);
    }
    //cerr<<"\n\n";
    grid=temp;
    int res=recur(0,0);
    cout<<"Case #"<<t+1<<": "<<res<<"\n";
  }
}  
