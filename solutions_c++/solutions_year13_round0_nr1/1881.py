#include <stdio.h>
#include <iostream>

using namespace std;

char M[4][5];

int checkR (int r) {
	int cx = 0, ct = 0, c0 = 0, i;
	for (i = 0; i < 4; i++) {
		if (M[r][i] == 'X')	cx++;
		else if (M[r][i] == 'O')	c0++;
		else if (M[r][i] == 'T')	ct++;
	}
	if (cx+ct == 4)	return 1;
	if (c0+ct == 4)	return -1;
	return 0;
}

int checkC (int c) {
	int cx = 0, ct = 0, c0 = 0, i;	
	for (i = 0; i < 4; i++) {
		if (M[i][c] == 'X')	cx++;
		else if (M[i][c] == 'O')	c0++;
		else if (M[i][c] == 'T')	ct++;
	}
	if (cx+ct == 4)	return 1;
	if (c0+ct == 4)	return -1;
	return 0;
}

int checkD (void) {
	int cx = 0, ct = 0, c0 = 0, i;
	for (i = 0; i < 4; i++) {
		if (M[i][i] == 'X')	cx++;
		else if (M[i][i] == 'O')	c0++;
		else if (M[i][i] == 'T')	ct++;
	}
	if (cx+ct == 4)	return 1;
	if (c0+ct == 4)	return -1;
	cx = c0 = ct = 0;
	for (i = 0; i < 4; i++) {
		if (M[i][3-i] == 'X')	cx++;
		else if (M[i][3-i] == 'O')	c0++;
		else if (M[i][3-i] == 'T')	ct++;
	}
	if (cx+ct == 4)	return 1;
	if (c0+ct == 4)	return -1;
	return 0;
}
int main (void) {
	int T, c, i, j, ans;
	char line[10];
	cin.getline (line, 10);
	sscanf (line, "%d", &T);
	for (c = 0; c < T; c++) {
		cout << "Case #" << c+1 << ": ";
		for (i = 0; i < 4; i++)	cin.getline (M[i], 5);
		cin.getline(line, 10);
		ans = 0;
		for (i = 0; i < 4; i++)
			if (ans = checkR(i))	break;
		if (!ans)
			for (i = 0; i < 4; i++)
				if (ans = checkC(i))	break;
		if (!ans)
			ans = checkD();
		if (!ans) {
			for (i = 0; i < 4; i++)
				for (j = 0; j < 4; j++)
					if (M[i][j] == '.')	ans = -2;
			if(ans == -2)	cout << "Game has not completed\n";
			else	cout << "Draw\n";
		} else
			if (ans == 1)	cout << "X won\n";
			else	cout << "O won\n";
	}
	return 0;
}
