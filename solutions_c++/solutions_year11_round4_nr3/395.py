#include <iostream>
#include <cstdio>
#include <math.h>
#include <string>
#include <string.h>
#include <algorithm>
#include <vector>
using namespace std;
const long maxn = 1000005;
long long n;
long long p[maxn], m;
bool mark[maxn];

void prework()
{
	memset(mark,0,sizeof(mark));
	m = 0;
	for (long long i = 2; i != maxn; ++i)
		if (!mark[i]) {
			p[m++] = i;
			for (long long j = i*2; j < maxn; j+=i) {
				mark[j] = true;
			}			
		}
}

long calc(long long n, long long p)
{
	long long g = p * p;
	for (long i = 1; i <= n; ++i) {
		if (g<=n && n<g*p) return i;
		g*=p;
	}
}

int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C.out","w",stdout);

	prework();
	int TextNum, Num = 0;
	cin >> TextNum;
	while (TextNum--) {
		cout << "Case #" << ++Num << ": ";
		cin >> n;
		long long ans = 1;
		for (long i = 0; i != m; ++i) 
		if (p[i]*p[i]<=n) {
			ans += calc(n,p[i]);
		} else break;
		if (n==1 || n==2) ans = 0;
		cout << ans << endl;
	}

	return 0;
}
