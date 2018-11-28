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

const int INF=0x1fffffff;
#define H 100
#define W 100
int SET[H*W];/* SET */
int G[H][W];
char tag[H][W];/* character */
int h,w;

inline int c2v(int i,int j)
{
  return i*w+j;
}
inline void v2c(int v,int *i,int *j)
{
  *i=v/w;
  *j=v%w;
  return ;
}
int dir[4][2]={{-1,0},
	       {0,-1},
	       {0,1},
	       {1,0}};
void solve()
{
  memset(SET,-1,sizeof(SET));
  for(int i=0;i<h;i++){
    for(int j=0;j<w;j++){
      int alt=G[i][j];
      int u=c2v(i,j);
      int k,ni,nj;
      int other_alt[4]={INF,INF,INF,INF};
      int min_alt=INF;
      for(k=0;k<4;k++){
	ni=i+dir[k][0];
	nj=j+dir[k][1];
	if(ni<0 || ni>=h)continue;
	if(nj<0 || nj>=w)continue;
	other_alt[k]=G[ni][nj];
	min_alt=min(min_alt,G[ni][nj]);
      }
      /* whether can flow */
      if(alt<=min_alt)continue;
      for(k=0;k<4;k++){
	ni=i+dir[k][0];
	nj=j+dir[k][1];
	if(ni<0 || ni>=h)continue;
	if(nj<0 || nj>=w)continue;
	if(other_alt[k]==min_alt)break;
      }
      int v=c2v(ni,nj);
      /* u->v */
      SET[u]=v;
    }
  }
  
  memset(tag,-1,sizeof(tag));
  int tagn=0;
  /* label the tag */
  for(int i=0;i<h;i++){
    for(int j=0;j<w;j++){
      if(tag[i][j]!=-1)continue;      
      int u=c2v(i,j);
      int ni,nj;
      while(SET[u]!=-1)u=SET[u];
      v2c(u,&ni,&nj);
      char ch;
      if(tag[ni][nj]==-1){
	ch=tagn+'a';
	tagn++;
	tag[ni][nj]=ch;
      }else
	ch=tag[ni][nj];
      
      u=c2v(i,j);
      while(SET[u]!=-1){
	int pu=SET[u];
	v2c(u,&ni,&nj);
	tag[ni][nj]=ch;
	u=pu;
      }
    }
  }
  return ;
}
int main()
{
  //freopen("input.txt","r",stdin);
  int casn;
  scanf("%d",&casn);
  for(int t=1;t<=casn;t++){
    scanf("%d %d",&h,&w);
    for(int i=0;i<h;i++){
      for(int j=0;j<w;j++)
	scanf("%d",&(G[i][j]));
    }
    solve();
    printf("Case #%d:\n",t);
    for(int i=0;i<h;i++){
      for(int j=0;j<w-1;j++)printf("%c ",tag[i][j]);
      printf("%c\n",tag[i][w-1]);
    }
  }
  return 0;
}
