#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <algorithm>
#include <string>
#include <vector>
#include <deque>
#include <sstream>
#include <set>
#include <numeric>
#include <map>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <memory>

template<typename _T,typename _S> _T cast(_S _a) {std::stringstream _s;_s << _a;_T _r; _s >> _r;return _r;}
template<typename end_type> std::vector<end_type> split(const std::string& s,const std::string &delim = " "){std::vector<end_type>res;std::string t;for(int i=0;i!=s.size();++i){if(delim.find(s[i])!=std::string::npos){if(!t.empty()){res.push_back(cast<end_type>(t));t="";}}else {t+=s[i];}} if(!t.empty()){res.push_back(cast<end_type>(t));}return res;}
int s2i(std::string _x) {return cast<int>(_x);}

#define INF 0x7fffffff
#define EPS 1e-12
#define IN(x,a,b) ((x)>(a)&&(x)<(b))
#define round(x) floor(x+0.5)
#define round2(x,p) round(x*(1e-p))/(1e-p)
#define ALL(x) (x).begin(),(x).end()
#define sqr(a) ((a)*(a))
#define WR printf
#define RE scanf
#define FOR(i,Be,En) for(i=(Be);i<=(En);i++)
#define DFOR(i,Be,En) for(i=(Be);i>=(En);i--)
#define PB push_back
#define SZ(a) (int)((a).size())
#define FIT(i,v) for(i=(v).begin();i!=(v).end();i++)
#define RFIT(i,v) for(i=(v).rbegin();i!=(v).rend();i++)
#define FA(i,v) FOR(i,0,SZ(v)-1)
#define RFA(i,v) DFOR(i,SZ(v)-1,0)
#define SE second
#define FI first
#define CLR(a) memset(a,0,sizeof(a))
#define ULL  unsigned long long
#define LL long long

using namespace std;

int dx[] = {0,-1,1,0};
int dy[] = {-1,0,0,1};

int m[105][105];
int q[105][105];
char ans[105][105];
int H,W;
int cur = 0;
pair<int,int> path[105][105];

pair<int,int> fi_ma(){
	int ma = -1;
	pair<int,int> i_ma;
	for(int i=0;i<H;++i)
		for(int j=0;j<W;++j)
			if(m[i][j] > ma && !q[i][j]){
				ma = m[i][j];
				i_ma = make_pair(i,j);
			}
	return i_ma;
		
}

int get(int i,int j){
	if(i>=H || i<0 || j >= W || j < 0)
		return 2000000000;
	return m[i][j];
}

void dfs2(int i, int j,int color){
	pair<int,int>tmp = make_pair(i,j);
	while(tmp.first != -1 && tmp.second != -1){
		q[tmp.first][tmp.second] = color;
		tmp = path[tmp.first][tmp.second];
	}
}

void dfs(int i,int j, pair<int,int> par){
	q[i][j] = cur;
	int mi = m[i][j];
	path[i][j] = par;
	pair<int,int>i_mi;
	for(int a = 0;a<4;++a){
		if(get(i + dy[a],j + dx[a]) < mi){
			mi = get(i + dy[a],j + dx[a]);
			i_mi = make_pair(i+dy[a],j+dx[a]);
		}
	}
	if(mi < m[i][j])
		if(!q[i_mi.first][i_mi.second])
			dfs(i_mi.first,i_mi.second,make_pair(i,j));
		else
			dfs2(i,j,q[i_mi.first][i_mi.second]);
}

void fil(int i,int j,char c,int tt){
	if(i < 0 || i >= H || j < 0 || j >= W)
		return;
	if(ans[i][j])
		return;
	if(q[i][j] != tt)
		return;
	ans[i][j] = c;
	for(int a=0;a<4;++a)		
		fil(i + dy[a],j + dx[a],c,tt);
}

int main(){
  freopen("input.txt","r",stdin);
  freopen("output.txt","w",stdout);

  int n;
  scanf("%d",&n);
  for(int t=1;t<=n;++t){
	  int h,w;
	  scanf("%d%d",&h,&w);
	  H = h;
	  W = w;
	  cur = 0;
	  CLR(m);
	  CLR(q);
	  CLR(path);
	  CLR(ans);
	  for(int i=0;i<h;++i)
		  for(int j=0;j<w;++j){
			  int tmp;
			  scanf("%d",&tmp);
			  m[i][j] = tmp;
		  }
	  bool ok = true;
	  while(ok){
	      pair<int,int>p = fi_ma();
		  cur++;
		  ok = !q[p.first][p.second];
		  if(!q[p.first][p.second])
		     dfs(p.first,p.second,make_pair(-1,-1));
	  }
	  char c = 'a';
	  for(int i=0;i<h;++i)
		  for(int j=0;j<w;++j)
			  if(!ans[i][j])
				  fil(i,j,c++,q[i][j]);

	  printf("Case #%d:\n",t);

	  for(int i=0;i<h;++i){
		  for(int j=0;j<w;++j)
			  if(j)
				  printf(" %c",ans[i][j]);
			  else
				  printf("%c",ans[i][j]);
		  printf("\n");
	  }
  }

  return 0;
}