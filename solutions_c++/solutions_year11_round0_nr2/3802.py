#include <cstdio>
#include <cstring>
#include <vector>
using namespace std;

#define MAX 27

int c,d;
char comb[MAX][MAX], opp[MAX], cnt[MAX];
char s[102];
int n;

void foo(char* p) {
	while(*p) *p++ -= 'A';
}
void out(char* curr, int l) {
	printf("[");
	for (int i = 0; i < l; ++i) {
		printf("%c", curr[i]+'A');
		if (i != l-1) printf(", ");
	}
	printf("]\n");
}

void solve() {
	char curr[500];
	memset(cnt, 0, sizeof(cnt));
	int l = 0;
	for (int i = 0; i < n; ++i) {
		//out(curr, l);
		char t = s[i];
		if (l && comb[curr[l-1]][t] ) {
			fprintf(stderr, "=>");
			--cnt[curr[l-1]];
			curr[l-1] = comb[curr[l-1]][t];
			++cnt[curr[l-1]];
			continue;
		}
		if ( cnt[opp[t]] ) {
			fprintf(stderr, "reset");
			l = 0;
			memset(cnt, 0, sizeof(cnt));
			continue;
		}
		curr[l++] = t;
		++cnt[t];
	}
	out(curr, l);
}

void input() {
	memset(comb, 0, sizeof(comb));
	memset(opp, 26, sizeof(opp));
	char buff[7];
	scanf("%d", &c);
	for(int i = 0; i < c; ++i) {
		scanf("%s", buff);
		foo(buff);
		//out(buff, strlen(buff));
		comb[buff[0]][buff[1]] = comb[buff[1]][buff[0]] = buff[2];
	}
	scanf("%d", &d);
	for(int i = 0; i < d; ++i) {
		scanf("%s", buff);
		foo(buff);
		//sout(buff, strlen(buff));
		opp[buff[0]] = buff[1];
		opp[buff[1]] = buff[0];
//		out(&opp['A'-'A'], 1);
	}
	scanf("%d%s", &n, s);
	foo(s);
}

int main() {
	int m;
	scanf("%d", &m);
	for(int i = 0; i < m; ++i) {
		input();
		printf("Case #%d: ", i+1);
		solve();
	}
}
