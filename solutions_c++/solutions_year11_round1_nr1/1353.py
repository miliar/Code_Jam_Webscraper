#include <cstdio>
#include <algorithm>
using namespace std;
int n, ret, loc;
char s[2001];

void dfs(int dep) {
	if(s[loc] == '#') return;
	ret = max(ret, dep + 1);
	++loc;
	dfs(dep + 1);
	++loc;
	dfs(dep + 1);
}

int main() {
	scanf("%d\n", &n);
	while(n--) {
		loc = ret = 0;
		gets(s);
		dfs(0);
		printf("%d\n", ret);
	}
	return 0;
}