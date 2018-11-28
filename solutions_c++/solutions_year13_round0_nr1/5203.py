#include<cstdio>
using namespace std;

int main(){
	int Z;
	scanf("%d",&Z);
	for(int Q = 1; Q<=Z; ++Q){
		char T[5][5];
		int state = 0, empty = 0;
		for(int i = 0; i < 4 ; ++i){
			scanf("%s",T[i]);
			for(int j = 0; j < 4; j++){
				if(T[i][j]=='.')empty++;
				switch(T[i][j]){
					case '.': T[i][j] = 50;break;
					case 'X': T[i][j] = 1;break;
					case 'O': T[i][j] = 10;break;
					default:  T[i][j] = 0;
				}
			}
		}
		if(!empty)state = 3;
		int sum=T[0][0]+T[1][1]+T[2][2]+T[3][3];	
		if(sum == 3 || sum == 4)state = 1;
		if(sum == 30 || sum == 40)state = 2;
		sum=T[3][0]+T[2][1]+T[1][2]+T[0][3];	
		if(sum == 3 || sum == 4)state = 1;
		if(sum == 30 || sum == 40)state = 2;
		for(int i = 0; i < 4; i++){
			sum = T[i][0] + T[i][1] + T[i][2] + T[i][3];
			if(sum == 3 || sum == 4)state = 1;
			if(sum == 30 || sum == 40)state = 2;
			sum = T[0][i] + T[1][i] + T[2][i] + T[3][i];
			if(sum == 3 || sum == 4)state = 1;
			if(sum == 30 || sum == 40)state = 2;
		}
			
		printf("Case #%d: ", Q);
		switch(state){
			case 0: printf("Game has not completed\n");break;
			case 1: printf("X won\n");break;
			case 2: printf("O won\n");break;
			case 3: printf("Draw\n");break;
		}
	}
	return 0;
}
