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

bool cmp(pair<int,int>p1,pair<int,int>p2){
	if(p1.first < p2.first)
		return true;
	if(p1.first == p2.first && p1.second > p2.second)
		return true;
	return false;
}

int go(){
	vector< pair<int,int> >v;
	int n;
	scanf("%d",&n);
	for(int i=0;i<n;++i){
		int a,b;
		scanf("%d%d",&a,&b);
		v.push_back(make_pair(a,b));
	}
	sort(v.begin(),v.end(),cmp);
	int ans = 0;
	for(int i=0;i<v.size();++i){
		for(int j=i + 1;j<v.size();++j){
			if(v[j].first > v[i].first && v[j].second < v[i].second)
				ans++;
		}
	}
	return ans;
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