#include <iostream>
#include <cstdio>
#include <cmath>

#define MAX_N 200

using namespace std;

int main(void) {
	int t, n;
	int points[MAX_N + 1];
	double res[MAX_N + 1];
	
	cin >> t;
	for(int numCase = 1; numCase <= t; numCase++) {
		cin >> n;
		
		int sum = 0;
		for(int i = 0; i < n; i++) {
			cin >> points[i];
			sum += points[i];
			res[i] = 0;
		}
		
		double tot = 0;
		int mean = 2.0 * sum / n, positives = 0;
		for(int i = 0; i < n; i++) {
			res[i] += 100.0 * (mean - points[i]) / sum;
			
			if (res[i] < 0) {
				res[i] = 0;
			} else {
				positives++;
			}

			tot += res[i];
		}
		
		if (tot > 100.0) {
			for(int i = 0; i < n; i++) {
				if(res[i] > 0) {
					res[i] -= (tot - 100.0) / positives;
				}
			}
		} else {
			for(int i = 0; i < n; i++) {
				res[i] += (100.0 - tot) / n;
			}
		}
		
		printf("Case #%d:", numCase);
		for(int i = 0; i < n; i++) {
			printf(" %.5lf", res[i]);
		}
		printf("\n");
	}
}
