#include <stdio.h>
#include  <iostream>
#include <algorithm>
#define maxn 1000
using namespace std;
long long n;
long long s1[maxn],s2[maxn];
int main(void)
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	long long T;
	cin >> T;
	for (int cases = 1;cases <= T;cases++)
	{
		cin >> n;
		for (int i = 0;i < n;i++) cin >> s1[i];
		for (int i = 0;i < n;i++) cin >> s2[i];
		sort(s1,s1 + n);
		sort(s2,s2 + n);
		
		long long ans = 0;
		for (int i = 0;i < n;i++) ans += s1[i] * s2[n - 1 - i];
		cout << "Case #" << cases << ": " << ans << endl;
	}
	return 0;
}
