#include<stdio.h>
#include<stdlib.h>

const int MAX=801;

int cmp1(const void* p1,const void* p2){
	int pp1 = *((int *)p1);
	int pp2 = *((int *)p2);
	return pp1-pp2;
}

int cmp2(const void* p1,const void* p2){
	int pp1 = *((int *)p1);
	int pp2 = *((int *)p2);
	return pp2-pp1;
}


int main(){
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
	int t,n;
	int v1[MAX],v2[MAX];
	__int64 sum;
	scanf("%d",&t);
	for(int c=1;c<=t;c++){
		scanf("%d",&n);
		for(int i=0;i<n;i++)	scanf("%d",&v1[i]);
		for(int i=0;i<n;i++)	scanf("%d",&v2[i]);
		qsort(v1,n,sizeof(int),cmp1);
		qsort(v2,n,sizeof(int),cmp2);
		sum=0;
		for(int i=0;i<n;i++)	sum+=v1[i]*v2[i];
		printf("Case #%d: %lld\n",c,sum);
	}
	return 0;

}
