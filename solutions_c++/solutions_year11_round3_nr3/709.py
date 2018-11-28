#include "iostream"
#include "algorithm"
#include "cstdio"
#include "cstring"
using namespace std;

int N;
long long L,H;
long long a[20000];

long long gcd(long long a, long long b){
	long long x = a>=b?a:b;
	long long y = a<b?a:b;
	while(y!=0){
		long long tmp=y;
		y=x%y;
		x=tmp;
	}
	return x;
}
int main(){
	freopen("C.out","w",stdout);
	int cs;
	cin>>cs;

	for(int css=1;css<=cs;css++){
		cin>>N;
		scanf("%lld %lld", &L, &H);
		for(int i=0;i<N;i++){
			scanf("%lld", &a[i]);
		}
		long long c = gcd(a[0],a[1]);
		for(int i=2;i<N;i++){
			c = gcd(c, a[i]);
		}
		long long ans = -1;
		bool yes = 0;
		for(long long i=L;i<=H;i++){
			bool ok = 1;
			for(int j=0;j<N;j++){
				if(a[j]>i){
					if(a[j]%i==0){
					}
					else{
						ok = 0;
						break;
					}
				}
				else{
					if(i%a[j]==0){
					}
					else{
						ok = 0;
						break;
					}
				}
			}
			if(ok==1){
				yes = 1;
				ans = i;
				break;
			}
		}
		if(yes==1) printf("Case #%d: %lld\n", css, ans);
		else printf("Case #%d: NO\n", css);
		
	}
	return 0;
}