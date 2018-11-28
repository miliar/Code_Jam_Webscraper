#include<stdio.h>
#include<memory.h>
#include<algorithm>

using namespace std;

long long num[110];
int t,n;

long long gcd(long long a,long long b){
    if(b==0)   return a;
    return gcd(b,a%b);
}
int main(){
	int ccount = 0;
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small-attempt0.txt","w",stdout);
    scanf("%d",&t);
	while(t--){
	    scanf("%d",&n);
	    for(int i=1;i<=n;i++)
	        scanf("%I64d",&num[i]);
	    sort(num+1,num+1+n);
	    long long mod = num[2] - num[1];
	    for(int i=3;i<=n;i++)
	        mod = gcd(mod, num[i] - num[i-1]);
	    long long test = num[1]%mod;
		if(test==0)
		   printf("Case #%d: %I64d\n",++ccount,0);
		else
		   printf("Case #%d: %I64d\n",++ccount,mod  - test); 
	}    
	return 0;
}
