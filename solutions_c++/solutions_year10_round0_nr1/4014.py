#include<cstdio>

int main(){
	int v[50];
	int i;
	v[0]=1;
	for(i=1;i<31;i++){
		v[i]=2*v[i-1];
	}
	
	
	int totalTests, testNum=1;
	int n,k,mod;
	scanf("%d\n",&totalTests);
	while(totalTests--){
		printf("Case #%d: ",testNum++);
		scanf("%d %d\n",&n,&k);
		mod = k%v[n];
		if(mod == v[n]-1){
			printf("ON\n");
		}else{
			printf("OFF\n");
		}
		
	}
}
