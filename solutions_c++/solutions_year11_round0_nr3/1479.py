
#include <iostream>
#include <cstdio>
using namespace std;

main()
{
	int tc; cin>>tc;
	for(int it=1; it<=tc; it++) {
		int n; cin>>n;
		int v[n]; for(int i=0; i<n; i++) cin>>v[i];
		int s1=0; for(int i=0; i<n; i++) s1 += v[i];
		int s0=0; for(int i=0; i<n; i++) s0 ^= v[i];
		int m0=v[0]; for(int i=0; i<n; i++) m0 = min(m0, v[i]);

		int ans;
		if(!s0) {
			ans = s1 - m0;
		}
		else {
			ans = 0;
		}

		printf(ans ? "Case #%d: %d\n" : "Case #%d: NO\n", it, ans);
	}
	return 0;
}


