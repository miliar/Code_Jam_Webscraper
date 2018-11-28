
//Written by Alex H Ahmadi (alex@hamedahmadi.com)

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

const int maxn=60;
int a[maxn][maxn];
char b[maxn][maxn];
int m,n;

char pat[2][3]={"/\\","\\/"};

void clear() {
  memset(a,0,sizeof a);
}

void solve(int cnum) {
  cout<<"Case #"<<cnum<<":"<<endl;

  cin>>m>>n;
  FOR (i,m)
	FOR (j,n) {
	char x;
	cin>>x;
	a[i][j]=(x=='#');
	b[i][j]=x;
  }

  FOR (i,m)
	FOR (j,n) 
	if (a[i][j]==1) {
	  FOR (u,2) FOR (v,2) {
		if (a[i+u][j+v]!=1) goto fail;
		a[i+u][j+v]=2;
		b[i+u][j+v]=pat[u][v];
	  }
	}

  FOR (i,m) {
	b[i][n]=0;
	cout<<b[i]<<endl;
  }
  
  return;
 fail:;
  
  cout<<"Impossible"<<endl;

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
