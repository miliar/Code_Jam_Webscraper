#include <cstdio>

char x[4][5];
int c;

void check(){
	bool w;
	
	for (int q = 0; q < 4; q++){
		w = true;
		for (int e = 0; e < 4; e++)
			if (x[q][e] == 'O' || x[q][e] == '.')
				w = false;
		if (w){
			printf("Case #%d: X won\n", ++c);
			return;
		}
	}
	for (int q = 0; q < 4; q++){
		w = true;
		for (int e = 0; e < 4; e++)
			if (x[e][q] == 'O' || x[e][q] == '.')
				w = false;
		if (w){
			printf("Case #%d: X won\n", ++c);
			return;
		}
	}
	w = true;
	for (int e = 0; e < 4; e++)
		if (x[e][e] == 'O' || x[e][e] == '.')
			w = false;
	if (w){
		printf("Case #%d: X won\n", ++c);
		return;
	}
	
	w = true;
	for (int e = 0; e < 4; e++)
		if (x[e][3-e] == 'O' || x[e][3-e] == '.')
			w = false;
	if (w){
		printf("Case #%d: X won\n", ++c);
		return;
	}
	
	
	
	
	
	
	for (int q = 0; q < 4; q++){
		w = true;
		for (int e = 0; e < 4; e++)
			if (x[q][e] == 'X' || x[q][e] == '.')
				w = false;
		if (w){
			printf("Case #%d: O won\n", ++c);
			return;
		}
	}
	for (int q = 0; q < 4; q++){
		w = true;
		for (int e = 0; e < 4; e++)
			if (x[e][q] == 'X' || x[e][q] == '.')
				w = false;
		if (w){
			printf("Case #%d: O won\n", ++c);
			return;
		}
	}
	w = true;
	for (int e = 0; e < 4; e++)
		if (x[e][e] == 'X' || x[e][e] == '.')
			w = false;
	if (w){
		printf("Case #%d: O won\n", ++c);
		return;
	}
	
	w = true;
	for (int e = 0; e < 4; e++)
		if (x[e][3-e] == 'X' || x[e][3-e] == '.')
			w = false;
	if (w){
		printf("Case #%d: O won\n", ++c);
		return;
	}
	
	
	w = true;
	for (int q = 0; q < 4; q++)
		for (int e = 0; e < 4; e++)
			if (x[q][e] == '.')
				w = false;
	if (w)
		printf("Case #%d: Draw\n", ++c);
	else
		printf("Case #%d: Game has not completed\n", ++c);
}


int main(){
	int n;
	
	scanf("%d", &n);
	for (int i = 0; i < n; i++){
		for (int j = 0; j < 4; j++)
			scanf(" %s", x[j]);
		
		check();
	}
	
}
