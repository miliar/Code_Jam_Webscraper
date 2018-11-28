#include <iostream>
#include <string>
#include <string.h>
#include <cstring>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <bitset>

using namespace std;

long long is_prime(long long x){
	if (x==1) return 0;
	for (long long i=2; i*i<=x; i++)
		if (x%i==0) return 0;
	return 1;
}

long long pr[1010000];
long long used[1010000];
long long gd[1010000];
vector <long long> OK;
long long d,k;
long long a[20];

long long modpow(long long a,long long pw,long long P){
	if (pw==0) return 1;
	if (pw==1) return a%P;
	if (pw%2==0){
		long long rs=modpow(a,pw/2,P);
		long long ret=(rs*rs)%P;
		return ret;
	} else
		return (a*modpow(a,pw-1,P))%P;
}

long long findA(long long p){
	long long x=a[2]-a[1];
	long long y=a[3]-a[2];
	if (x<0) x+=p;
	if (y<0) y+=p;
	x%=p, y%=p;

	long long x_inv=modpow(x,p-2,p);
	long long A=x_inv*y;
	A%=p;
	return A;
}

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	long long t;
	scanf("%I64d",&t);

	for (long long i=1; i<1010000; i++)
		pr[i]=is_prime(i);

	for (long long tt=1; tt<=t; tt++){
		OK.clear();
		printf("Case #%I64d: ",tt);
				
		scanf("%I64d%I64d",&d,&k);

		long long tn=1;
		for (long long i=1; i<=d; i++) tn*=10LL;
		for (long long i=1; i<=k; i++)
			scanf("%I64d",&a[i]);

		

		if (k==1){
			printf("I don't know.\n");
			continue;
		} else
			if (k==2){
				if (a[1]!=a[2]) printf("I don't know.\n"); else
					printf("%I64d\n",a[2]);
				continue;
			}

		for (long long i=2; i<tn; i++)
			if (pr[i]){
				if (i<=a[1]) continue;
				long long p=i;
				long long A=findA(i);

				long long S=A*a[1];
				S-=a[2];
				if (S<0) S+=p;
				S%=p;
				long long B=p-S;
				S=a[1];
				long long tr=1;
				for (long long l=1; l<k; l++){
					S=(A*S+B)%p;
					if (S!=a[l+1]){
						tr=0;
						break;
					}
				}
				if (tr){
					OK.push_back((A*S+B)%p);
				}
			}

			sort(OK.begin(),OK.end());
			if (OK.size()<1) printf("I don't know.\n"); else
				if (OK[0]!=OK[OK.size()-1]) printf("I don't know.\n"); else
				printf("%I64d\n",OK[0]);
	}

	return 0;
}