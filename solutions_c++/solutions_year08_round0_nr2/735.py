#include<stdio.h>
#include<stdlib.h>

int a1[120],a2[120],b1[120],b2[120];

int cmp(const void* a,const void *b)
{
	return -(*(const int*)a - *(const int*)b);
}

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);

	int N,NA,NB,T;
	int i,j,k,t1,t2;
	int ch;
	int rt1,rt2;
	scanf("%d",&N);
	for(i=0;i<N;i++){
		scanf("%d%d%d",&T,&NA,&NB);
		for(j=0;j<NA;j++){
			scanf("%d%c%d",&t1,&ch,&t2);
			a1[j] = t1*100 + t2;

			scanf("%d%c%d",&t1,&ch,&t2);
			t2 += T;
			t1 += t2 / 60;
			t2 %= 60;
			a2[j] = t1*100 + t2;
		}
		qsort(a1,NA,sizeof(int),cmp);
		qsort(a2,NA,sizeof(int),cmp);

		for(j=0;j<NB;j++){
			scanf("%d%c%d",&t1,&ch,&t2);
			b1[j] = t1*100 + t2;

			scanf("%d%c%d",&t1,&ch,&t2);
			t2 += T;
			t1 += t2 / 60;
			t2 %= 60;
			b2[j] = t1*100 + t2;
		}
		qsort(b1,NB,sizeof(int),cmp);
		qsort(b2,NB,sizeof(int),cmp);
		rt1 = NA;
		rt2 = NB;
		
		k = 0;
		for(j=0;j<NA;j++){
			while(a1[j] < b2[k]){
				k++;
				if(k>=NB)break;
			}
			if(k>=NB)break;
			else{
				rt1--;
				k++;
				if(k>=NB)break;
			}
		}

		k = 0;
		for(j=0;j<NB;j++){
			while(b1[j] < a2[k]){
				k++;
				if(k>=NA)break;
			}
			if(k>=NA)break;
			else{
				rt2--;
				k++;
				if(k>=NA)break;
			}
		}
		
		printf("Case #%d: %d %d\n",i+1,rt1,rt2);
	}
	return 0;
}