#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cassert>
#include<string>
#include<algorithm>
#include<fstream>
#include<sstream>
#include<set>
#include<map>
#include<vector>
#include<queue>
#include<deque>
#include<complex>
#include<numeric>
using namespace std;

const int MaxN = 1000002;
int P[MaxN];

int check(int x, int y) { // x < y
	if(y % x == 0) return true;
	for(int k=1;k*x<y;++k)
		if(y-k*x < x && x < P[y-k*x]) return true;
	return false;
}

int init() {
	P[1] = 2;
	for(int i=2;i<MaxN;++i) {
		P[i]=P[i-1]-(i-1)+i;
		if(!check(i, P[i])) ++P[i];
	}
}
#define LL long long
int no;
int run() {
	LL res=0;
	printf("Case #%d: ",++no);
	int a1,a2,b1,b2;
	scanf("%d %d %d %d",&a1,&a2,&b1,&b2);
	for(int a=a1;a<=a2;++a)
		if(b2 > a) res += max(0, b2 - max(P[a], b1) + 1);
	for(int b=b1;b<=b2;++b)
		if(a2 > b) res += max(0, a2 - max(P[b], a1) + 1);
	printf("%lld\n", res);
}

int main() {
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
	init();
	int test; scanf("%d", &test);
	while(test--)run();
}
