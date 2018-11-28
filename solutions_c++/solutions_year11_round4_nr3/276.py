#include<cstdio>

int Z;
long long N;
long long p[1000000],P=0;
bool b[1000005];

int main(){
	for (int i=2;i<=1000000;++i){
		if (!b[i]){
			p[P++] = i;
			for (int j=i+i;j<=1000000;j+=i){
				b[j] = 1;
			}
		}
	}
	
	scanf("%d",&Z);
	for (int z=1;z<=Z;++z){
		scanf("%lld",&N);
		long long cnt = 1;
		for (int i=0;i<P && p[i]*p[i]<=N;++i){
			long long n = N;
			while (n>=p[i]*p[i]){
				n/=p[i];
				++cnt;
			}
		}
		
		printf("Case #%d: ",z);
		if (N==1){
			puts("0");
		}else{
			printf("%lld\n",cnt);
		}
		
	}
	return 0;
}
