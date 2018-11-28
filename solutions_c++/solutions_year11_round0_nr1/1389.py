#include<cstdio>
#include<algorithm>
#include<cmath>
using namespace std;

int main(){
	int t;
	scanf("%d", &t);
	for(int i = 1; i <= t; i++){
		int poz_O = 1, poz_B = 1, ruchy_O = 0, ruchy_B = 0, n, wyn = 0, cel, przes;
		char znak;
		scanf("%d", &n);
		while(n--){
			scanf(" %c %d", &znak, &cel);
			if(znak=='O'){
				przes = max(abs(poz_O-cel)-ruchy_O, 0)+1;
				poz_O = cel;
				ruchy_O = 0;
				ruchy_B += przes;
			}
			else{ //znak=='B'
				przes = max(abs(poz_B-cel)-ruchy_B, 0)+1;
				poz_B = cel;
				ruchy_B = 0;
				ruchy_O += przes;
			}
			wyn += przes;
		}
		printf("Case #%d: %d\n", i, wyn);
	}
	return 0;
}
