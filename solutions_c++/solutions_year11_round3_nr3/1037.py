#include<cstdio>
#include<vector>

using namespace std;

long long _gcd(long long a,long long b) {
	if(b==0)
		return a;
	return _gcd(b,a%b);
}

int main() {
	int T;
	scanf("%d",&T);
	for(int caso=1;caso<=T;caso++) {
		int n;
		long long l,h;
		scanf("%d %lli %lli",&n,&l,&h);
		long long A[n];
		for(int i=0;i<n;i++)
			scanf("%lli",&A[i]);
	/*	long long gcd=0;
		for(int i=0;i<n;i++)
			gcd=_gcd(gcd,A[i]);*/
		long long rpta=-1;
		for(int i=l; i<=h;i++) {
			bool vale=1;
			for(int j=0;j<n;j++) {
				if(!(A[j]%i==0LL || i%A[j]==0LL || A[j]==1LL)) {
					vale=0;
					break;
				}
			}
			if(vale) {
				rpta=i;
				break;
			}
		}
		printf("Case #%d: ",caso);
		if(rpta==-1)
			printf("NO\n");
		else
			printf("%lli\n",rpta);
	}
}
