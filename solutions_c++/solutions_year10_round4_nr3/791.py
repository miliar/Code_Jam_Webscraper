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

int mem[205][205];
int mem2[205][205];
int n,m;

bool is_clear(){
	for(int i=0;i<=n;++i){
		for(int j=0;j<=m;++j)
			if(mem[i][j] == 1)
				return false;		
	}
	return true;
}

void next(){
	for(int i=0;i<=n;++i){
		for(int j=0;j<=m;++j){
			if(mem[i][j] == 1){
				int t = 0;
				if(i-1 < 0 && j-1 < 0)
					t = 0;
				else{
					if(i-1 < 0)
						t = mem[i][j-1];
					else
						if(j-1 < 0)
							t = mem[i-1][j];
						else
							t = mem[i-1][j] || mem[i][j-1];
					
				}
				mem2[i][j] = t;
			}
			else{
				int t = 0;
				if(i-1 < 0 && j-1 < 0)
					t = 0;
				else{
					if(i-1 < 0)
						t = 0;
					else
						if(j-1 < 0)
							t = 0;
						else
							t = mem[i-1][j] && mem[i][j-1];
					
				}
				mem2[i][j] = t;
			}
		}
	}
	for(int i=0;i<=n;++i)
		for(int j=0;j<=m;++j){
			mem[i][j] = mem2[i][j];
		}
}

int go(){
	int R;
	scanf("%d",&R);
	n = m = 0;
	CLR(mem);
	CLR(mem2);
	for(int i=0;i<R;++i){
		int x1,y1,x2,y2;
		scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
		m = max(m,x2);
		n = max(n,y2);		
		for(int j = x1;j<=x2;++j){
			for(int k=y1;k<=y2;++k){
				mem[k][j] = 1;
			}
		}
	}
	bool ok = is_clear();
	int k =0;
	while(!ok){
		next();
		ok = is_clear();
		k++;
	}
	return k;	
}

void solve(){
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;++t){
		printf("Case #%d: %d\n",t,go());
	}
}

int main(){
  freopen("input.txt","r",stdin);
  freopen("output.txt","w",stdout);
  solve();
  return 0;
}