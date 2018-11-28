#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cstring>
#include<vector>
using namespace std;
typedef long long LL;
int gcd (int a, int b)
{
   if (b == 0)
      return a;
   else
      return gcd (b, a % b);
}

vector<LL> a(111),A(111),b(111),B(111);
int n,m;
LL solve(vector<LL>a,vector<LL>b,int p, int q) {
  if (p >= n) return 0;
  if (q >= m) return 0;
  LL ans = 0;
  if (A[p] == B[q]) {
    LL v = min(a[p], b[q]);
    a[p] -= v;
    b[q] -= v;
    if (a[p] == 0) p++;
    if (b[q] == 0) q++;
    ans = v;
    ans += solve(a, b, p , q);
  } else {
    ans += max (solve(a, b, p+1 , q), max(solve(a, b, p , q+1), solve(a, b, p+1 , q+1)));
  }
  return ans;
}

int main() {
	int T;
	cin>>T;
	for(int tc=1;tc<=T;tc++) {
		scanf("%d%d", &n, &m);
		for (int i = 0; i < n; i++) scanf("%lld%lld",&a[i],&A[i]);
		for (int i = 0; i < m; i++) scanf("%lld%lld",&b[i],&B[i]);
		printf("Case #%d: %lld\n",tc,solve(a, b, 0, 0));
	}
	return 0;
}
