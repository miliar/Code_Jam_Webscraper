#include <iostream>

using namespace std;

int main() {
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int t;
	scanf("%d",&t);
	for (int test=1;test<=t;test++) {
		int n,k;
		scanf("%d %d",&n,&k);
		printf("Case #%d: ",test);
		if (k%(1<<n)==(1<<n)-1) printf("ON\n");
		else printf("OFF\n");
	}
    return 0;
}
