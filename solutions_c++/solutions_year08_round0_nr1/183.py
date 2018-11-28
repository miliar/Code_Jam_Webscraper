#include<iostream>
#include<stdio.h>
#include<vector>
#include<string>

using namespace std;

int nengine;
int nquery;
char buff[200]="";
vector<string>engine;
vector<string>query;
int dp[101][1001];

void initdparr()
{ for(int i=0;i<101;i++)
  for(int j=0;j<1001;j++)
  dp[i][j]=-1;
}

string getstring()
{ string str="";
  while(str=="")
  { gets(buff);
    str=buff;
  }
  return str;
}
  
int dfswithdp(int engineind,int queryind)
{ if(queryind==nquery)
  return 0;
  if(dp[engineind][queryind]!=-1)
  return dp[engineind][queryind];
  dp[engineind][queryind]=100000000;
  for(int i=0;i<nengine;i++)
  if(engine[i]!=query[queryind])
  dp[engineind][queryind]=min(dp[engineind][queryind],((i==engineind)?0:1)+dfswithdp(i,queryind+1));
  return dp[engineind][queryind];
}
  
int main()
{ int N;
  cin>>N;
  for(int k=0;k<N;k++)
  { nengine=0;
    nquery=0;
    cin>>nengine;
    vector<string>etemp;
    engine=etemp;
    query=etemp;
    initdparr();
    for(int i=0;i<nengine;i++)
    engine.push_back(getstring());
    cin>>nquery;  
    for(int i=0;i<nquery;i++)
    query.push_back(getstring());
    int res=(1<<30);
    if(nquery!=0)
    { for(int i=0;i<nengine;i++)
      if(engine[i]!=query[0])  
      res=min(res,dfswithdp(i,1));
    }
    else
    res=0;
    cout<<"Case #"<<k+1<<": "<<res<<"\n";
  }
}
