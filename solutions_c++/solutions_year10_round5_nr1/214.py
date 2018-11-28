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
#define MAXP 1001000
#define MAXPR 100000
#define MAXK 10

char p[MAXP+10];
int primes[MAXPR+10],ct;
int s[MAXK+10];

void sieve() {
	int i,j;
	for(i=2;i*i<=MAXP;i++) if(!p[i]) for(j=i*i;j<=MAXP;j+=i) p[j] = 1;
	ct = 0;
	for(i=2;i<=MAXP;i++) if(!p[i]) primes[ct++] = i;
}

int get_mod(int a, int b) {
	int res = a % b;
	if(res < 0) res += b;
	return res;
}

int main() {
	int T,kase=1;
	int i,j,k;
	int p10[12];
	int mx;
	bool flag;
	int t;
	bool f_flag;
	int res;
	int D,K;
	vector<int> ans;

	p10[0] = 1;
	for(i=1;i<=10;i++) p10[i] = p10[i-1] * 10;
	sieve();

	scanf("%d",&T);
	
	while(T--) {
		printf("Case #%d: ",kase++);
		scanf(" %d %d",&D, &K);
		mx = -1;
		rep(i,K) { scanf(" %d",&s[i]); mx = max(mx,s[i]); }
		if(K == 1) {printf("I don't know.\n"); continue;}
		f_flag = true;
		ans.clear();
		rep(i,ct) {
			if(primes[i] > p10[D]) break;
			if(primes[i] <= mx) continue;
			rep(j,primes[i]) {
				flag = true;
				for(k=2;k<K;k++) {
					t = get_mod(s[k-1] + j * (s[k-1] - s[k-2]), primes[i]);
					if(t != s[k]) {
						flag = false;
						break;
					}
				}
				if(flag) {
					res = get_mod(s[K-1] + j * (s[K-1] - s[K-2]), primes[i]);
					ans.push_back(res);
					//res %= primes[i];
					//f_flag = true;
					//goto label;
				}
			}
		}
		if(ans.size() == 0) f_flag = false;
		rep(i,ans.size()) {
			if(ans[i] != ans[0]) f_flag = false;
		}
		if(f_flag) printf("%d\n",res);
		else printf("I don't know.\n");
	}
	return 0;
}