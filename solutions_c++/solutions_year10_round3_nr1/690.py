#include <stdio.h>
#include<stdlib.h>

#define maxn 1001

struct node {
	int a;
	int b;
} nod[maxn];

int compare (const void * a, const void * b){
  return ( (*(node*)a).a - (*(node*)b).a );
}


int main() {

    freopen ( "C:\\A-large.in", "r", stdin );
    freopen ( "C:\\A-large.out", "w", stdout );
	int T,p;
	int N;
	int i,j;
	int sum;
	scanf("%d",&T);
	for(p = 1;p <= T;p++)
	{
		sum = 0;
		scanf("%d",&N);
		for(i = 0;i < N;i++)
		scanf("%d %d",&nod[i].a,&nod[i].b);
		qsort(nod,N,sizeof(nod[0]),compare);

		for(i = 1;i < N;i++)
		{
			for(j = 0;j < i;j++)
				if(nod[j].b > nod[i].b)
					sum++;
		}
		 printf ( "Case #%d: %d\n", p,sum );
	}
	return 0;
}
