#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <cstring>
#include <cassert>
#include <set>
#include <map>
#include <vector>
using namespace std;

typedef long long int i64;
typedef vector<i64> VI;

int P;
int pt[1000008];
int rk[1000008];
int pr[1000008];
bool pf[1000008];

int goFind(int n);
void goMerge(int a, int b);

#define SIZE(__c) (int)(__c).size()
#define FOREACH(__i, __c) for (typeof(__c.begin()) __i=__c.begin(); __i!=__c.end(); ++__i)

int main() {
  int i, j, t, T;
  i64 BASE, COUNT, lo, hi, Z, n, m;
  pr[P++]=2;
  for (i=3; i<=1000000; i+=2)
    pf[i]=1;
  for (i=3; i<=1000000; i+=2)
    if (pf[i]) {
      pr[P++]=i;
      for (j=i+i+i; j<=1000000; j+=i+i)
	pf[j]=0;
    }
  scanf("%d", &T);
  for (t=1; t<=T; t++) {
    scanf("%lld %lld %lld", &lo, &hi, &Z);
    BASE=lo;
    COUNT=hi-lo+1;
    for (i=0; i<COUNT; i++) {
      pt[i]=i;
      rk[i]=1;
    }
    map<i64, VI> mp;
    for (n=lo; n<=hi; n++) {
      m=n;
      for (i=0; i<P; i++) {
	if (m<pr[i])
	  break;
	if (m%pr[i]==0) {
	  if (pr[i]>=Z)
	    mp[pr[i]].push_back(n);
	  do
	    m/=pr[i];
	  while (m%pr[i]==0);
	}
      }
      if (m!=1)
	mp[m].push_back(n);
    }
    FOREACH(z, mp) {
      const VI &nb=z->second;
      for (i=1; i<SIZE(nb); i++)
	goMerge(nb[0]-BASE, nb[i]-BASE);
    }
    set<int> st;
    for (i=0; i<COUNT; i++)
      st.insert(goFind(i));
    printf("Case #%d: %d\n", t, (int)st.size());
  }
  return 0;
}

int goFind(int n) {
  if (pt[n]!=n)
    pt[n]=goFind(pt[n]);
  return pt[n];
}

void goMerge(int a, int b) {
  a=goFind(a);
  b=goFind(b);
  if (a==b)
    return;
  if (rk[a]<rk[b])
    pt[a]=b;
  if (rk[a]>rk[b])
    pt[b]=a;
  if (rk[a]==rk[b]) {
    pt[a]=b;
    rk[b]++;
  }
}
