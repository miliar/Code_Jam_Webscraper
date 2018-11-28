#include <iostream>
#include <cstdio>
#include <cmath>
using namespace std;

#define steps(o,d) (abs(o-d)+1)

int main(){
	int N,m,i,j;
	char R;
	int P;
	int time_O, time_B, pos_O, pos_B;
	FILE* fout = fopen("A.out", "w");
	
	scanf("%d", &N);
	for(j=0; j<N; j++){
		pos_O = 1;
		pos_B = 1;
		time_O = 0;
		time_B = 0;
		scanf("%d", &m);
		for(i=0; i<m; i++){
			scanf("%s %d", &R, &P);
			if(R == 'O'){
				if(time_O + steps(P, pos_O) <= time_B){
					time_O = time_B + 1;
				}
				else{
					time_O += steps(P, pos_O);
				}
				pos_O = P;
			}
			if(R == 'B'){
				if(time_B + steps(P, pos_B) <= time_O){
					time_B = time_O + 1;
				}
				else{
					time_B += steps(P, pos_B);
				}
				pos_B = P;
			}
		}		
		fprintf(fout, "Case #%d: %d\n", j+1, time_O > time_B? time_O: time_B);
	}
	
	
	return 0;
}