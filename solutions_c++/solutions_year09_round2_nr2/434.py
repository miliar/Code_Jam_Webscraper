#include<cstdio>
#include<cstdlib>
#include<string>
#include<cstring>
#include<algorithm>
#include<vector>
#include<set>
#include<map>

using namespace std;

int n;
char num[25];
multiset<char> buck;
multiset<char>::iterator it_buck;

void input() {
	//scanf("%d", &n);
	scanf("%s", num);
}

void solve(int cn) {
	//sprintf(num, "%d", n);
	int len = strlen(num);
	int done = 0;
	buck.clear();
	buck.insert(num[len - 1]);
	for (int i = len - 2; i >= 0; i--) {
		buck.insert(num[i]);
		it_buck = buck.upper_bound(num[i]);
		if (it_buck != buck.end()) {
			char sub = *it_buck;
			num[i] = sub;
			buck.erase(it_buck);
			for (int j = i + 1; j < len; j++) {
				num[j] = *buck.begin();
				buck.erase(buck.begin());
			}
			done = 1;
			break;
		}
	}
	if (!done) {
		it_buck = buck.upper_bound('0');
		num[0] = *it_buck;
		buck.erase(it_buck);
		num[1] = '0';
		for (int j = 2; j <= len; j++) {
			num[j] = *buck.begin();
			buck.erase(buck.begin());
		}
		num[len + 1] = '\0';
	}
	printf("Case #%d: %s\n", cn, num);
}

int main() {
	int T;
	scanf("%d", &T);
	for (int cn = 1; cn <= T; cn++) {
		input();
		solve(cn);
	}
	return 0;
}

