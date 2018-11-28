#include <iostream>
#include <cstring>
using namespace std;

char s[1001];
char s2[1001];
int perm[5];

int recurse(int k, int p, int len) {
	if (p < k) {
		int best = len;
		for (int i = 0; i < k; i++) {
			bool allowed = true;
			for (int j = 0; j < p; j++) if (perm[j] == i) allowed = false;
			if (!allowed) continue;
			perm[p] = i;
			int b = recurse(k, p+1, len);
			if (b < best) best = b;
		}
		return best;
	}
	
	int ans = len;
	for (int i = 0; i < len; i += k)
		for (int j = 0; j < k; j++) {
			s2[i+j] = s[i+perm[j]];
			if (i+j > 0 && s2[i+j] == s2[i+j-1]) ans--;
		}
	return ans;
}

int main() {
	int N;
	cin >> N;
	for (int i = 0; i < N; i++) {
		int k;
		cin >> k >> s;
		cout << "Case #" << i+1 << ": " << recurse(k, 0, strlen(s)) << endl;
	}
}
