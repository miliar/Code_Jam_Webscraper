#include<stdio.h>

char M[40][40];
int t;

inline bool Valid (char a, char b, char c, char d, char fr) {
	int cntchr = 0, cntt = 0;
	cntchr += a == fr;
	cntchr += b == fr;
	cntchr += c == fr;
	cntchr += d == fr;
	cntt += a == 'T';
	cntt += b == 'T';
	cntt += c == 'T';
	cntt += d == 'T';
	
	return (cntchr == 4) or (cntchr == 3 and cntt == 1);
}

bool CheckFor(char fr) {
	return 		Valid (M[0][0], M[0][1], M[0][2], M[0][3], fr)
			or	Valid (M[1][0], M[1][1], M[1][2], M[1][3], fr)
			or	Valid (M[2][0], M[2][1], M[2][2], M[2][3], fr)
			or	Valid (M[3][0], M[3][1], M[3][2], M[3][3], fr)
			
			or	Valid (M[0][0], M[1][0], M[2][0], M[3][0], fr)
			or	Valid (M[0][1], M[1][1], M[2][1], M[3][1], fr)
			or	Valid (M[0][2], M[1][2], M[2][2], M[3][2], fr)
			or	Valid (M[0][3], M[1][3], M[2][3], M[3][3], fr)
			
			or	Valid (M[0][0], M[1][1], M[2][2], M[3][3], fr)
			or	Valid (M[3][0], M[2][1], M[1][2], M[0][3], fr);
}

bool CheckForDot () {
	for (int i = 0; i < 16; i ++)
		if (M[i/4][i%4] == '.')
			return true;
			
	return false;
}

int main() {
	scanf ("%d", &t);
	int caze = 0;
	while (t --) {
		caze ++;
		
		for (int i = 0; i < 4; i ++)
			scanf ("%s", M[i]);
		
		if (CheckFor ('X'))
			printf ("Case #%d: X won\n", caze);
		else if (CheckFor ('O'))
			printf ("Case #%d: O won\n", caze);
		else if (CheckForDot ())
			printf ("Case #%d: Game has not completed\n", caze);
		else
			printf ("Case #%d: Draw\n", caze);
		
	}
	return 0;
}
