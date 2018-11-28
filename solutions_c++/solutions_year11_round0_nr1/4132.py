#include <stdio.h>

int t, n;
int res;
int o, b;
int bonusO, bonusB;
int posTemp;
char color;
int temp;

int absoluto(int a){
	return a > 0 ? a : -a;
}

int positivo(int a){
	return a > 0 ? a : 0;
}

int main(){
	scanf("%d", &t);
	for(int i = 1; i <= t; i++){
		res = 0;
		o = 1;
		b = 1;
		bonusO = 0;
		bonusB = 0;
		scanf("%d", &n);
		for(int j = 1; j <= n; j++){
			scanf(" %c %d", &color, &posTemp);
			if(color == 'B'){
				temp = positivo(absoluto(b - posTemp) - bonusB) + 1;
				bonusO += temp;
				res+= temp;
				bonusB = 0;
				b = posTemp; 
			}
			else{
				temp = positivo(absoluto(o - posTemp) - bonusO) + 1;
				bonusB += temp;
				res+= temp;
				bonusO = 0;
				o = posTemp;
			}
		}
		printf("Case #%d: %d\n", i, res);
	}
	
	return 0;
}