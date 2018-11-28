// thiagokronig@gmail.com

#include <stdio.h>
#include <stack>
#include <stdlib.h>
 #include <string.h>

using namespace std;

int main () {

	int m;
	char *s;
	
	int ii;
	
	stack<int> pilha;
	
	
	char map[50][50];
	int i,j,l;
	int process = 0;

	int t, n, k;
	char c;
	
	int red_win, blue_win;

	
	int red[50][50][4], blue[50][50][4];
	
	int I,J;
	
	scanf("%d",&t);
	
	for (ii=1; ii <= t; ii++) {
	
	
		scanf("%d %d",&n,&k);		
		getchar();
		
		
		l = 0;
		I = J = m = 0;
		for (i=0; i<n; i++) { 
		
			for (j=0; j<n; j++) {
				scanf("%c",&c);
				
				if (c!= '.') {
					pilha.push(c);
				}				
			}
			
			J = 0;
			memset(map[I], 0, n);
			if (!pilha.empty()) {
				while (!pilha.empty()) {
					l = pilha.top();
					pilha.pop();				
					map[I][J++] = l;
				}
				
				m = m < j ? j : m;
			
				I++;
			}
			

			
			getchar();
		}
		
		n = I;

		red_win = 0;
		blue_win = 0;

		for (i=0; i< n; i++) {
			if (red_win && blue_win) break;
		
			for (j=0; j<m ; j++) {
			
				
				if (map[i][j] == 'B') {
						for (l=0; l<4; l++)
						blue[i][j][l] = 1;
						
					// horizontal
						if (j > 0 && map[i][j-1] == 'B')
							blue[i][j][0] += blue[i][j-1][0];

					// vertical
						if (i > 0 && map[i-1][j] == 'B') 
							blue[i][j][1] += blue[i-1][j][1];
						
					// diagonal direita
						if (i > 0 && j + 1 < m && map[i-1][j+1] == 'B')
							blue[i][j][2] += blue[i-1][j+1][2];
							
					// diagonal esquerda
						if (i > 0 && j > 0 && map[i-1][j-1] == 'B')
							blue[i][j][3] += blue[i-1][j-1][3];
					
/*					for (l=0; l<4; l++)
						printf("%d %d %d %d\n",i,j,l,red[i][j][l]);*/
					
					for (l=0; l<4; l++)
						if (blue[i][j][l] >= k) {
							blue_win = 1;
							break;
						}
				}
				
				else if  (map[i][j] == 'R') {
					for (l=0; l<4; l++)
						red[i][j][l] = 1;
						
					// horizontal
						if (j > 0 && map[i][j-1] == 'R')
							red[i][j][0] += red[i][j-1][0];

					// vertical
						if (i > 0 && map[i-1][j] == 'R') 
							red[i][j][1] += red[i-1][j][1];
						
					// diagonal direita
						if (i > 0 && j + 1 < m && map[i-1][j+1] == 'R')
							red[i][j][2] += red[i-1][j+1][2];
							
					// diagonal esquerda
						if (i > 0 && j > 0 && map[i-1][j-1] == 'R')
							red[i][j][3] += red[i-1][j-1][3];
					
/*					for (l=0; l<4; l++)
						printf("%d %d %d %d\n",i,j,l,red[i][j][l]);*/
					
					for (l=0; l<4; l++)
						if (red[i][j][l] >= k) {
							red_win = 1;
							break;
						}
				}
				
				
				
				else break;			
			}
		}


			
		if (blue_win && red_win) {
			printf("Case #%d: Both\n", ii);
		} else if (blue_win)
			printf("Case #%d: Blue\n", ii);
		else if (red_win)
			printf("Case #%d: Red\n", ii);
		else
			printf("Case #%d: Neither\n", ii);
		
			
		//printf("Case #%d: %s\n", ii, s);
	}


	return 0;
}
