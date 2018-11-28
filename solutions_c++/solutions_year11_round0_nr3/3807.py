#include <stdio.h>

int t;
int n;
int valores[100];

int limite;

int res;

void analiza(int cual){
	int sean = 0;
	int patrick = 0;
	int seanReal = 0;
	for(int i = 0; i < n; i++ ){
		if(((cual >> i) & 1) == 1 ){
			sean ^= valores[i];
			seanReal += valores[i];
		}
		else{
			patrick ^= valores[i];
		}
	}
	if(sean == patrick && seanReal > res){
		res = seanReal;
	}
}

int main(){
	scanf("%d", &t);
	for(int i = 1; i <= t; i++){
		limite = 0;
		res = 0;
		scanf("%d", &n);
		for(int j = 0; j < n; j++){
			scanf("%d", &valores[j]);
		}
		//probamos todos
		limite = 1 << n;
		limite-=2;
		for(int j = 1; j <= limite; j++){
			analiza(j);
		}
		printf("Case #%d: ", i);
		if(res > 0){
			printf("%d\n", res);
		}
		else{
			printf("NO\n");
		}
	}
	return 0;
}