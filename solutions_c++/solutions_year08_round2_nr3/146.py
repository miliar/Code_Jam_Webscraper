#include<stdio.h>

#define MAX 5005

#define nex(p)	((p+1)%na)
#define pev(p)	((p-1+na)%na)

int k,n,x[MAX];
int na,a[MAX];

void insert(int v,int l){
	int i;
	for(i=na;i>=l;i--)
		a[i+1] = a[i];
	a[l] = v;
	na++;
}

int main(){
	int T,N;
	int i,j,c;
	scanf("%d",&T);
	for(N=1;N<=T;N++){
		
		scanf("%d%d",&k,&n);

		for(i=0;i<n;i++){
			scanf("%d",&x[i]);
			x[i]--;
		}


		na = 0;
		insert(k,0);
		j = 0;

		for(i=k-1;i>=1;i--){
			c = 1;
			while(c < i+1){
				j = pev(j);
				c++;
			}
			insert(i,j);
		}

/*		for(i=0;i<na;i++){
			printf("%d ",a[j]);
			j = nex(j);
		}
		printf("\n");
*/
		printf("Case #%d:",N);
		for(i=0;i<n;i++)
			printf(" %d",a[(j+x[i])%na]);
		printf("\n");
		

	}
	return 0;
}