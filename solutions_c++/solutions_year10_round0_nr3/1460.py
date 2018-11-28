
//Written by Alex Hamed Ahmadi (alex@hamedahmadi.com)

#include <iostream>
#include <cstdlib>
#include <cstring>

using namespace std;

#define FOR(i,n) for (int i=0;i<(n);i++)
#define FORIT(it,s) for (__typeof(s.begin()) it=s.begin(); it!=s.end(); ++it)
#define ALL(x) (x).begin(),(x).end()
#define P(x) cerr<<#x<<" = "<<x<<endl;
#define pb push_back

const int maxn=1100;

typedef long long ll;

int r,k,n;
int a[maxn];
ll sum[maxn];
int next[maxn];
int mark[maxn];

ll solve() {
  scanf("%d%d%d",&r,&k,&n);
  FOR (i,n) scanf("%d",&a[i]);
  FOR (i,n) {
	ll s=0;
	int j, pos;
	for (j=0,pos=i;j<n;j++,pos=(pos+1)%n) {
	  if (s+a[pos]>k) break;
	  s+=a[pos];	  
	}
	sum[i]=s;
	next[i]=pos;
  }

  memset(mark, 0, sizeof mark);

  int loopcnt=0;
  ll loopsum=0;
  int pos=0;
  while (!mark[pos]) {
	mark[pos]=++loopcnt;
	loopsum+=sum[pos];
	pos=next[pos];
  }
  int loopstart = pos;

  ll loopsum2=0;
  int looplen=0;
  memset(mark,0,sizeof mark);
  while (!mark[pos]) {
	mark[pos]=++looplen;
	loopsum2+=sum[pos];
	pos=next[pos];
  }

  int startcnt=loopcnt-looplen;
  ll startsum=loopsum-loopsum2;

  ll total = 0;

  pos=0;

  if (r>=startcnt) {
	total+=startsum;	
	r-=startcnt;

	pos=loopstart;

	total+=(r/looplen)*loopsum2;
	r%=looplen;
  }
 
  FOR (i,r) {
	total+=sum[pos];
	pos=next[pos];
  }

  return total;
}

int main () {
  int nt;
  cin>>nt;
  for (int test=1; test<=nt; test++) {
	cout<<"Case #"<<test<<": ";
	ll ans=solve();
	cout<<ans<<endl;
  }

  return 0;
}
