#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int a1[110],a2[110],b1[110],b2[110];
int tests,ss;
int t,na,nb;

int cmp(const void *a,const void *b){
	return *(int *)a-*(int *)b;
}

int calc(int a[],int b[],int tota,int totb){
	int i,j,k,ans;
	k=ans=0;
	for (i=j=1;i<=tota;i++){
		while (j<=totb && b[j]<=a[i]){
			j++;
			k++;
		}
		if (k) k--;
		else ans++;
	}
	return ans;
}

int main(){
	int hour1,min1,hour2,min2,i;
	scanf("%d\n",&tests);
	for (ss=1;ss<=tests;ss++){
		scanf("%d%d%d",&t,&na,&nb);
		for (i=1;i<=na;i++){
			scanf("%d:%d %d:%d",&hour1,&min1,&hour2,&min2);
			a1[i]=hour1*60+min1;
			a2[i]=hour2*60+min2+t;
		}
		for (i=1;i<=nb;i++){
			scanf("%d:%d %d:%d",&hour1,&min1,&hour2,&min2);
			b1[i]=hour1*60+min1;
			b2[i]=hour2*60+min2+t;
		}
		qsort(a1+1,na,sizeof a1[0],cmp);
		qsort(a2+1,na,sizeof a2[0],cmp);
		qsort(b1+1,nb,sizeof b1[0],cmp);
		qsort(b2+1,nb,sizeof b2[0],cmp);
		printf("Case #%d: %d %d\n",ss,calc(a1,b2,na,nb),calc(b1,a2,nb,na));
	}
}
