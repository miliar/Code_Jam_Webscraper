#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#define Max(a,b) ((a)>(b)?(a):(b))
#define Min(a,b) ((a)<(b)?(a):(b))

struct node{
	int h,w;
}a[1100],b[1100];

int cmp(const void *a,const void *b){
	return ((node*)a)->h - ((node*)b)->h;
}

int main(){
	int t,T,n,i,j;
	freopen("A-small-attempt0.in","r",stdin);
	freopen("1.out","w",stdout);
	scanf("%d",&T);
	for(t = 1; t <= T; t++){
		scanf("%d",&n);
		for(i = 0; i < n; i++){
			scanf("%d",&a[i].h);
			a[i].w = i;
			scanf("%d",&b[i].h);
			b[i].w = i;
		}
		int sum = 0;
		qsort(a,n,sizeof(a[0]),cmp);
		qsort(b,n,sizeof(b[0]),cmp);
		for(i = 0; i < n; i++){
			for(j = i; j < n; j++){
				if(b[j].w == a[i].w){
					sum += j-i;
					break;
				}
			} 
		}
		printf("Case #%d: %d\n",t,sum);
	}
	return 0;
}