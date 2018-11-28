#include <iostream>
using namespace std;

int a[2000];

int cmp(const void *a , const void *b)
{
	int *c = (int *)a;
	int *d = (int *)b;
	return *c - *d;
}

int main()
{
	freopen("in.txt" , "r" , stdin);
	freopen("out.txt" , "w" , stdout);
	int t;
	int n;
	int temp;
	int cas = 0;
	int total;

	scanf("%d" , &t);
	while (t--) {
		cas++;
		scanf("%d" , &n);
		temp = 0;
		total = 0;
		for (int i=0 ; i<n ; i++) {
			scanf("%d" , &a[i]);
		}

		for (int i=0 ; i<n ; i++) {
			total += a[i];
		}

		for (int i=0 ; i<n ; i++) {
			temp ^= a[i];
		}

		printf("Case #%d: " , cas);
		if (temp != 0) {
			printf("NO\n");
		}
		else {
			qsort(a , n , sizeof(a[0]) , cmp);
			printf("%d\n" , total - a[0]);
		}
	}

	return 0;
}