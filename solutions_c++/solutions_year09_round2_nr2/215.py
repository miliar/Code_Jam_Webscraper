#include<stdio.h>
#include<string.h>
#include<stdlib.h>

#include<algorithm>
using namespace std;

int main(void)
{
	freopen("B-large.in", "rt", stdin);
	freopen("pb.out", "wt", stdout);
	
	int tn=0;
	scanf("%d\n", &tn);
	for (int tc=1; tc<=tn; ++tc) {
		char d[64], dd[64];
		gets(d);
		memcpy(dd, d, sizeof(d));
		int n = strlen(d);
		if (next_permutation(d, d+n)) {
			printf("Case #%d: %s\n", tc, d);
		}
		else {
			memcpy(d, dd, sizeof(d));
			for (int i=n+1; i>0; --i)
				d[i] = d[i-1];
			d[0] = '0';
			
			next_permutation(d, d+n+1);
			printf("Case #%d: %s\n", tc, d);
		}
	}
}
