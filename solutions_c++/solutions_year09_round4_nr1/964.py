#include <iostream>
using namespace std;

const int SIZE = 100;
bool mark[SIZE];
int last[SIZE];

char line[SIZE];

int get_count(int k) {
	int result = 0;
	for (int i = 0; i < k; ++i) {
		int current = 0;
		for (int j = 0; j < k; ++j) {
			if (!mark[j] && last[j] <= i) {
				result += current;
				mark[j] = true;
				break;
			} else if (!mark[j])
				current++;
		}
	}
	return result;
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("a-large.out", "w", stdout);
	int N;
	cin >> N;
	for (int kk = 0; kk < N; ++kk) {
		memset(mark, 0, sizeof(bool) * SIZE);
		memset(last, 0, sizeof(int) * SIZE);
		int k;
		cin >> k;
		for (int i = 0; i < k; ++i) {
			memset(line, 0, sizeof(char) * SIZE);
			cin >> line;
			int max_right = 0;
			for (int j = 0; j < k; ++j) {
				if (line[j] == '1')
					max_right = j;
			}
			last[i] = max_right;
		}
		int rr = get_count(k);
		printf("Case #%d: %d\n", kk+1, rr);
		/*
		 for (int i = 0; i < k; ++i) {
		 cout << last[i] << endl;
		 }
		 */
	}
	return 0;
}
