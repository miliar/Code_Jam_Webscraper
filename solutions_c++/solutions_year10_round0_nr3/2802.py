#include<stdio.h>
int arr[10000],f[10000];
long long sum[10000];
int main(){
	int R,k,N,i;
	long long res,tot;
	int tt,t;
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
	scanf("%d",&tt);
	for (t=1;t<=tt;t++)
	{
		scanf("%d%d%d",&R,&k,&N);
		res = 0;
		for (i=0;i<N;i++)
			scanf("%d",&arr[i]);
		for (i=N;i<2*N;i++)
			arr[i] = arr[i-N];
		for (i=0;i<N;i++)
		{
			tot = 0;
			f[i] = 0;
			sum[i] = 0;
			int j=i;
			while(tot<=k){
				tot+=arr[j];
				if (tot>k) break;
				f[i]++;
				sum[i] = tot;
				j++;
				if (f[i]==N) break;
			}
		}
		i = 0;
		while(R--){
			res+=sum[i];
			i = (i+f[i])%N;
		}
		printf("Case #%d: %lld\n",t,res);
	}
}
			
