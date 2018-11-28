#include <cstdio>
#include <cstring>

int L, D, N;
char s[6000][20], t[1000];
bool b[20][26];

bool check(char* ss) {
	for (int i=0;ss[i];i++) {
		if (!b[i][ss[i]-'a']) return 0;
	}
	return 1;
}

int main() {
	scanf("%d%d%d", &L, &D, &N);
	for (int i=0;i<D;i++) scanf("%s", s[i]);
	for (int j=0;j<N;j++) {
		scanf("%s", t);
		memset(b, 0, sizeof(b));
		int k=0;
		for (int i=0;t[i];) {
			if (t[i]=='(') {
				for (++i;t[i]!=')';i++) {
					b[k][t[i]-'a']=1;
				}
				k++; i++;
			}
			else {
				b[k++][t[i++]-'a']=1;
			}
		}
		int cnt=0;
		for (int i=0;i<D;i++) if (check(s[i])) cnt++;
		printf("Case #%d: %d\n", j+1, cnt);
	}
	return 0;
}
