#include <algorithm>
#include <stdio.h>

using namespace std;

int n;
struct _data {
	int l, p;
	int index;
	inline bool operator < (const _data &rhs) const {
		return l*(100-rhs.p) + 100*rhs.l == rhs.l*(100-p) + 100*l ? index < rhs.index : l*(100-rhs.p) + 100*rhs.l > rhs.l*(100-p) + 100*l;
	}
};
_data data[1010];

int main()
{
	int i, j;

	int t, tt=0;

	scanf("%d", &t);
	while (t--) {
		scanf("%d", &n);
		for (i=0; i<n; i++) scanf("%d", &data[i].l);
		for (i=0; i<n; i++) scanf("%d", &data[i].p);

		for (i=0; i<n; i++) data[i].index = i;

		for (i=0; i<n; i++) {
			for (j=i; j>0; j--) {
				if (data[j] < data[j-1])
					swap(data[j-1], data[j]);
			}
		}

		printf("Case #%d: ", ++tt);
		for (i=0; i<n; i++) printf("%d ", data[i].index);
		printf("\n");
	}

	return 0;
}
