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

int mas[1005];
int ne[1005];
int sum[1005];

void solve(){
	CLR(mas);
	CLR(ne);
	CLR(sum);

	int R,k,N;
	scanf("%d %d %d",&R,&k,&N);
	for(int i=0;i<N;++i){
		scanf("%d",&mas[i]);
	}
	
	for(int i=0;i<N;++i){
		int tmp = 0;
		bool last_j = false;
		for(int j=i;;++j){			
			if((tmp + mas[j] > k) || (last_j && j == i)){				
				ne[i] = j;
				sum[i] = tmp;
				break;
			}
			tmp += mas[j];
			
			last_j = true;
			if(j == N-1)
				j = -1;
		}
	}

	LL ans = 0;
	int cur = 0;

	for(int i=0;i<R;++i){
		ans += sum[cur];
		cur = ne[cur];				
	}
	cout << ans << "\n";
}

void init(){
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;++t){
		printf("Case #%d: ",t);
		solve();
	}
}

int main(){
  freopen("input.txt","r",stdin);
  freopen("output.txt","w",stdout);

  init();



  return 0;
}