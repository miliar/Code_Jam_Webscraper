#include <iostream>
#include <sstream>
#include <iomanip>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <cctype>
using namespace std;

#define inf 20000

int solve(int pos,int val,int m,
	  vector<int> &node,
	  vector<int> &change,
	  vector<vector<int> > &tbl)
{
  if (pos>=m/2)
    return (node[pos]==val?0:inf);

  int &ret=tbl[val][pos];
  if (ret>=0) return ret;

  ret=inf;

  if (val==1){
    ret<?=
      solve(2*pos+1,1,m,node,change,tbl)+
      solve(2*pos+2,1,m,node,change,tbl)+
      (node[pos]==1?0:change[pos]==1?1:inf);
  }
  else{
    ret<?=
      solve(2*pos+1,0,m,node,change,tbl)+
      solve(2*pos+2,0,m,node,change,tbl)+
      (node[pos]==1?0:change[pos]==1?1:inf);
    ret<?=
      solve(2*pos+1,0,m,node,change,tbl)+
      solve(2*pos+2,1,m,node,change,tbl)+
      (node[pos]==1?0:change[pos]==1?1:inf);
    ret<?=
      solve(2*pos+1,1,m,node,change,tbl)+
      solve(2*pos+2,0,m,node,change,tbl)+
      (node[pos]==1?0:change[pos]==1?1:inf);
  }

  if (val==1){
    ret<?=
      solve(2*pos+1,1,m,node,change,tbl)+
      solve(2*pos+2,1,m,node,change,tbl)+
      (node[pos]==0?0:change[pos]==1?1:inf);
    ret<?=
      solve(2*pos+1,0,m,node,change,tbl)+
      solve(2*pos+2,1,m,node,change,tbl)+
      (node[pos]==0?0:change[pos]==1?1:inf);
    ret<?=
      solve(2*pos+1,1,m,node,change,tbl)+
      solve(2*pos+2,0,m,node,change,tbl)+
      (node[pos]==0?0:change[pos]==1?1:inf);
  }
  else{
    ret<?=
      solve(2*pos+1,0,m,node,change,tbl)+
      solve(2*pos+2,0,m,node,change,tbl)+
      (node[pos]==0?0:change[pos]==1?1:inf);
  }

  //cout<<pos<<", "<<val<<": "<<ret<<endl;

  return ret;
}

void process()
{
  int m,v;cin>>m>>v;
  vector<int> node(m);
  vector<int> change(m);
  for (int i=0;i<m/2;i++){
    int g,c;cin>>g>>c;
    node[i]=g;
    change[i]=c;
  }
  for (int i=m/2;i<m;i++)
    cin>>node[i];
  vector<vector<int> > tbl(2,vector<int>(m,-1));

  int ans=solve(0,v,m,node,change,tbl);

  if (ans>=inf) cout<<"IMPOSSIBLE"<<endl;
  else cout<<ans<<endl;
}

int main()
{
  string line;
  getline(cin,line);
  int cases=atoi(line.c_str());
  for (int c=1;c<=cases;c++){
    cout<<"Case #"<<c<<": ";
    process();
  }
}
