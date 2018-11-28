#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int N;

int len[40];

int main () {
	int i, j, k;
	int T, cse=0;
	cin >> T;
	char c;
	while (T--) {
		cin >> N;
		for (i=0; i<N; i++) {
			len[i] = 0;
			for (j=0; j<N; j++) {
				cin >> c;
				if (c=='1') len[i]=j+1;
			}
		}
		int cnt = 0;
		for (i=0; i<N; i++) {
			for (j=i; j<N; j++) {
				if (len[j] <= i+1) {
					if (j != i) {
						for (k=j; k>i; k--) {
							swap(len[k], len[k-1]);
							cnt++;
						}
					}
					break;
				}
			}
		}
		cout << "Case #" << ++cse << ": " << cnt << endl;
	}
	return 0;
}
