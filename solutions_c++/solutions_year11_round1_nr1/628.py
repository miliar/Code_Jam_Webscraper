#include <iostream>
using namespace std;
int gcd(int a,int b)
{
	if(b == 0) return a;
	return gcd(b,a%b);
}
int main()
{
	freopen("D:\\A-large.in","r",stdin);
	freopen("D:\\Alarge.out","w",stdout);
	int T,a,b,cnt=0;
	long long n;
	scanf("%d",&T);
	while(T--) {
		scanf("%lld %d %d",&n,&a,&b);
		int tmp = 100/gcd(a,100);
		if(tmp<=n){
			if((a!=0 && b==0) || (a!=100 && b==100))	printf("Case #%d: Broken\n",++cnt);
			else 	printf("Case #%d: Possible\n",++cnt);
		}
		else {
				printf("Case #%d: Broken\n",++cnt);
		}
	}
}