#include <stdio.h>
#include <string.h>

typedef long long LL;
LL sum[2048],cont[1024];
int a[2048],u[1024],next[1024];
int main(){
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	int T,R,K,N,t,i,j,d,p;
	LL s;
	scanf("%d",&T);
	for (t = 1;t <= T;t++){
		scanf("%d%d%d",&R,&K,&N);
		for (i = 0;i < N;i++){
			scanf("%d",&a[i]);
			a[i+N] = a[i];
		}
		for (i = 0;i < N;i++){
			for (s = 0,j = 0;s <= K && j < N;j++)
				s += a[i+j];
			--j;
			if (s > K) s -= a[i+j];
			cont[i] = s;
			next[i] = (i+j) % N;
		}
		memset(u,0,sizeof(u));
		i = 0,j = 0;
		while (!u[i]){
			u[i] = ++j;
			sum[j] = sum[j-1]+cont[i];
			i = next[i];
		}
		d = u[i]-1,p = j-d;
		printf("Case #%d: ",t);
		if (R <= d) printf("%lld\n",sum[R]);
		else{
			s = (R-d-1) / p*(sum[j]-sum[d]);
			s += sum[d+1+(R-d-1) % p];
			printf("%lld\n",s);
		}
	}
	fclose(stdout);
}
