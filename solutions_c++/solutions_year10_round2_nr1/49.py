#include <cstdio>
#include <string>
#include <set>
using namespace std;

set<string> dirs;
int cnt;
char buff[1000000];

void add(string s) {
	//printf("add %s\n", s.c_str());
	if(s == "/" || s=="") return;
	if(dirs.find(s)!=dirs.end()) {
		return ;
	}
	cnt ++;
	dirs.insert(s);
	int i = s.size() - 1;
	while(i > 0 && s[i] != '/') {
		i--;
	}

	add(s.substr(0, i));

}

int main() {
	int tcase;
	scanf("%d", &tcase);
	for(int ttt=1; ttt<=tcase; ttt++) {
		int n, m;
		dirs.clear();
		cnt = 0;
		scanf("%d%d", &n, &m);
		for(int i=0; i<n; i++) {
			scanf("%s", buff);
			dirs.insert(string(buff));
		}
		for(int i=0; i<m; i++) {
			scanf("%s", buff);
			add(string(buff));
		}
		printf("Case #%d: %d\n", ttt, cnt);
	}
}
