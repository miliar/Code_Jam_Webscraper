#include <iostream>
#include <cstdio>
#include <string>

using namespace std;
int c, d;
char a[100][5], b[100][5];
string s;
bool Combin()
{
	//return false;
	if (s.size() >= 2) {
		int i, j;
		for (j = s.size() - 2; j >= 0; --j)
			for (i = 0; i < c; ++i) {
				if ((s[j] == a[i][0] && s[j + 1] == a[i][1]) || (s[j] == a[i][1] && s[j + 1] == a[i][0])) {
					s[j]= a[i][2];
					s.erase(s.begin() + j + 1);
					return true;
				}
			}
	}
	return false;
}
bool Clear()
{
	if (s.size() > 1) {
		int i, j, k;
		for (j = s.size() - 1; j > 0; --j)
			for (i = j - 1; i >= 0; --i)
				for (k = 0; k < d; ++k) {
					//printf("%d %d %s\n", i, j, b[k]);
					if ((s[i] == b[k][0] && s[j] == b[k][1]) || (s[i] == b[k][1] && s[j] == b[k][0])) {
						//s.erase(s.begin() + i, s.begin() + j + 1);
						s.clear();
						return true;
					}
				}
	}
	return false;
}
int main()
{
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
	int T;
	cin >> T;
	for (int t = 0; t < T; ++t) {
		cin >> c;
		int i;
		for (i = 0; i < c; ++i) {
			cin >> a[i];
		}
		cin >> d;
		for (i = 0; i < d; ++i) {
			cin >> b[i];
		}
		s.clear();
		int n;
		cin >> n;
		char buf[200];
		cin >> buf;
		for (i = 0; i < n; ++i) {
			s += buf[i];
			bool flag = true;
			//while (flag) {
				flag = false;
				while (Combin()) flag = true;
				while (Clear()) flag = true;
			//}
		}
		printf("Case #%d: [", t + 1);
		for (i = 0; i < s.size(); ++i) {
			putchar(s[i]);
			if (i + 1 < s.size()) printf(", ");
		}
		printf("]\n");
		
	}
}
