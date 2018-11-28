#include<stdio.h>
#include<algorithm>
using namespace std;

char cov[32*32];
char &getEle(char a, char b) {
	return cov[(int)(a-'A')<<5|(b-'A')];
}
int oppo[26];
void solve() {
	memset(cov, 0, sizeof(cov));
	memset(oppo, 0, sizeof(oppo));
	int C;
	scanf("%d", &C);
	for(int i=0;i<C;i++) {
		char item[4];
		scanf("%s", item);
		getEle(item[0], item[1])=item[2];
		getEle(item[1], item[0])=item[2];
	}
	int D;
	scanf("%d", &D);
	for(int i=0;i<D;i++) {
		char item[4];
		scanf("%s", item);
		oppo[item[0]-'A']|=1<<(item[1]-'A');
		oppo[item[1]-'A']|=1<<(item[0]-'A');
	}
	int N, p=0, op[128]={0};
	char str[128]={'Z'+1};
	scanf("%d", &N);
	scanf("%s", str+1);
	for(int i=1;i<=N;i++) {
		str[++p]=str[i];
		char c=getEle(str[p], str[p-1]);
		if(c!=0) str[--p]=c;
		if(op[p-1]&(1<<(str[p]-'A'))) {
			p=0;
		} else {
			op[p]=op[p-1]|oppo[str[p]-'A'];
		}
	}
	putchar('[');
	for(int i=1;i<=p;i++) {
		putchar(str[i]);
		if(i!=p) {
			putchar(',');
			putchar(' ');
		}
	}
	putchar(']');
	putchar('\n');
}

int main() {
	int T;
	scanf("%d", &T);
	for(int cas=1;cas<=T;cas++) {
		printf("Case #%d: ", cas);
		solve();
	}
}