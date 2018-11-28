#include <cstdio>
#include <cstdlib>
using namespace std;

int main(int argc, char **argv) {
	if (argc!=3) {
		printf("provide input and output file names as command line parameters\n");
	}
	FILE *fp_in, *fp_out;
	if ((fp_in=fopen(argv[1],"r"))==NULL) { printf("can't open file %s\n", argv[1]); exit(1); }
	if ((fp_out=fopen(argv[2],"w"))==NULL) { printf("can't open file %s\n", argv[2]); exit(1); }
	
	int num_cases;
	fscanf(fp_in, "%d\n", &num_cases);
	char str[4][8];
	int i, j;
	int x_won, o_won, draw;
	for (int test_case=1; test_case<=num_cases; test_case++) {
		for (i=0; i<4; i++) fscanf(fp_in, "%s\n", &(str[i][0]));
		
	//	printf("case %d\n", test_case);
	//	for (i=0; i<4; i++) printf("%s\n", str[i]);
		
		x_won = 0;
		o_won = 0;
		draw = 0;
		
		//check each row
		for (i=0; i<4; i++) {
			for (j=0; j<4; j++) if (!(str[i][j]=='X' || str[i][j]=='T')) break;
			if (j==4) {
				x_won = 1;
				goto bypass;
			}
			for (j=0; j<4; j++) if (!(str[i][j]=='O' || str[i][j]=='T')) break;
			if (j==4) {
				o_won = 1;
				goto bypass;
			}
		}
		
		//check each column
		for (i=0; i<4; i++) {
			for (j=0; j<4; j++) if (!(str[j][i]=='X' || str[j][i]=='T')) break;
			if (j==4) {
				x_won = 1;
				goto bypass;
			}
			for (j=0; j<4; j++) if (!(str[j][i]=='O' || str[j][i]=='T')) break;
			if (j==4) {
				o_won = 1;
				goto bypass;
			}
		}
		
		//check diagonals
		for (i=0; i<4; i++) if (!(str[i][i]=='X' || str[i][i]=='T')) break;
		if (i==4) {
			x_won = 1;
			goto bypass;
		}
		for (i=0; i<4; i++) if (!(str[i][i]=='O' || str[i][i]=='T')) break;
		if (i==4) {
			o_won = 1;
			goto bypass;
		}
		for (i=0; i<4; i++) if (!(str[i][3-i]=='X' || str[i][3-i]=='T')) break;
		if (i==4) {
			x_won = 1;
			goto bypass;
		}
		for (i=0; i<4; i++) if (!(str[i][3-i]=='O' || str[i][3-i]=='T')) break;
		if (i==4) {
			o_won = 1;
			goto bypass;
		}
		
		//if it gets here, no one won, check if all spots are taken
		for (i=0; i<4; i++) for (j=0; j<4; j++) if (str[i][j]=='.') goto bypass;
		if (i==4 && j==4) draw = 1;
		
		bypass:;
		
		fprintf(fp_out, "Case #%d: ", test_case);
		if (x_won) fprintf(fp_out, "X won\n");
		else if (o_won) fprintf(fp_out, "O won\n");
		else if (draw) fprintf(fp_out, "Draw\n");
		else fprintf(fp_out, "Game has not completed\n");
	}
	
	
	fclose(fp_in);
	fclose(fp_out);
	return 0;
}
