#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstring>
#include <cassert>

using namespace std;

int a[15];

int main()
{
	int cases;
	scanf("%d", &cases);
	for(int gi=1; gi<=cases; ++gi){
		int n;
		scanf("%d", &n);
		for(int i=0; i<n; ++i) scanf("%d", &a[i]);
		int mn = a[0];
		for(int i=1; i<n; ++i) mn = min(mn, a[i]);
		int sum = 0;
		for(int i=0; i<n; ++i) sum += a[i];
		int xr = 0;
		for(int i=0; i<n; ++i) xr ^= a[i];
		printf("Case #%d: ", gi);
		printf(xr != 0 ?  "NO\n" : "%d\n", sum - mn);
	}
	return 0;
}
