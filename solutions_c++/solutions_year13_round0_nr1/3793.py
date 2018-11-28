#include <stdio.h>

int main() {
	FILE * iFile;
	FILE * oFile;
	iFile = fopen("A-large.in", "r");
	oFile = fopen("A-large.out", "w");
	int T, i, row, col;
	char C;
	int Os, Xs;
	const char * stats[4];
	stats[0] = "X won";
	stats[1] = "O won";
	stats[2] = "Draw";
	stats[3] = "Game has not completed";
	fscanf(iFile, "%d\n", &T);
	for(i = 1; i <= T; i++) {
		// Here comes the logic
		int cont = 1;
		int stat = 0;
		int Xcol[4] = {0, 0, 0, 0};
		int Ocol[4] = {0, 0, 0, 0};
		int drightX = 0;
		int drightO = 0;
		int dleftX = 0;
		int dleftO = 0;
		int points = 0;
		// Read character by character
		for(row = 0; row < 4 && cont == 1; row++) {
			Xs = 0;
			Os = 0;
			for(col = 0; col < 5 && cont == 1; col++) {
				fscanf(iFile, "%c", &C);
				switch(C) {
					case 'X':
						Xs++;
						Xcol[col]++;
						if(col == row) {
							drightX++;
						} else if(col == (3-row)) {
							dleftX++;						
						}
						break;
					case 'O':
						Os++;
						Ocol[col]++;
						if(col == row) {
							drightO++;
						} else if(col == (3-row)) {
							dleftO++;						
						}
						break;
					case 'T':
						Xs++;
						Os++;
						Xcol[col]++;
						Ocol[col]++;
						if(col == row) {
							drightX++;
							drightO++;
						} else if(col == (3-row)) {
							dleftX++;
							dleftO++;					
						}
						break;
					case '.':
						points++;
						break;		
				}
			}
			// Finished scanning column
			if(Xs == 4)	{
				stat = 1;	
			}
			if(Os == 4)	{
				stat = 2;	
			}
		}
		// Rows are checked, now check columns
		if(stat == 0) {
			if(Xcol[0] == 4 || Xcol[1] == 4 || Xcol[2] == 4 || Xcol[3] == 4) {
				stat = 1;			
			} else if(Ocol[0] == 4 || Ocol[1] == 4 || Ocol[2] == 4 || Ocol[3] == 4) {
				stat = 2;			
			}
		}
		// Check diagonals
		if(drightX == 4 || dleftX == 4) {
			stat = 1;		
		} else if(drightO == 4 || dleftO == 4) {
			stat = 2;		
		}
		// If no one won, check if it's a draw or not completed game
		if(stat == 0) {
			if(points == 0) {
				stat = 3;			
			} else {
				stat = 4;			
			}	
		}
		fscanf(iFile, "%c", &C);
		fprintf(oFile, "Case #%d: %s\n", i, stats[stat-1]);
	}
	fclose(iFile);
	fclose(oFile);
	return 0;
}
