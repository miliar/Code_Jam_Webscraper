#include <cstdio>
#include <string>

using namespace std;

bool b[2000001];

string str(int num) {
	char s[256];
	sprintf(s, "%d", num);
	return string(s);
}

int int_s(string s) {
	return atoi(s.c_str());
}

string move_str(string s, int k) {
	return s.substr(s.length() - k, k) + s.substr(0, s.length() - k);
}

int main() {
	freopen("C-large.in", "r", stdin);
	//freopen("C-large.out", "w", stdout);

	int T, A, B;
	int count, t, ct, m;
	string s;
	scanf("%d", &T);
	for (int case_t = 1; case_t <= T; ++case_t) {
		scanf("%d%d", &A, &B);
		count = 0;
		memset(&b[A], false, sizeof(bool)*(B-A+1));
		for (int j = A; j <= B; ++j) {
			if (b[j])
				continue;
			s = str(j);
			m = s.length();
			ct = 0;
			for (int k=1; k<m; ++k) {
				t = int_s(move_str(s, k));
				if (t > j && t <= B && !b[t]) {
					b[t] = true;
					count += ++ct;
				}
			}
		}
		printf("Case #%d: %d\n", case_t, count);
	}
}