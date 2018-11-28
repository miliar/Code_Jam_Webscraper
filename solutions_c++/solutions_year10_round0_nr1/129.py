#include<cstdio>
using namespace std;
int main() {
	int T, e = 0;
	scanf("%d",&T);
	while(T--) {
		int n,k;
		scanf("%d%d",&n,&k);
		int nn = (1<<n);
		k%= nn;
		printf("Case #%d: ",++e);
		if(k+1 == nn) printf("ON\n");
		else printf("OFF\n");
	}
	return 0;
}