
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

const int maxn=2100;
int a[maxn];
int y[maxn];
bool peak[maxn];
int p[maxn];
int np=0;
int n;
bool mark[maxn];
int slope[maxn];
int curslope;

void clear() {
  zer(peak);
  zer(mark);
}

void dfs(int x) {
  if (x==n) return;
  if (mark[x]) return;
  mark[x]=1;
  dfs(a[x]);
  y[x]=y[a[x]]-curslope*(a[x]-x);
}

void solve(int cnum) {
  cout<<"Case #"<<cnum<<": ";

  zer(y);
  cin>>n;
  for (int i=1;i<=n-1;i++) {
	cin>>a[i];
  }

  for (int i=1;i<=n-1;i++) {
	peak[a[i]]=1;
	int j=a[i];
	for (int k=i+1;k<j;k++) {
	  if (peak[k]) goto fail;
	}
	peak[j]=1;
	if (y[i]<y[j]) continue; //all good
	if (y[i]>y[j]) {
	  cerr<<"WRONG WRONG WRONG"<<endl;
	}
  }

  //np=0;
  //for (int i=1;i<=n;i++) if (peak[i]) p[np++]=i;
  //for (int i=1;i<=n;i++) if (peak[i]) y[i]=2; else y[i]=1;
  curslope=0;
  for (int i=1;i<=n;i++) {
	if (!mark[i]) {
	  dfs(i);
	  curslope++;
	}
  }

  int top=y[1];
  for (int i=1;i<=n;i++) top=min(top,y[i]);
  top--;
  for (int i=1;i<=n;i++) y[i]-=top;

  for (int i=1;i<=n;i++) cout<<y[i]<<" ";
  cout<<endl;
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
