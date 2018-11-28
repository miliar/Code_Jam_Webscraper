#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

const int MAXN = 64;
int t, n;
int a[MAXN];

int main() {
	scanf("%d", &t);
	for (int ti = 0; ti < t; ti++) {
		scanf("%d", &n);
		for (int i = 0; i < n; i++) {
			a[i] = 0;
			for (int j = 0; j < n; j++) {
				char ch;
				scanf(" %c", &ch);
				if (ch == '1')
					a[i] = j+1;
			}
		}

		int cnt = 0;
		for (int i = 0; i < n; i++)
			if (a[i] > i+1) {
				// printf("i = %d\n", i);
				for (int j = i+1; j < n; j++)
					if (a[j] <= i+1) {
						while (j > i) {
							swap(a[j], a[j-1]);
							cnt++;
							j--;
						}
						break;
					}
			}
		printf("Case #%d: %d\n", ti+1, cnt); 
	}
}


