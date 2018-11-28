#include <cstdio>
#include <cstdlib>
#include <iostream>

using namespace std;
int a[10000];
int b[10000];

int solve() {
	int n; scanf("%d", &n);
	int ans=0;
	for (int i=0; i<n; ++i) scanf("%d%d",&a[i], &b[i]);

	for (int i=0; i<n; ++i)
		for (int j=i+1; j<n; ++j) {
			if ( !( (a[j]>a[i] && b[j]>b[i]) || (a[j]<a[i] && b[j]<b[i]) ) )
				++ans;
		}
	return ans;
}

int main()
{
	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);

	int T; scanf("%d", &T);
	for (int i=1; i<=T; ++i) printf("Case #%d: %d\n", i, solve() );
}
