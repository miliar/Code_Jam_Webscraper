#include<stdio.h>
#include<stdlib.h>
#include<string>

using namespace std;

int T;
int x[10], o[10];
int full, o_won, x_won;
char c;

int main(){
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	scanf("%d", &T);
	for(int t = 1; t <= T; t++){
		for(int i = 0; i < 10; i++){
			x[i] = 0;
			o[i] = 0;
		}
		full = 16;
		for(int i = 0; i < 4; i++){
			for(int j = 0; j < 4; j++){
				scanf(" %c", &c);
				if (c == 'X' || c == 'T'){
					x[i]++;
					x[4 + j]++;
					if (i == j) x[8]++; 
					if (i + j == 3)  x[9]++;
				}
				if (c == 'O' || c == 'T'){
					o[i]++;
					o[4 + j]++;
					if (i == j) o[8]++; 
					if (i + j == 3)  o[9]++;
				}
			    if (c != '.') full--;
			}
		}
		o_won = 0;
		x_won = 0;
		printf("Case #%d: ", t);
		for(int i = 0; i < 10; i++){
			if (x[i] == 4) x_won = 1;
			if (o[i] == 4) o_won = 1;
		}
		if (x_won && !o_won)
			printf("X won\n");
		if (!x_won && o_won)
			printf("O won\n");
		if (x_won && o_won)
			printf("Draw\n");
		if (!x_won && !o_won && !full)
			printf("Draw\n");
		if (!x_won && !o_won && full)
			printf("Game has not completed\n");
	}
	return 0;
}