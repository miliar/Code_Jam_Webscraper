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

char *pp = "welcome to code jam";

int dp[505][25];

int main(){
  freopen("C-small.in","r",stdin);
  freopen("C-small.out","w",stdout);

  int n;
  scanf("%d\n",&n);

  int qq = strlen(pp);

  for(int t=1;t<=n;++t){
	  CLR(dp);
	  char buf[505];
	  gets(buf);
	  int len = strlen(buf);
	  //dp[0][0] = buf[0] == 'w';
	  //dp[0][0] = 1;
	  for(int i=0;i<len;++i){
		  for(int l = 0;l < qq;++l){			  			  
			  if(buf[i] == pp[l]){
				  if(buf[i] == 'w'){
					  dp[i][l] = 1;	
					  continue;
				  }
				  for(int j = i - 1; j >= 0; --j)
					  dp[i][l] = (dp[i][l] + dp[j][l-1])%10000;
			  }
		  }		  
	  }
	  int ans = 0;
	  for(int i=0;i<len;++i)
		  ans = (ans + dp[i][qq-1])%10000;
	  sprintf(buf,"%d",ans);
	  string s = buf;
	  if(SZ(s) < 4){
		  int tt = SZ(s);
		  for(int i=0;i < 4 - tt;++i)
			  s = "0" + s;
	  }
	  printf("Case #%d: %s\n",t,s.c_str());
  }

  return 0;
}