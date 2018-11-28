#include <iostream>
#include <queue>

using namespace std;

int n,k;

int  solve() {
	if(!k)return 0;
	long long tmp = (1LL)<<n;
	long long k2 = k;
	k2 %= tmp;
	return k2 + 1 == tmp;
}

int main() {
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int T,cas = 1;
	scanf("%d",&T);
	while(T--) {
		scanf("%d%d",&n,&k);
		printf("Case #%d: ",cas++);
		if(solve())puts("ON");
		else puts("OFF");
	}	
	return 0;
}
