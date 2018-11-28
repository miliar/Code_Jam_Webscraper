#include <stdio.h>
#include <string.h>
#include <assert.h>

const char *s = "welcome to code jam"; // 19 chars
int memo[501][21], N;
char t[1000];

int rec(int idx, int pos){
	int &ret = memo[idx][pos];
	if (ret!=-1) return ret; else ret = 0;
	if (pos >= 19) return ret = 1;
	if (!t[idx]) return ret = 0;
	for (int i=idx; t[i]; i++){
		if (t[i]==s[pos]){
			ret = (ret + rec(i+1,pos+1)) % 10000;
		}
	}
	return ret;
}

int main(){
	scanf("%d\n",&N);
	for (int i=0; i<N; i++){
		gets(t);
		memset(memo,-1,sizeof(memo));
		printf("Case #%d: %04d\n",i+1,rec(0,0));
	}
}
