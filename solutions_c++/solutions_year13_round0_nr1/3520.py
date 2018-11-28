#include <stdio.h>
int main() {
	int t;
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	scanf("%d", &t);
	for(int k = 1; k <= t; k++) {
		char a[5][5];
		int rx[5] = {0}, ro[5] = {0}, rp[5] = {0}, lx[5] = {0}, lo[5] = {0}, lp[5] = {0}, key = 0, flag = 0;
		for(int i = 0; i < 4; i++) scanf("%s", a[i]);
		printf("Case #%d: ", k);
		for(int i = 0; i < 4; i++) for(int j = 0; j < 4; j++) {
			if(a[i][j] == 'X') rx[i]++, lx[j]++;
			else if(a[i][j] == 'O') ro[i]++, lo[j]++;
			else if(a[i][j] == '.') rp[i]++, lp[j]++, key = 1;
		}
		for(int i = 0; i < 4; i++) {
			if(rx[i] - ro[i] - rp[i] >= 3 || lx[i] - lo[i] - lp[i] >= 3) {
				flag = 1;
				printf("X won\n");
				break;
			}
			else if(ro[i] - rx[i] - rp[i] >= 3 || lo[i] - lx[i] - lp[i] >= 3) {
				flag = 1;
				printf("O won\n");
				break;			 
			}
		}
		if(flag == 0) {
			int x = 0, o = 0, p = 0;
			for(int i = 0; i < 4; i++) {
				if(a[i][i] == 'X') x++;
			    else if(a[i][i] == 'O') o++;
			    else if(a[i][i] == '.') p++, key = 1;
			}
			if(x - o - p >= 3) {
				flag = 1;
				printf("X won\n");
			}
			else if(o - x - p >= 3) {
				flag = 1;
				printf("O won\n");
			}
			else {
				x = 0, o = 0, p = 0;
			    for(int i = 0, j = 3; i < 4 && j >= 0; i++, j--) {
				  if(a[i][j] == 'X') x++;
			      else if(a[i][j] == 'O') o++;
			      else if(a[i][j] == '.') p++, key = 1;
		     	}
		     	if(x - o - p >= 3) {
			      flag = 1;
				  printf("X won\n");
		    	}
		    	if(o - x - p >= 3) {
				  flag = 1;
				  printf("O won\n");
		    	}  
			}
		}
		if(key == 1 && flag == 0) printf("Game has not completed\n");
		else if(!flag) printf("Draw\n"); 
	}
}