#include<stdio.h>
#include<stdlib.h>
#include<math.h>

bool is_bit_set(int a, int b){
	return ((a | (1 << b)) == a);
}
bool makes_run(int k, int n){
	for(int i = 0;i < n;i++){
		if(!is_bit_set(k, i))return false;
	}return true;
}

int main(){
	int num_case = 0;
	scanf("%d", &num_case);
	for(int caseno = 0;caseno < num_case;caseno++){
		int n, k;
		scanf("%d %d", &n, &k);
		printf("Case #%d: ", caseno+1);
		if(makes_run(k%((int)pow(2, n)), n))
			printf("ON\n");
		else
			printf("OFF\n");
	}
}
