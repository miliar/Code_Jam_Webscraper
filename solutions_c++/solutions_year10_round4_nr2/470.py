
//Written by Alex Hamed Ahmadi (alex@hamedahmadi.com)

#include <algorithm>
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <complex>
using namespace std;

#define FOR(i,n) for (int i=0;i<(n);i++)
#define FORIT(it,s) for (__typeof(s.begin()) it=s.begin(); it!=s.end(); ++it)
#define ALL(x) (x).begin(),(x).end()
#define P(x) cerr<<#x<<" = "<<x<<endl
#define pb push_back

#define zer(x) memset(x,0,sizeof(x));
#define isin(x,s) (s.find(x)!=s.end())

typedef long long ll;
typedef vector <int> vi;
typedef set <int> si;
typedef pair <int, int> pii;

const int maxn=1100;
const int maxp=14;

int a[maxn*2];
int price[maxp][maxn];
int d[maxn*2][maxp];

int m;
int p;

void clear() {
  zer(d);
}

const int inf=300000000;

void solve(int cnum) {
  cin>>p;
  m=1<<p;
  FOR (i,m) cin>>a[m+i];

  for (int i=p-1;i>=0;i--)
	for (int j=0;j<(1<<i);j++)
	  cin>>price[i][j];

  for (int x=m;x<2*m;x++) {
	for (int tak=0;tak<p;tak++)
	  if(tak>=(p-a[x])) d[x][tak]=0; else d[x][tak]=inf;
  }
  
  for (int x=m-1;x>=1;x--) {
	int lev=0;
	for (int y=x;y!=1;y/=2,lev++);
	a[x]=min(a[x*2], a[x*2+1]);
	int ticket=price[lev][x-(1<<lev)];;
	for (int tak=0;tak<=lev;tak++) {
	  int ans=inf;
	  //take
	  ans=min(ans, ticket+d[x*2][tak+1]+d[x*2+1][tak+1]);

	  //don't take
	  ans=min(ans, d[x*2][tak]+d[x*2+1][tak]);

	  d[x][tak]=ans;
	}
  }
  
  int ans=d[1][0];

  cout<<"Case #"<<cnum<<": "<<ans<<endl;
}

int main() {
  int nt;
  cin>>nt;
  for (int cnum=1; cnum<=nt; cnum++) {
	clear();
	solve(cnum);
  }
  return 0;
}
