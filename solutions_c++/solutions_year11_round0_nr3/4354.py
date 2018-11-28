#include<cstdio>
#include<algorithm>

/* Author: Anu Bandi */

using namespace std;

int size;

int splits(int arr[], int index, int wLeft, int wRight, int left, int right) {
	if(index >= size) {
		if(wLeft == wRight && left != 0 && right != 0) {
			return max(left, right);
		} else {
			return -1;
		}
	}
	int value = arr[index];
	int l = splits(arr, index + 1, wLeft ^ value, wRight, left + value, right);
	int r = splits(arr, index + 1, wLeft, wRight ^ value, left, right + value);
	return max(l, r);
}

int main() {
	int numCases;
	scanf("%d", &numCases);
	for(int c = 1; c <= numCases; c++) {
		scanf("%d", &size);
		int pile[size];
		for(int i = 0; i < size; i++) {
			scanf("%d", &pile[i]);
		}

		int ans = splits(pile, 0, 0, 0, 0, 0);
		if(ans <= 0) {
			printf("Case #%d: NO\n", c);
			fprintf(stderr, "Case #%d: NO\n", c);
		} else {
			printf("Case #%d: %d\n", c, ans);
			fprintf(stderr, "Case #%d: %d\n", c, ans);
		}
	}

	return 0;
}
