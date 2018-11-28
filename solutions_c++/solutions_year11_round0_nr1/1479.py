
#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

main()
{
	int t; scanf("%d", &t);
	for(int it=0; it<t; it++) {
		int n; scanf("%d", &n);

		int tt[2] = {0, 0};
		int pp[2] = {1, 1};
		int cur=0;

		for(int i=0; i<n; i++) {
			char c; int p; scanf(" %c%d", &c, &p);
			int ir = c=='O' ? 1 : 0;
			int mov = abs(pp[ir] - p);
			int tm = max(0, mov - (cur-tt[ir]));
			cur += tm+1;
			pp[ir] = p;
			tt[ir] = cur;
		}
		printf("Case #%d: %d\n", it+1, cur);
	}
	return 0;
}

