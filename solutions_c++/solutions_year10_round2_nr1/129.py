#include <cstdio>
#include <cstring>
#include <string>
#include <set>
using namespace std;

const int MAXL = 1024 + 1;

int N, M, cnt;
set <string> dict;

inline void insert(set <string> & dict, string str) {
	for (int i = 1; i < (int)str.size(); i++) {
		if (str[i] != '/') continue;
		string tmpstr = str.substr(0, i);
		if (dict.count(tmpstr)) continue;
		dict.insert(tmpstr);
		cnt++;
	}
	if (dict.count(str)) return ;
	dict.insert(str);
	cnt++;
}

int main() {
	int task;
	scanf("%d", &task);
	for (int oo = 0; oo < task; oo++) {
		scanf("%d%d", &N, &M);
		dict.clear();
		for (int i = 0; i < N; i++) {
			char line[MAXL];
			scanf("%s", line);
			insert(dict, line);
		}
		cnt = 0;
		for (int i = 0; i < M; i++) {
			char line[MAXL];
			scanf("%s", line);
			insert(dict, line);
		}
		printf("Case #%d: %d\n", oo + 1, cnt);
	}
	return 0;
}
