/* -*- c++ -*-
   ID: dirtysalt
   PROG: 
   LANG: C++
   copy[write] by dirlt(dirtysalt1987@gmail.com) */
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <ctime>
#include <cassert>
#include <cstring>

#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <list>
#include <queue>
#include <stack>
#include <deque>
#include <map>
#include <numeric>
#include <algorithm>

using namespace std;
typedef long long LL;
typedef vector < int >VI;
typedef vector < string > VS;
typedef vector < double >VD;
typedef pair < int, int >PII;
#define SZ(v) ((int)((sizeof(v))/sizeof(*(v))))
#define PV(v) do {						\
    cout<<#v<<endl;						\
    for(int i=0;i<(int)(v).size();i++)cout<<(v)[i]<<" ";	\
    cout<<endl; \
  }while(0)
#define PA(v) do{							\
    cout<<#v<<endl;							\
    for(int i=0;i<(int)(sizeof(v)/sizeof(*(v)));i++)cout<<(v)[i]<<" ";	\
    cout<<endl;								\
  }while(0)
#define FUNC() do{					\
    cout<<"=========="<<__func__<<"=========="<<endl;	\
  }while(0)
#define N 100000
char mask[10][N+1];
int trans(int base,int x)
{
  int sum=0;
  while(x){
    int i=x%base;
    sum+=i*i;
    x/=base;
  }
  return sum;
}

map<int,bool>tbl;
void fill_mask(vector<int>&v)
{
  for(int k=0;k<(int)v.size();k++){
    int base=v[k];
    memset(mask[k],-1,sizeof(mask[k]));
    mask[k][1]=1;
    for(int i=2;i<=N;i++){
      if(mask[k][i]!=-1)continue;
      int x=i;
      tbl.clear();
      while((tbl.find(x)==tbl.end()) && (mask[k][x]==-1)){
	tbl[x]=true;
	x=trans(base,x);
      }
      int v=0;
      if(mask[k][x]!=-1)v=mask[k][x];
      for(map<int,bool>::iterator it=tbl.begin();it!=tbl.end();++it){
	mask[k][it->first]=v;
      }
    }
  }
}

int main()
{
  int casn;
  //freopen("input.txt","r",stdin);
  scanf("%d\n",&casn);
  for(int t=1;t<=casn;t++){
    vector<int>v;
    string s;
    getline(cin,s);    
    int i=0;
    int sum=0;
    while(i<(int)s.length()){
      while(i<(int)s.length() && s[i]!=' '){
	sum=sum*10+s[i]-'0';
	i++;
      }
      v.push_back(sum);
      sum=0;
      if(s[i]==' ')i++;
    }
    fill_mask(v);
    /*
    for(i=1;i<=10;i++){
      printf("%d ",mask[0][i]);
    }
    printf("\n");
    */
    for(i=2;i<=N;i++){
      bool flag=true;
      for(int k=0;k<(int)v.size();k++){
	if(mask[k][i]==0){
	  flag=false;
	  break;
	}
      }
      if(flag==true)break;
    }
    printf("Case #%d: %d\n",t,i);
  }
  return 0;
}
