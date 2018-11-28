#include <iostream>
#include <stdio.h>
#include <math.h>
using namespace std;

char G [5][5];

bool Won (char c) {
	int P, T, ans = 0;
	
	for (int i = 0; i < 4; i++) {
			P = 0;
			T = 0;
			
			for (int j = 0; j < 4; j++) {
				if (G [i][j] == c)
					P++;
				if (G [i][j] == 'T')
					T++;
			}
			
			if ((P == 4) || (P == 3 && T == 1))
				ans |= 1;
	}
	
	for (int j = 0; j < 4; j++) {
			P = 0;
			T = 0;
			
			for (int i = 0; i < 4; i++) {
				if (G [i][j] == c)
					P++;
				if (G [i][j] == 'T')
					T++;
			}
			
			if ((P == 4) || (P == 3 && T == 1))
				ans |= 1;
	}
	
	P = 0;
	T = 0;
	
	for (int i = 0; i < 4; i++) {
		if (G [i][i] == c)
			P++;
		if (G [i][i] == 'T')
			T++;
	}
	
	if ((P == 4) || (P == 3 && T == 1))
		ans |= 1;
		
	P = 0;
	T = 0;
	
	for (int i = 0; i < 4; i++) {
		if (G [3 - i][i] == c)
			P++;
		if (G [3- i][i] == 'T')
			T++;
	}
	
	if ((P == 4) || (P == 3 && T == 1))
		ans |= 1;
	
	return ans;
}

bool isCompleted () {
	for (int i = 0; i < 4; i++) {
		for (int j = 0; j < 4; j++) {
			if (G [i][j] == '.')
				return false;
		}
	}
	return true;
}

int main () {
	int T;

	scanf ("%d", &T);
	
	for (int tc = 1; tc <= T; tc++) {
	
		for (int i = 0; i < 4; i++)
			scanf ("%s", G [i]);
		
		if (Won ('X'))
			printf ("Case #%d: X won\n", tc);
		
		else if (Won ('O'))
			printf ("Case #%d: O won\n", tc);
			
		else if (!isCompleted ())
			printf ("Case #%d: Game has not completed\n", tc);
			
		else
			printf ("Case #%d: Draw\n", tc);
	}
	
	return 0;
}
