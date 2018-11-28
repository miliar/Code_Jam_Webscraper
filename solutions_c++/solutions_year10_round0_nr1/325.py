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

i64 p2[60];

int main() {
	int i;
	bool flag;
	int N,K,kase=1,T;
	p2[0] = 1;
	for(i = 1; i <=40; i++) p2[i] = p2[i-1] * 2;
	scanf("%d",&T);
	while(T--) {
		scanf("%d %d",&N,&K);
		printf("Case #%d: ",kase++);
		flag = false;
		/*for(i = 1; ; i++) {
			if(p2[N] * i - 1 > K) break;
			if(p2[N] * i - 1 == K) { flag = true; break;}
		}*/
		if((K+1) % p2[N] == 0) flag = true;
		if(flag) printf("ON\n");
		else printf("OFF\n");
	}
	return 0;
}
