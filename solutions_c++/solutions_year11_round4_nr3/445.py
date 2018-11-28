#include <iostream>
#include <cstring>
#include <cstdio>
#include <cmath>
using namespace std;

const int maxn=1100001;//ËØÊýÉžÑ¡µÄ·¶Î§

int prime[maxn],tot_prime;//ÓÃÓÚ±£ŽæËØÊýŒ°ËØÊýµÄžöÊý
bool isp[maxn];

int sp_sum[maxn], div_sum[maxn]; //Õý³ýÊýÖ®ºÍº¯Êý
int sp_num[maxn], div_num[maxn]; //Õý³ýÊýžöÊýº¯Êý
int phi[maxn]; //Å·À­º¯Êý
int mobius[maxn]; //Äª±ÈÎÚº¯Êý

void cal_prime()
{
	tot_prime=0;
	memset(isp,0,sizeof(isp));
	div_num[1]=div_sum[1]=phi[1]=mobius[1]=1;
	
	for (int i=2; i<maxn; ++i) {
		if (!isp[i]) {
			prime[++tot_prime]=i;
			div_sum[i]=1+i;   sp_sum[i]=i*i;
			div_num[i]=2;    sp_num[i]=2;
			phi[i]=i-1;  
			mobius[i]=-1;
		}
		for (int j=1, num=i*prime[j]; j<=tot_prime && i*prime[j]<maxn; num=i*prime[++j]) {
			isp[num]=1;
			if (i%prime[j]>0) {
				sp_sum[num]=prime[j]*prime[j];
				div_sum[num]=div_sum[i]*(sp_sum[num]-1)/(prime[j]-1);

				sp_num[num]=2;
				div_num[num]=div_num[i]*sp_num[num];

				phi[num]=phi[i]*(prime[j]-1);

				mobius[num]=mobius[i]*(-1);
			} else {
				div_sum[num]=div_sum[i]*(sp_sum[i]*prime[j]-1)/(sp_sum[i]-1); //×¢ÒâÒç³ö
				sp_sum[num]=sp_sum[i]*prime[j];

				div_num[num]=div_num[i]/sp_num[i]*(sp_num[i]+1);
				sp_num[num]=sp_num[i]+1;

				phi[num]=phi[i]*prime[j];

				mobius[num]=0;

				break;
			}
		}
	}
}

int main(){
	cal_prime();
	int t,n,h,i;
	double f;
	long long ans;
	scanf("%d",&t);
	for(h=1;h<=t;h++){
		scanf("%d",&n);
		printf("Case #%d: ",h);
		if(n==1){
			printf("0\n");
			continue;
		}
		ans=0;
		for(i=1;i<=tot_prime;i++){
			if(prime[i]*prime[i]>n)break;
			f=log(n)/log(prime[i])-1;
			ans+=(int)(f+1e-9);
		}
		printf("%lld\n",ans+1);
	}
	return 0;
}
