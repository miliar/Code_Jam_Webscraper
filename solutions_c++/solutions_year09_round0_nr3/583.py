#include<iostream>
using namespace std;

const char Pat[] = "welcome to code jam";
const int K = strlen(Pat);

char S[10000];
int L;

inline int inc(int&a, int b) {
	a+=b; a%=10000;
}

int f[10000][50];

int run() {
	gets(S+1);
	L=strlen(S+1);
	f[0][0] = 1;
	for(int i=1;i<=L;++i)
		for(int j=0;j<=K;++j) {
			f[i][j] = f[i-1][j];
			if(j && Pat[j-1] == S[i])
				inc(f[i][j], f[i-1][j-1]);
		}
	printf("%04d\n", f[L][K]);
}

int main() {
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	
	int test; sscanf(gets(S),"%d", &test);
	for(int no=1;no<=test;++no) {
		printf("Case #%d: ", no);
		run();
	}
}
