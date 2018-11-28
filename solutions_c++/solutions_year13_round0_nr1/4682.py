#include <stdio.h>

FILE *in;
FILE *out;

char board[4][4];
int cases;
char vec[4];
char status;


char check_vec()
{
	char init;

	if(vec[0] != 'T') init = vec[0];
	else init = vec[1];

	for(int i=0; i<4; i++) {
		if( vec[i] != init && vec[i] != 'T' ) return '.';
	}

	return init;
}


int main()
{
	in = fopen("input", "r");
	out = fopen("output", "w");
	fscanf(in, "%d\n", &cases);
	
	for(int k=0; k<cases; k++) {
		for(int i=0; i<4; i++) {
			for(int j=0; j<4; j++) fscanf(in, "%c", &board[i][j]);
			fscanf(in, "\n");
		}
		fscanf(in, "\n");


		// Check for board status
		status = '.';

		for(int i=0; i<4; i++) {
			for(int j=0; j<4; j++) vec[j] = board[i][j];
			if(check_vec() == 'X' || check_vec() == 'O') status = check_vec();
		}
		
		for(int i=0; i<4; i++) {
			for(int j=0; j<4; j++) vec[j] = board[j][i];
			if(check_vec() == 'X' || check_vec() == 'O') status = check_vec();
		}

		for(int j=0; j<4; j++) vec[j] = board[j][j];
		if(check_vec() == 'X' || check_vec() == 'O') status = check_vec();

		for(int j=0; j<4; j++) vec[j] = board[j][3-j];
		if(check_vec() == 'X' || check_vec() == 'O') status = check_vec();

		// draw or empty check
		if(status == '.') {
			for(int i=0; i<4; i++) for(int j=0; j<4; j++) if(board[i][j] == '.') status = 'c';
		}


		// printing the solution
		if(status == 'X') fprintf(out, "Case #%d: X won\n", k+1);
		else if(status == 'O') fprintf(out, "Case #%d: O won\n", k+1);
		else if(status == 'c') fprintf(out, "Case #%d: Game has not completed\n", k+1);
		else fprintf(out, "Case #%d: Draw\n", k+1);
	}

	fclose(out);
	fclose(in);


	return 0;
}
