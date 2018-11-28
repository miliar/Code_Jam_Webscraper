#include<cstdio>
#include<cstring>
int set[20][30];
char alien[5100][20], ipt[500];

inline int count(int D, int L) {
	int ret = 0;
	for(int i=0; i<D; i++) {
		int found = 1;
		for(int k=0; k<L; k++) {
			if ( !set[k][alien[i][k]-'a'] ) {
				found = 0;
				break;
			}
		}
		if ( found ) ret++;
	}
	return ret;
}
int main() {
	int L,D,N;
	while(scanf("%d %d %d", &L, &D, &N) != EOF) {
		for(int i=0; i<D; i++) scanf("%s", alien[i]);
		for(int TC=1; TC<=N; TC++) {
                     memset(set, 0, sizeof(set));
			scanf("%s", ipt);
			int len = strlen(ipt), idx = 0, open = 0;
			for(int i=0; i<len; i++) {
				if ( ipt[i] == '(' ) open = 1;
				else if ( ipt[i] == ')' ) open = 0, idx++;
				else if ( open && 'a' <= ipt[i] && ipt[i] <= 'z' ) {
					set[idx][ipt[i]-'a'] = 1;
				} else if ( !open && 'a' <= ipt[i] && ipt[i] <= 'z' ) {
					set[idx++][ipt[i]-'a'] = 1;
				}
			}
			printf("Case #%d: %d\n", TC, count(D, L));
		}
	}
	return 0;
}
