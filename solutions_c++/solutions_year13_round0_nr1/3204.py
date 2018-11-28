#include <stdlib.h>
#include <stdio.h>

unsigned map(char c) {
	switch (c) {
		case '.' : return 0;
		case 'X' : return 0x0001;
		case 'O' : return 0x0100;
		case 'T' : return 0x0101;
	};
	return 0;	// error, actually
};


int solve(int ctry){
	unsigned tab[4][4] = {};
	for (int i = 0; i < 4; i++) {
		scanf("\n");
		for (int j = 0; j < 4; j++) {
			char c;
			scanf("%c", &c);
			tab[i][j] = map(c);
//			printf("%c", c);
		};
	};
		
	
	bool finished = true;
	for (int i = 0; i < 4; i++)
		for (int j = 0; j < 4; j++)
			if (!tab[i][j])
				finished = false;
	
	// win?
	unsigned rez = 0;
	for (int i = 0; i < 4; i++) {
		for (int j = 0; j < 4; j++)
			rez += tab[i][j];
		rez &= ~0x0303;	// resetting lsbs
		for (int j = 0; j < 4; j++)
			rez += tab[j][i];
		rez &= ~0x0303;	
	};
	// and the diagonals
	for (int i = 0; i < 4; i++)
		rez += tab[i][i];
	rez &= ~0x0303;	// resetting lsbs
	for (int i = 0; i < 4; i++)
		rez += tab[i][3-i];
	rez &= ~0x0303;	
	
	const char* txt = "Game has not completed";
	if      (rez & 0x00FC) 
		txt = "X won";
	else if (rez & 0xFC00)
		txt = "O won";
	else if (finished)
		txt = "Draw";
	
	printf("Case #%d: %s\n", ctry, txt);
};


int main(){

	if (freopen("test.in", "rt", stdin)){
//		freopen("A-large-practice.out", "wt", stdout);
		int tries = 0;
		scanf("%d", &tries);
		for (int ctry = 1; ctry <= tries; ctry++){
			solve(ctry);
		};
	};
	if (freopen("A-small-attempt1.in", "rt", stdin)){
		freopen("A-small-attempt1.out", "wt", stdout);
		int tries = 0;
		scanf("%d", &tries);
		for (int ctry = 1; ctry <= tries; ctry++){
			solve(ctry);
		};
	};
	if (freopen("A-large.in", "rt", stdin)){
		freopen("A-large.out", "wt", stdout);
		int tries = 0;
		scanf("%d", &tries);
		for (int ctry = 1; ctry <= tries; ctry++){
			solve(ctry);
		};
	};
	return 0;
};