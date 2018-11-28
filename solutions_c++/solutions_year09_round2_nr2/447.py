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

string go(string s){
	sort(s.begin(),s.end());
	int i_mi = -1;
	for(int i=0;i<s.size();++i){
		if(s[i] != '0'){
			i_mi = i;
			break;
		}
	}
	swap(s[i_mi],s[0]);
	return s;
}

void solve(){
	char buf[100];
	gets(buf);
	string s = buf;
	if(next_permutation(s.begin(),s.end())){
		printf("%s",s.c_str());
	}
	else{
		s += "0";
		string ss = go(s);
		printf("%s",ss.c_str());
	}
}

int main(){
  freopen("input.txt","r",stdin);
  freopen("output.txt","w",stdout);

  int T;
  scanf("%d\n",&T);
  for(int t = 1; t <= T; ++t){
	  printf("Case #%d: ",t);
	  solve();
	  printf("\n");
  }

  return 0;
}