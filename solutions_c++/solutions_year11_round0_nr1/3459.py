#include <stdio.h>
#include <memory.h>
#include <algorithm>
#define MN 101
using namespace std;
int n;
pair<int,char> d[MN];
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t, T, r, i, j, k, p, q, f;
	char str[4];

	scanf("%d",&T);
	for (t = 1; t <= T; t++) {
		scanf("%d",&n);
		for (i = 0; i < n; i++) {
			scanf("%s%d",str,&d[i].first);
			d[i].second = str[0];
		}
		r = 0; p = 1; q = 1;
		for (i = 0; i < n;) {
			r++; f = 0;
			for (j = i; j < n; j++) {
				if (d[j].second == 'B') break;
			}
			if (j < n) {
				if (d[j].first < p) {
					p--;
				}
				else if (d[j].first > p) {
					p++;
				}
				else {
					if (j == i) f = 1;
				}
			}
			for (j = i; j < n; j++) {
				if (d[j].second == 'O') break;
			}
			if (j < n) {
				if (d[j].first < q) {
					q--;
				}
				else if (d[j].first > q) {
					q++;
				}
				else {
					if (j == i) f = 1;
				}
			}
			if (f) i++;
		}
		printf("Case #%d: %d\n",t,r);
	}
	return 0;
}