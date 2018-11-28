#include<stdio.h>
#include<stdlib.h>
#include<string.h>


int n, k;
int ttt;
void solve(){
	int i,j;
	scanf("%d%d", &n,&k);
	j = 1;
	for(i=0;i<n;++i){
		if(!(k&j)) break;
		j<<=1;
	}
	printf("Case #%d: ",++ttt);
	if(i>=n){
		printf("ON\n");
	}else{
		printf("OFF\n");
	}
}
int main(){
//	freopen("A-large.in","r",stdin);
//	freopen("A-large.out","w",stdout);
	int t;scanf("%d",&t);
	ttt=0;
	while(--t>=0) solve();
	return 0;
}
