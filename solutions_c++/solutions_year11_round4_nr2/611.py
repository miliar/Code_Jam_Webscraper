#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <cstdio>
#include <cstring>
#include <climits>

using namespace std;

int r, c;
char polje[11][11];

int razdalja(int a, int k) {
	int sred;
	if (k % 2 == 1) {
		sred = k / 2;
		return a - sred;
	} else {
		sred = (k - 1) / 2;
		if (a <= sred)
			return a - (sred + 1);
		return a - sred;
	}
}

void task() {
	//read
	scanf("%d%d", &r, &c); gets(polje[0]);
	for (int i = 0; i < r; i++)
		gets(polje[i]);
		
	//solve
	for (int k = min(r, c); k >= 3; k--) {
		for (int i = 0; i <= r - k; i++) {
			for (int j = 0; j <= c - k; j++) {
			
				//k = 5;
				//cout << " + " << i << " " << j << endl;
			
				int xsum = 0;
				int ysum = 0;
				
				for (int a = 0; a < k; a++)
					for (int b = 0; b < k; b++)
						if (!(a == 0 && b == 0) && !(a == k - 1 && b == 0) && !(a == 0 && b == k - 1) && !(a == k - 1 && b == k - 1)) {
							xsum += (int)(polje[i + a][j + b] - '0') * razdalja(a, k);
							ysum += (int)(polje[i + a][j + b] - '0') * razdalja(b, k);
						}
			
				//cout << xsum << " " << ysum << endl;
			
				if (xsum == 0 && ysum == 0) {
					cout << k << endl;
					return;
				}
			
			}
		}
		//break;
	}
	
	cout << "IMPOSSIBLE" << endl;
}

int main() {
	int t;
	scanf("%d", &t); gets(polje[0]);
	for (int i = 1; i <= t; i++) {
		printf("Case #%d: ", i);
		//printf("%d\n", task());
		task();
	}
}

