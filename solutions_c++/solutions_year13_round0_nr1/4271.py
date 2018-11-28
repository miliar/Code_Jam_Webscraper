#include <stdio.h>

char s[5][5];

const int OWIN = 0;
const int XWIN = 1;
const int DRAW = 2;
const int NCOM = 3;


int run()
{
	int i,j;
	for (i = 0; i < 4; i++) {
		scanf("%s",s[i]);
	}
	// ------
	int Xwin = 0, Owin = 0;
	for (i = 0; i < 4; i++) {
		Xwin = 0, Owin = 0;
		for (j = 0; j < 4; j++) {
			if (s[i][j] == 'X'||s[i][j] == 'T') {
				Xwin++;
			}
			if (s[i][j] == 'O'||s[i][j] == 'T'){
				Owin++;
			}
		}
		if (Owin == 4) {
//			puts("1");
			return OWIN;
		}
		if (Xwin ==  4){
//			puts("2");
			return XWIN;
		}
	}
	
	//||
//	printf("%d %d\n",Owin,Xwin);
	for (i = 0; i < 4; i++) {
		Xwin = 0, Owin = 0;
	//printf("%d %d\n",Owin,Xwin);
		for (j = 0; j < 4; j++) {
			if (s[j][i] == 'X'||s[j][i] == 'T') {
				Xwin++;
			}
			if (s[j][i] == 'O'||s[j][i] == 'T'){
				Owin++;
			}
		}
		if (Owin == 4) {
	///		puts("3");
			return OWIN;
		}
		if (Xwin ==  4){
		///	puts("4");
			return XWIN;
		}
	}
	//  \
	Xwin = 0;
	Owin = 0;
	//printf("%d %d\n",Owin,Xwin);

	for (Xwin=0,Owin=0,i = 0; i < 4; i++) {
		if (s[i][i] == 'X' || s[i][i] == 'T') {
			Xwin++;
		//	puts("**");
		}
		if (s[i][i] == 'O' || s[i][i] == 'T') {
			Owin++;
		}
	}
//	printf("%d %d\n",Owin,Xwin);
	if (Owin == 4) {
		///	puts("5");
			return OWIN;
	}
		if (Xwin == 4){
			///puts("6");
			return XWIN;
		}
	
	// /
	for (Xwin = 0, Owin = 0,i = 0; i < 4; i++) {
		if (s[i][4-i-1] == 'X' || s[i][4-i-1] == 'T') {
			Xwin++;
		}
		if (s[i][4-i-1] == 'O' || s[i][4-i-1] == 'T') {
			Owin++;
		}
	}
		if (Owin == 4) {
			///puts("7");
			return OWIN;
		}
		if (Xwin == 4){
			///puts("8");
			return XWIN;
		}
	
	
	for (i = 0; i < 4; i++) {
		for (j = 0; j < 4; j++) {
			if (s[i][j] == '.') {
				///puts("9");
				return NCOM;			
			}
		}
	}	
	
///	puts("10");
	return DRAW;
}
int main(int argc, char *argv[]) {
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int T;
	scanf("%d",&T);
	int k = 0;
	while (T--) {
		int ans = run();
		printf("Case #%d: ",++k);	
		if (ans == OWIN) {
			printf("O won\n");
		}
		else if (ans == XWIN) {
			printf("X won\n");
		}
		else if (ans == DRAW) {
			printf("Draw\n");
		}
		else {
			printf("Game has not completed\n");
		}
	}
	return 0;
}