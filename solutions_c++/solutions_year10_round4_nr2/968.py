#include <stdio.h>
#define	MAX	1024

int m[MAX];
int ticket[MAX][MAX];
static inline int watch(int x, int range){
	int i;
	for(i=x;i<x+range;i++)
		if(m[i]>0) return 1;
	return 0;
}
void update(int x, int range){
	int i;
	for(i=x;i<x+range;i++)
		m[i]--;
}
void solve(){
	int P,count=0,range;
	int i,j,cost=0;
	scanf("%d", &P);
	for(i=0;i<(1<<P);i++){
		scanf("%d", &m[i]);
		m[i] = P-m[i];
		count+=m[i];
	}
	for(i=P-1;i>=0;i--){
		for(j=0;j<(1<<i);j++)
			scanf("%d", &ticket[i][j]);
	}
	for(range=1<<P; range>0; range/=2){
		for(i=0;i<(1<<P);i+=range){
			if(watch(i, range)){
				cost++;
				update(i,range);
			}
		}
	}
	printf("%d\n", cost);
}
int main(){
	int T, i;
	scanf("%d", &T);
	for(i=0;i<T;i++){
		printf("Case #%d: ", i+1);
		solve();
	}
	return 0;
}
