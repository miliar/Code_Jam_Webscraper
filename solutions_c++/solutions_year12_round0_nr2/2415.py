#include <cstdio>
using namespace std;

int n, s, p1, p2, r;


int main()
{
	int t; scanf("%d", &t);
	for (int T=1; T<=t; ++T) {
		scanf("%d%d%d", &n, &s, &p1); r = 0;
		p1 = 3*p1-2;
		p2 = (p1==1 ? 1 : p1-2);
		
		for (int i=0, a; i<n; ++i) {
			scanf("%d", &a);
			if (a >= p1) ++r;
			else if (s && a >= p2) ++r, --s;
		}
		
		printf("Case #%d: %d\n", T, r);
	}
	
	return 0;
}
