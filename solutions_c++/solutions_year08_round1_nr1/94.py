#include <iostream>
#include <algorithm>
using namespace std;

long long vector1[1000], vector2[1000];

int main() {
	int T;
	cin >> T;
	for (int i = 0; i < T; i++) {
		int n;
		cin >> n;
		for (int j = 0; j < n; j++) cin >> vector1[j];
		sort(vector1, vector1+n);
		for (int j = 0; j < n; j++) cin >> vector2[j];
		sort(vector2, vector2+n);
		long long minprod = 0;
		for (int j = 0; j < n; j++) minprod += vector1[j]*vector2[n-1-j];
		cout << "Case #" << i+1 << ": " << minprod << endl;
	}
}
