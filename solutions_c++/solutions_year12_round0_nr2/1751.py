#include <cstdio>
#include <iostream>
using namespace std;
int main()
{
	int test;
	scanf("%d", &test);
	for(int i = 1; i <= test; i++) {
		int n,s,p;
		int c = 0;
		int t[200];
		scanf("%d%d%d", &n, &s, &p);
		for(int j = 0; j < n; j++) {	
			scanf("%d", &t[j]);
		}
                if(p == 0) {
                        printf("Case #%d: %d\n", i, n);
                        continue;
                }
		for(int j = 0; j < n; j++) {
			int r = t[j]%3;
			int q = t[j]/3;
			if(r != 0) {
				q++;
			}
			if(q >= p) {
				c++;
			} else if(s > 0 && (r == 0 || r == 2) && q+1 >= p && q != 0) {
				c++;
				s--;
			}
		}
		printf("Case #%d: %d\n", i, c);
	}
	return 0;
}
