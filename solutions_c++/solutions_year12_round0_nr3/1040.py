#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <string>

using namespace std;

int readInt() {int N = -1; cin >> N; return N;}

vector <int> len;
vector <int> ten;

#define BUG(x) cout << #x << " = " << x << endl

void initialize() {
	ten.push_back(1);
	for (int i = 0; i < 7; ++i) ten.push_back(ten.back() * 10);
	len.resize(2000000 + 1, 0);
	for (int i = 0; i <= 9; ++i) len[i] = 1;
	for (int i = 10; i < len.size(); ++i) len[i] = len[i / 10] + 1;
}

bool isMirror(int n, int shift, int A, int B, set <int>& ofM) {
	int length = len[n];
	int m = (n % ten[shift]) * ten[length - shift] + (n / ten[shift]);
	if (m <= B && m > n && ofM.find(m) == ofM.end()) {
		ofM.insert(m);
		return true;
	}
	else return false;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	initialize();
	int nTestCases = readInt();
	for (int testCase = 1; testCase <= nTestCases; ++testCase) {
		int A = readInt(), B = readInt();
		int count = 0;
		for (int n = A; n < B; ++n) {
			set <int> ofM;
			for (int shift = 1; shift <= len[n] - 1; ++shift)
				if (isMirror(n, shift, A, B, ofM))
					++count;
		}
		printf("Case #%d: %d\n", testCase, count);
	}
}
