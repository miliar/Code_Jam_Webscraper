#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

struct JOB {
	int button;
	int num;
};

#define A(x) ((x) - 'A')

int main() {
	int T;
	cin >> T;

	for (int test = 0; test < T; test ++){
		int C, D, N;
		char combine[32][32] = {0};
		char opposed[32][32] = {0};
		string input;

		cin >> C;
		for (int i = 0; i < C; i ++) {
			string str;
			cin >> str;
			combine[A(str[0])][A(str[1])] = A(str[2]);
			combine[A(str[1])][A(str[0])] = A(str[2]);
		}

		cin >> D;
		for (int i = 0; i < D; i ++) {
			string str;
			cin >> str;
			opposed[A(str[0])][A(str[1])] = 1;
			opposed[A(str[1])][A(str[0])] = 1;
		}

		cin >> N;
		cin >> input;

		// process
		char result[1024] = {0};

		char count[32] = {0}; // base elementÇÃèoåªêî

		int now = 0;
		int cnt = 0;
		for (; cnt < N; cnt ++) {
			result[now] = A(input[cnt]);
			count[result[now]] ++;
			now ++;
			// combine?
			if (now >= 2 && combine[result[now-1]][result[now-2]] != 0) {
				count[result[now-1]] --;
				count[result[now-2]] --;
				result[now - 2] = combine[result[now-1]][result[now-2]];
				now --;
			} else { // invoke
				for (int i = 0; i < 32; i ++) {
					for (int j = 0; j < 32; j ++) {
						if (count[i] > 0 && count[j] > 0 && opposed[i][j] == 1) {
							// clear!
							now = 0;
							for (int k = 0; k < 32; k ++)
								count[k] = 0;
						}
					}
				}
			}
		}

		cout << "Case #" << test + 1 << ": [";
		for (int i = 0; i < now; i ++) {
			char ch = result[i] + 'A';
			cout << ch;
			if (i != now - 1)
				cout << ", ";
		}
		cout << "]" << endl;
	}

	return 0;
}