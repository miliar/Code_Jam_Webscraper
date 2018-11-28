# include<stdio.h>


int main(){
	freopen("A-large.in", "r", stdin);
	freopen("A-large0.out","w", stdout);
	int t, n, k, i, j,value;	
	scanf("%d",&t);
	for(i=1; i<=t; i++){
		scanf("%d %d",&n,&k);
		if(n==1){
			if(k==0 || k%2==0)
				printf("Case #%d: OFF\n",i);
			else
				printf("Case #%d: ON\n",i);
			continue;
		}
		if(k==0 || k%2==0){
			printf("Case #%d: OFF\n",i);
			continue;
		}
		value= k;
		for(j=1; j<n; j++){
			value--;
			value/=2;
			if(value%2==0){				
				break;
			}
		}
		if(value%2==0)
			printf("Case #%d: OFF\n",i);
		else
			printf("Case #%d: ON\n",i);
	}
	return 0;
}