#include <stdio.h>

int state[4][4] = {0};

FILE * out;

bool horizontal(int currentCase) {
		//horiz
		for(int i=0; i < 4; i++) {
			bool win = true;
			char line[4] = {0};
			//X
			for(int j=0; j < 4; j++) {
				if(state[i][j] != 'X' && state[i][j] != 'T') {
					win = false;
				}
			}
			if(win) {
				fprintf(out, "Case #%d: X won", currentCase);
				return true;
			}

			//O
			win = true;
			for(int j=0; j < 4; j++) {
				if(state[i][j] != 'O' && state[i][j] != 'T') {
					win = false;
				}
			}
			if(win) {
				fprintf(out, "Case #%d: O won", currentCase);
				return true;
			}
		}
}

bool vertical(int currentCase) {
		//horiz
		for(int i=0; i < 4; i++) {
			bool win = true;
			char line[4] = {0};
			//X
			for(int j=0; j < 4; j++) {
				if(state[j][i] != 'X' && state[j][i] != 'T') {
					win = false;
				}
			}
			if(win) {
				fprintf(out, "Case #%d: X won", currentCase);
				return true;
			}

			//O
			win = true;
			for(int j=0; j < 4; j++) {
				if(state[j][i] != 'O' && state[j][i] != 'T') {
					win = false;
				}
			}
			if(win) {
				fprintf(out, "Case #%d: O won", currentCase);
				return true;
			}
		}
}


bool diagonal1(int currentCase) {
	char winstate[4] = {0};
	for(int i=0; i < 4; i++) {
		winstate[i] = state[i][i];
	}
	//X
	bool win = true;
	for(int i=0; i < 4; i++) {
		if (winstate[i] != 'X' && winstate[i] != 'T') {
			win = false;
		}
	}
	if(win) {
		fprintf(out, "Case #%d: X won", currentCase);
		return true;
	}

	//O
	win = true;
	for(int i=0; i < 4; i++) {
		if (winstate[i] != 'O' && winstate[i] != 'T') {
			win = false;
		}
	}
	if(win) {
		fprintf(out, "Case #%d: O won", currentCase);
		return true;
	}
}

bool diagonal2(int currentCase) {
	char winstate[4] = {0};
	for(int i=0; i < 4; i++) {
		winstate[i] = state[i][3-i];
	}
	//X
	bool win = true;
	for(int i=0; i < 4; i++) {
		if (winstate[i] != 'X' && winstate[i] != 'T') {
			win = false;
		}
	}
	if(win) {
		fprintf(out, "Case #%d: X won", currentCase);
		return true;
	}

	//O
	win = true;
	for(int i=0; i < 4; i++) {
		if (winstate[i] != 'O' && winstate[i] != 'T') {
			win = false;
		}
	}
	if(win) {
		fprintf(out, "Case #%d: O won", currentCase);
		return true;
	}
}


int main(int argv, char** argc) {
	FILE * file = fopen("C:\\Users\\Aaron\\in.txt", "r");
	out = fopen("C:\\Users\\Aaron\\out.txt", "w");

	int cases = 0;
	char buff[512];

	fscanf(file, "%d\n", &cases);

	for(int currentCase=1 ; currentCase <= cases; currentCase++) {
		bool win = false;
		bool hasDot = false;
		for(int i=0; i < 4; i++) {
			for(int j=0; j < 4; j++) {
				state[i][j] = fgetc(file);
				if(state[i][j] == '.') {
					hasDot = true;
				}
			}
			fgetc(file);
		}
		win = win || horizontal(currentCase);
		win = win || vertical(currentCase);
		win = win || diagonal1(currentCase);
		win = win || diagonal2(currentCase);
		if(!win) {
			if(hasDot) {
				fprintf(out, "Case #%d: Game has not completed", currentCase);
			}
			else {
				fprintf(out, "Case #%d: Draw", currentCase);
			}
		}
		fprintf(out, "\n");


		fgets(buff, sizeof(buff), file);
	}
	fclose(out);

	return 0;
}