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
#define rab(i,a,b) for(i=(a);i<=(b);i++)
#define MAXN 1005
#define i64 __int64

int g[MAXN];
int en[MAXN];
i64 earn[MAXN];

int main() {
	int T,kase=1;
	int R,K,N;
	int i,j;
	i64 ct;
	int pos;

	scanf("%d",&T);
	while(T--) {
		printf("Case #%d: ",kase++);
		scanf("%d %d %d",&R,&K,&N);
		rep(i,N) scanf(" %d",&g[i+1]);
		rab(i,1,N) {
			ct = g[i];
			j = i + 1;
			while(1) {
				if(j > N) j = 1;
				if(j == i) break;
				if(ct + g[j] > K) break;
				ct += g[j++];
			}
			j--;
			if(j < 1) j = N;
			en[i] = j;
			earn[i] = ct;
		}

		ct = 0;
		pos = 1;
		rep(i,R) {
			ct += earn[pos];
			pos = en[pos] + 1;
			if(pos > N) pos = 1;
		}
		printf("%I64d\n",ct);
	}
	return 0;
}