#include <cstdio>
#include <cstring>

#define FOR(i,a,b) for(int i=a; i<(b); i++)

using namespace std;

char text[19+1] = "welcome to code jam";
int tab[505][20];
char line[505];
int L;

int licz(int pos, int len) {
	if(len == 0) return 1;
	if(pos == L) return 0;
	int &ret = tab[pos][len];
	if(ret != -1) return ret;
	ret = licz(pos+1, len);
	if(line[pos] == text[19-len]) ret += licz(pos+1, len-1);
	ret %= 10000;
	return ret;
}

int main() {
	int N;
	scanf("%d", &N);
	FOR(q,1,N+1) {
		scanf(" %[^\n]", line);
		L = strlen(line);
		FOR(l,0,L) FOR(s,0,20) tab[l][s] = -1;
		int ret = licz(0,19) % 10000;
		printf("Case #%d: %04d\n", q, ret);
	}
	return 0;
}