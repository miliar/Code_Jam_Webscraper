#include<stdio.h>
#include<string.h>
#include<assert.h>
#include<ctype.h>

#define MAXD 5000
#define MAXL 15
#define rep(i,n) for(i=0;i<(n);i++)

int L;
int D;
int N;
char w[MAXD+2][MAXL+2];
char pattern[500];
bool flag[MAXL+2][30];

int solve() {
	int i,j,pos,len;
	memset(flag,0,sizeof(flag));
	len = strlen(pattern);
	pos = 0;
	rep(i,len) {
		if(isalpha(pattern[i])) {
			flag[pos][pattern[i]-'a'] = 1;
			pos++;
		}
		else {
			assert(pattern[i] == '(');
			for(j=i+1;j<len;j++) {
				if(pattern[j] == ')') break;
				flag[pos][pattern[j]-'a'] = 1;
			}
			pos++;
			i = j;
		}
	}

	bool f;
	int res = 0;
	rep(i,D) {
		f = 1;
		rep(j,L) {
			if(flag[j][w[i][j]-'a'] == 0) {f = 0; break;}
		}
		if(f) res++;
	}
	return res;
}

int main() {
	int i;
	int T,res;
	scanf(" %d %d %d",&L,&D,&N);
	rep(i,D) scanf( "%s",w[i]);
	for(T=1;T<=N;T++) {
		scanf(" %s",pattern);
		res = solve();
		printf("Case #%d: %d\n",T,res);
	}
	return 0;
}