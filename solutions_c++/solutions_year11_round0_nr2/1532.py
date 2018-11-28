#include <cstdio>
#include <cstdlib>

#include <algorithm>

using namespace std;

int n, combine[26][26], clear[26][26];
char buf[128];

void input() {
	memset(combine, -1, sizeof(combine));
	memset(clear, -1, sizeof(clear));

	scanf("%d", &n);
	for(int i = 0;i < n;i ++) {
		scanf("%s", buf);
		combine[buf[0]-'A'][buf[1]-'A'] = buf[2] - 'A';
		combine[buf[1]-'A'][buf[0]-'A'] = buf[2] - 'A';
	}

	scanf("%d", &n);
	for(int i = 0;i < n;i ++) {
		scanf("%s", buf);
		clear[buf[0]-'A'][buf[1]-'A'] = 1;
		clear[buf[1]-'A'][buf[0]-'A'] = 1;
	}
	
	scanf("%d", &n);
	scanf("%s", buf);
}

void solve() {
	int nn = 1;
	for(int i = 1;i < n;i ++) {
		if(nn == 0) {
			buf[nn] = buf[i];
			++ nn;
		}
		else if(combine[buf[i]-'A'][buf[nn-1]-'A'] != -1) {
			buf[nn-1] = combine[buf[i]-'A'][buf[nn-1]-'A'] + 'A';
		}
		else {
			for(int j = 0;j < nn;j ++) if(clear[buf[j]-'A'][buf[i]-'A'] == 1) nn = 0;
			if(nn != 0) {
				buf[nn] = buf[i];
				++ nn;
			}
		}
	}
	printf("[");
	for(int i = 0;i < nn;i ++) {
		if(i != 0) printf(", ");
		printf("%c", buf[i]);
	}
	printf("]\n");
}

int main() {
	freopen("B-large.in", "r", stdin);
	//freopen("B-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for(int cas = 1;cas <= T;cas ++) {
		input();
		printf("Case #%d: ", cas);
		solve();
	}
	return 0;
}