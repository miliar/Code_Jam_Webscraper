#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <utility>
#include <cmath>
#include <cstdio>


using namespace std;

inline int length (int i)
{
	int k = 0;
	while (i) {
		k++;
		i /= 10;
	}
	
	return k;
};

int main (void)
{
	int x[] = {0, 1, 10, 100, 1000, 10000, 100000, 1000000, 
				10000000, 100000000, 1000000000};
	int T, low, up;
	int l, k, sum;

	cin >> T;
	for (int i = 1; i <= T; ++i) {
		cin >> low >> up;
		sum = 0;
		for (int j = low; j <= up; ++j) {
			l = length (j);
			k = j;
			for (int m = 0; m < l - 1; ++m) {
				k = x[l] * (k % 10) + k / 10;
				if (k == j) continue;
				if (k >= low && k <= up) {
					sum++;
				}
			}
		}
		sum /= 2;
		cout << "Case #" << i << ": " << sum << endl;
	
	}
	

	return 0;

}