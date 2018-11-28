#include <cstdio>
#include <algorithm>
#include <cstring>
#include <iostream>
#include <vector>
#include <set>
#include <string>
#include <map>

using namespace std;

int N, T, C, D;

string dict[55];
string temp;
bool bad[255][255];
string str;

char output[555];
int L;

inline void add(char c) {
	output[L++] = c;
	bool combine = false;
	if (L >= 2) {
		for(int i = 0 ; i < C ; i++) {
			if ((dict[i][0] == output[L - 1] && dict[i][1] == output[L - 2]) || (dict[i][0] == output[L - 2] && dict[i][1] == output[L - 1])) {
				output[L - 2] = dict[i][2];
				L--;
				combine = true;
				break;
			}
		}
	}
	if (!combine) {
		for(int i = 0 ; i < L - 1 ; i++) {
			if (bad[c][output[i]]) {
				L = 0;
				break;
			}
		}
	}	
}

int main() {
	cin >> T;
	for(int t = 1 ; t <= T ; t++) {
		L = 0;
		memset(bad, 0, sizeof(bad));
		cin >> C;
		for(int i = 0 ; i < C ; i++) {
			cin >> dict[i];
		}
		cin >> D;
		for(int i = 0 ; i < D ; i++) {
			cin >> temp;
			bad[temp[0]][temp[1]] = true;
			bad[temp[1]][temp[0]] = true;
		}
		cin >> N;
		cin >> str;
		for(int i = 0 ; i < N ; i++) {
			add(str[i]);
		}
		cout << "Case #" << t << ": ";
		if (L == 0) {
			cout << "[]" << endl;
		}	else {
			cout << "[" << output[0];
			for(int i = 1 ; i < L ; i++) {
				cout << ", " << output[i];
			}
			cout << "]" << endl;
		}
	}
	return 0;
}
