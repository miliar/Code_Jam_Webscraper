#include <cstdio>
#include <algorithm>
#include <cstring>

using namespace std;

long long bubbleSort(long long a[], int n) {
	long long count = 0;
	
	long long pot = 2;
	for (int i = 0; i < n; i++) {
		//printf("i = %d\n", i);
		for (int j = i; j < n; j++)
			if (a[j] < pot) {
				//printf("j = %d pot=%lld a[j]=%lld\n", j, pot, a[j]);
				count += j - i;
				for (int l = j; l >= i; l--) {
					long long tmp = a[l];
					a[l] = a[l - 1];
					a[l - 1] = tmp;
				}
				break;
			}
		pot *= 2;
	}
	return count;
}

int main() {
	int n, test;
	scanf("%d\n", &test);
	for (int l = 1; l <= test; l++) {
		scanf("%d\n", &n);

		long long nonOrdered[n];
		
		char line[n];
		for (int i = 0; i < n; i++) {
			scanf("%[01]\n", line);
			
			reverse(line, line + n);
			nonOrdered[i] = 0;
			for (int j = 0; j < n; j++)
				nonOrdered[i] = (nonOrdered[i] << 1) + line[j] - '0';
		}
		
		printf("Case #%d: %lld\n", l, bubbleSort(nonOrdered, n));
	}
	return 0;
}

