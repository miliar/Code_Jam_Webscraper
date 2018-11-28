#include "iostream"
#include "algorithm"
#include "cstdio"
#include "cstring"
using namespace std;

long long gcd(long long a, long long b)
{
	if(b == 0)
		return a;
	return gcd(b, a % b);
}

int main(){
	freopen("A.out","w",stdout);
	int css;
	long long n;
	int pd,pg;
	cin>>css;
	for(int cs=1;cs<=css;cs++){
		scanf("%lld", &n);
		cin>>pd>>pg;
		if(pg==0 && pd!=0){
			printf("Case #%d: Broken\n", cs);
			continue;
		}
		if(pg==100&&pd!=100){
			printf("Case #%d: Broken\n", cs);
			continue;
		}
		else{
			long long cd = 100/gcd(pd,100);
			if(n>=cd){
				printf("Case #%d: Possible\n", cs);
			}
			else
			{
				printf("Case #%d: Broken\n", cs);
			}
		}
	}

	return 0;
}