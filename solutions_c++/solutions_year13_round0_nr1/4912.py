#include <cstdio>
#include <cstdlib>

using namespace std;

int grid[4][4];

int solve() {
	
	int moves=0;
	int rows[2][4];
	int columns[2][4];
	int diag[2][2];
	
	for (int i=0; i<2; ++i) {
		for (int j=0; j<4; ++j) {
			rows[i][j] = 0;
			columns[i][j] = 0;
			diag[i][j/2] = 0;
		}
	}
	
	scanf("\n");
	for (int i=0; i<4; ++i) {
		for (int j=0; j<4; ++j) {
			char c;
			scanf("%c",&c);
			//printf("%c",c);
			switch(c) {
				case '.':
					grid[i][j] = 0;
					break;
					
				case 'X':
					grid[i][j] = 1;
					rows[0][i]++;
					columns[0][j]++;
					if ( i==j ) diag[0][0]++;
					if ( i+j==3 ) diag[0][1]++;
					break;
					
				case 'O':
					grid[i][j] = 2;
					rows[1][i]++;
					columns[1][j]++;
					if ( i==j ) diag[1][0]++;
					if ( i+j==3 ) diag[1][1]++;
					break;
					
				case 'T':
					grid[i][j] = 3;
					
					rows[0][i]++;
					columns[0][j]++;
					if ( i==j ) diag[0][0]++;
					if ( i+j==3 ) diag[0][1]++;
					
					rows[1][i]++;
					columns[1][j]++;
					if ( i==j ) diag[1][0]++;
					if ( i+j==3 ) diag[1][1]++;
					
					break;
			}
			if ( grid[i][j] != 0 ) moves++;
		}
		scanf("\n");
	}

	
	bool end = (moves == 16);
	
	for (int i=0; i<4; ++i) {
		if ( rows[0][i] == 4 || columns[0][i] == 4 ) {
			//printf("Row/col %d victory of X\n",i);
			return 0; // X victory
		}
		if ( rows[1][i] == 4 || columns[1][i] == 4 ) {
			//printf("Row/col %d victory of O\n",i);
			return 1; // O victory
		}

	}
	for (int i=0; i<2; ++i) {
		if ( diag[0][i] == 4 ) {
			//printf("Diag %d victory of X\n",i);
			return 0;
		}
		if ( diag[1][i] == 4 ) {
			//printf("Diag %d victory of O\n",i);
			return 1;
		}
	}
	
	if ( end ) {
		//printf("Draw\n");
		return 2; // Draw
	}
	
	//printf("Not ended\n");
	return 3; // Not ended
}

int main() {
	
	int t;
	scanf("%d",&t);
	
	for (int i=0; i<t; ++i) {
		int res = solve();
		printf("Case #%d: ",i+1);
		switch (res) {
			case 0:
				printf("X won\n");
				break;
			case 1:
				printf("O won\n");
				break;
			case 2:
				printf("Draw\n");
				break;
			case 3:
				printf("Game has not completed\n");
				break;
		}
	}
	
	return 0;
}
