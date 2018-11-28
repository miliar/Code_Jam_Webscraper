#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<vector>
#include<string>
#include<algorithm>
#include<queue>
using namespace std;

#define min(a,b) (((a)<(b))?(a):(b))
#define max(a,b) (((a)>(b))?(a):(b))
#define rep(i,n) for(i=0;i<(n);i++)
#define MAX 105
#define i64 __int64

char s[1000], curString[1000], res[1000];
i64 cur;
int L;
i64 t;
bool flag;

void go(int dex) {
	if(dex == L) {
		t = (i64)sqrt(cur);
		if(t * t == cur) {
			flag = true;
			strcpy(res, curString);
		}
		return;
	}

	cur = (cur << 1);
	if(s[dex] == '?') {
		curString[dex] = '0';
		go(dex+1);
		if(flag) return;

		cur = cur | 1;
		curString[dex] = '1';
		go(dex+1);
		if(flag) return;
	}
	else {
		cur = cur | (s[dex] == '1');
		go(dex+1);
		if(flag) return;
	}
	cur >>= 1;

}

int main() {
	int T,kase=1;
	scanf(" %d",&T);
	while(T--) {
		printf("Case #%d: ",kase++);
		scanf(" %s",s);
		L = strlen(s);
		strcpy(curString, s);
		cur = 0;
		flag = false;
		go(0);
		printf("%s\n",res);
	}
	return 0;
}