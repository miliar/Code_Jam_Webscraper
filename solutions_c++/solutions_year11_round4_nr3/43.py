#include<stdio.h>
bool np[1000100];
int pr[1000000],pc;
inline void pre(){
    long long i,j;
    for(i=2;i<=1000000;i++)if(!np[i]){
	pr[pc++]=i;
	for(j=i*i;j<=1000000;j+=i)np[j]=1;
    }
}
inline int solve(long long n){
    int i,ans=0;
    for(i=0;i<pc&&pr[i]*pr[i]<=n;i++){
	long long k=pr[i]*pr[i];
	while(k<=n){
	    k*=pr[i];
	    ans++;
	}
    }
    if(n!=1)ans++;
    return ans;
}
int main(){
    pre();
    int t,cas=1;
    scanf("%d",&t);
    while(t--){
	long long n;
	scanf("%I64d",&n);
	printf("Case #%d: %d\n",cas++,solve(n));
    }
}
