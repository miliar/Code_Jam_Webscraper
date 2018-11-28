#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

vector<int> result;
int K;

void calc()
{
	result.clear();
	result.resize(K, 0);

	int pos = 0;
	for (int i=1; i<=K; ++i) {
		int num = i;
		while (1) {
			if (!result[pos]) {
				num--;
				if (num == 0) {
					result[pos] = i;
					break;
				}
			}
			pos++;
			if (pos >= K) pos-=K;
		}
	}
/*
	cout << K << endl;
	for (int i=0; i<K; ++i) {
		cout << result[i] << ' ';
	}
	cout << endl;
*/
}

int main(void)
{
	int i, j, a;

	int N;
	cin >> N;
	int n;
	for (i=1; i<=N; ++i) {
		cin >> K;

		calc();

		cout << "Case #" << i << ":";

		cin >> n;
		for (j=0; j<n; ++j) {
			cin >> a;
			cout << " " << result[a-1];
		}
		cout << endl;
	}

	return 0;
}
