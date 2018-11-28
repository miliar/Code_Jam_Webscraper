//#include<conio.h>
#include<assert.h>
#include<stdio.h>
#include<string.h>

#define MAX 1005

typedef __int64 LL;

int n;
LL	sum,times,cap,tot;// , loop;
LL	g[MAX*4];
int start[4*MAX];
LL	cnt[4*MAX];

int main(){

	int i,j,k,ct;
	LL run;

	int T,N;

	scanf("%d",&T);
 
	for(N=1;N<=T;N++){
	
		scanf("%I64d%I64d%d",&times, &cap, &n);

		sum = 0;
		for(i=0;i<n;i++){
			scanf("%I64d",&g[i]);
			sum+=g[i];
			g[i+n]=g[i];
		}

//		printf("!!!!\n");

		memset(start,-1,sizeof(start));

		cnt[0] = 0;
//		loop = 0;
		i = 0;
		start[0] = 0;
		int flag = 0;

		for(k=1;k<=times;k++){
//			printf("%d %I64d : ",k,times);
			run = 0;
			for(j=i,ct=0;run+g[j]<=cap && ct<n;j=(j+1)%n,ct++)
				run += g[j];

//			printf("<%d %d>\n",i,(j+n-1)%n);
			cnt[k] = cnt[k-1] + run;
			if(start[j] == -1)
				start[j] = k;
			else if(flag==0){
				flag =1;
				assert((k - start[j]) != 0);

//				printf(">>> %d %d %d\n",j, start[j], k);

				cnt[k] += (cnt[k] - cnt[start[j]]) * ((times-(k)) / (k - start[j]));
//				printf("!! %I64d\n",loop);
				times = k + (times-(k)) % (k - start[j]);
			}
///			getch();
			i = j;
		}

		printf("Case #%d: %I64d\n",N,cnt[times]);
			
	}

	return 0;
}