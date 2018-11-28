#pragma comment(linker, "/STACK:36777216")
#include <iostream>
#include <cstdio>
#include <vector>
#include <cmath>
#include <string>
#include <map>
#include <set>
#include <algorithm>
#include <queue>
#include <stack>
#include <ctime>

#define pb push_back
#define mp make_pair
#define sz size()
#define all(a) (a).begin(),(a).end()
#define rall(a) (a).rbegin(),(a).rend()
#define vint vector<int>
#define rep(i,n) for (int i=0; i<n; i++)
#define ll long long

using namespace std;

const int INF=~(1<<31);
const double EPS=1;
const double PI=3.141592653589793;

int main() {
#ifdef _DEBUG
  freopen("in.txt","r",stdin);
  freopen("out.txt","w",stdout);
#endif
  int T;
  cin>>T;
  for(int t=1; t<=T; t++) {
	  vector<string>s(4);
	  rep(i,4) cin>>s[i];
	  bool lo,lx,wo=0,wx=0;
	  int cnt=0;
	  rep(i,4) {
		  lo=0;
		  lx=0;
		  rep(j,4) {
			  if (s[i][j]=='.') cnt++;
			  if (s[i][j]=='X'||s[i][j]=='.') lo=1;
			  if (s[i][j]=='O'||s[i][j]=='.') lx=1;
		  }
		  if(lo==0) wo=1;
		  if(lx==0) wx=1;
	  }
	  rep(i,4) {
		  lo=0;
		  lx=0;
		  rep(j,4) {
			  if (s[j][i]=='X'||s[j][i]=='.') lo=1;
			  if (s[j][i]=='O'||s[j][i]=='.') lx=1;
		  }
		  if(lo==0) wo=1;
		  if(lx==0) wx=1;
	  }
	  lo=0;
	  lx=0;
	  rep(i,4) {
		  if (s[i][i]=='X'||s[i][i]=='.') lo=1;
		  if (s[i][i]=='O'||s[i][i]=='.') lx=1;
	  }
	  if(lo==0) wo=1;
	  if(lx==0) wx=1;
	  lo=0;
	  lx=0;
	  rep(i,4) {
		  if (s[i][3-i]=='X'||s[i][3-i]=='.') lo=1;
		  if (s[i][3-i]=='O'||s[i][3-i]=='.') lx=1;
	  }
	  if(lo==0) wo=1;
	  if(lx==0) wx=1;
	  if (wx) {
		  printf("Case #%d: X won\n",t);
	  } else if (wo) {
		  printf("Case #%d: O won\n",t);
	  } else if (cnt>0) {
		  printf("Case #%d: Game has not completed\n",t);
	  } else {
		  printf("Case #%d: Draw\n",t);
	  }
  }
  return 0;
}