#include <string>
#include <iostream>
#include <cstdio>
using namespace std;

const string base = "QWERASDF";
int cnt[255], err[255][255], up[255][255];
int ans[200];

bool tst(char c)
{
	for (int i = 0; i < base.size(); i ++)
		if (cnt[base[i]] && err[base[i]][c]) return true;
	return false;
}

void solve(int caseID)
{
	int C, D, N;
	string s;
	
	cin >> C;
	memset(up, 0, sizeof(up));
	while (C --) {
		cin >> s;
		up[s[0]][s[1]] = up[s[1]][s[0]] = s[2];
	}

	cin >> D;
	memset(err, 0, sizeof(err));
	while (D --) {
		cin >> s;
		err[s[1]][s[0]] = err[s[0]][s[1]] = true;
	}

	cin >> N;
	char c;
	int len = -1;
	memset(cnt, 0, sizeof(cnt));
	while (N --) {
		cin >> c;
		if (len >= 0 && up[ans[len]][c] != 0) {
			cnt[ans[len]] --;
			ans[len] = up[ans[len]][c];
			cnt[ans[len]] ++;
		}
		else if (len >= 0 && tst(c)){
			len = -1;
			memset(cnt, 0, sizeof(cnt));
		}
		else {
			ans[++ len] = c;
			cnt[ans[len]] ++;
		}
	}

	printf("Case #%d: [", caseID);
	for (int i = 0; i <= len; i ++) {
		printf("%c", ans[i]);
		if (i < len) printf(", ");
	}
	printf("]\n");
}

int main()
{
	int T;
	cin >> T;
	for (int i = 1; i <= T; i ++)
		solve(i);
}
