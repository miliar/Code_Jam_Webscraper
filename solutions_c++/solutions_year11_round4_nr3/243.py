#include<cstdio>
#include<vector>
#include<algorithm>
#include<set>
#include<string>
#include<map>
#include<iostream>
using namespace std;

int tc;

long long n;
int a[100050];
int p[1000005];

int isp (long long p) {
	if (p==2) return 1;
	if (p%2==0) return 0;
	for (long long i=3; i*i<=p; i+=2)
		if (p%i==0) return 0;
	return 1;
}

int main() {
    freopen("c.in","r",stdin);
    freopen("c.out","w",stdout);
    scanf("%d",&tc);
    for (int i=2; i<=1000000; i++)
    	if (isp(i)==1) p[i]=1;
    	else p[i]=0;
	
    for (int T=1; T<=tc; T++) {
		scanf("%lld",&n);
		long long ti;
		int ret=0;
		for (long long i=2; i*i<=n; i++) 
			if (p[i]==1) {
				ti=i;
				while (ti<=n) {
					ti*=i; ret++;
				}
				if (ti==n) ret--;
				ret--;
				//printf("%lld %d\n",ti,ret);
			}
		if (n>1) ret++;
		printf("Case #%d: %d\n",T,ret);
				
	}
}
