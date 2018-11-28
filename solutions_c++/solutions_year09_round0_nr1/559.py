#include<iostream>
using namespace std;

int N, L;

char S[100000];

int msk[100];

char pat[6000][30];

struct node {
	char key;
	int flag, nxt[26];
	inline int init(char _key=0, int _flag=0){
		key=_key;flag=_flag;memset(nxt,-1,sizeof(nxt));
	} 
}lt[6000 * 30];
int tot;

int Ins(const char *S) {
	int p = 0;
	for(int i=0;i<L;++i) {
		if(lt[p].nxt[S[i]-'a'] < 0)
			lt[lt[p].nxt[S[i]-'a']=tot++].init(S[i]);
		p = lt[p].nxt[S[i]-'a'];
	}
	lt[p].flag = 1;
}

int init() {
	tot = 0;
	lt[tot++].init();
	for(int i=0;i<N;++i) {
		scanf("%s", pat[i]);
		Ins(pat[i]);
	}
}

int que[2][6000 * 30], sz[2], now;
int mark[6000 * 30];

int run() {
	scanf("%s", S);
	int n = strlen(S), p = 0;
	for(int i=0;i<L;++i) {
		int &mk = msk[i];
		mk = 0;
		if(S[p] != '(') {
			mk = 1<<(S[p++]-'a');
		} else {
			int q = p;
			for(;S[q]!=')';++q);
			for(int j=p+1;j<q;++j)
				mk |= 1<<(S[j]-'a');
			p = q+1;
		}
	}
	
	memset(sz,0,sizeof(sz));
	now = 0;
	que[now][sz[now] ++ ] = 0;
	for(int i=0;i<L;++i) {
		sz[now^1] = 0;
		for(int j=0;j<sz[now];++j) {
			int p = que[now][j];
			int mk = msk[i];
			while(mk) {
				int c = __builtin_ctz(mk);
				if(lt[p].nxt[c] > -1) {
					que[now^1][sz[now^1]++] = lt[p].nxt[c];
				}
				mk ^= (mk&-mk);
			}
		}
		now ^= 1;
	}
	printf("%d\n", sz[now]);
}

int main() {
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	
	int test;
	scanf("%d %d %d", &L, &N, &test);
	
	init();
	
	for(int no=1;no<=test;++no) {
		printf("Case #%d: ",no);
		run();
	}
}
