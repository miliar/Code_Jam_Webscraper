#include <cstdio>
#include <cassert>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#define REP(i,n) for(int i = 0;i<n;i++)
#define FOREACH(it,u) for(__typeof(u.begin()) it = u.begin();it!=u.end();it++)
#define PB push_back
#define st first
#define nd second
#define PI pair<int,int>
#define debug if(0)
typedef long long LL;
using namespace std;

const int MAXN = 1000;
LL t[MAXN+10];
int pos[MAXN+10];
int mark[MAXN+10];
int krok[MAXN+10];

void solve() {
	LL R, k, N;
	scanf("%lld %lld %lld", &R, &k, &N);
	REP(i,N) {
		scanf("%lld", &t[i]);
		pos[i]=mark[i]=krok[i]=-1;
	}
	LL sum=0;
	int p=0;
	int il=0;
	while(R>0) {
		pos[p]=sum;
		krok[p]=il;
		LL cur=0;
		while(mark[p]!=il) {
			if(cur+t[p]>k) break;
			mark[p]=il;
			int next=(p+1)%N;
			cur+=t[p];
			p=next;
		}
		//printf("cur=%lld\n", cur);
		sum+=cur;
		il++;
		R--;
	}
	printf("%lld\n", sum);
}

int main() {
	int z;
	scanf("%d", &z);
	REP(i,z) {
		printf("Case #%d: ", i+1);
		solve();
	}
	return 0;
}

