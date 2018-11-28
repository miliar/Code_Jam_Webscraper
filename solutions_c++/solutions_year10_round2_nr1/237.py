#include <iostream>
#include <set>
using namespace std;

set<string> exist;

int main() {
	freopen("a-large.in", "r", stdin);
	freopen("a-large.out", "w", stdout);
	int tt, ttt, cnt, i, N, M, found;
	char s[150];
    scanf("%d", &tt);
    for(ttt = 1; ttt <= tt; ttt++) {
		scanf("%d%d", &N, &M);
		cnt = 0;
		exist.clear();
		for(i = 0; i < N; i++) {
			scanf("%s", s);
			string str(s);
			exist.insert(str);
		}
		for(i = 0; i < M; i++) {
			scanf("%s", s);
			string str(s);
			str = str + "/";
			found = -1;
			for(;;) {
				found = str.find_first_of('/', found + 1);
				if (found == string::npos) break;
				if (found == 0) continue;
				string s1 = str.substr(0, found);
				if (exist.find(s1) == exist.end()) {
					exist.insert(s1);
					cnt++;
				}
			}
		}
		printf("Case #%d: %d\n", ttt, cnt);
	}
    return 0;
}
