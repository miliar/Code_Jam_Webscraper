#include <stdio.h>
#include <string.h>
#include <iostream>

using namespace std;

int main (void) {
	int n, c, i, size;
	char s[26], in[101];
	s[0] = 'y';
	s[1] = 'h';
	s[2] = 'e';
	s[3] = 's';
	s[4] = 'o';
	s[5] = 'c';
	s[6] = 'v';
	s[7] = 'x';
	s[8] = 'd';
	s[9] = 'u';
	s[10] = 'i';
	s[11] = 'g';
	s[12] = 'l';
	s[13] = 'b';
	s[14] = 'k';
	s[15] = 'r';
	s[16] = 'z';
	s[17] = 't';
	s[18] = 'n';
	s[19] = 'w';
	s[20] = 'j';
	s[21] = 'p';
	s[22] = 'f';
	s[23] = 'm';
	s[24] = 'a';
	s[25] = 'q';
	scanf ("%d\n", &n);
	for (c = 1; c <= n; c++) {
		cin.getline (in, 101);
		printf ("Case #%d: ", c);
		for (i = 0, size = strlen(in); i < size; i++) {
			if (in[i] == ' ')	putchar(' ');
			else	putchar(s[in[i]-'a']);
		}
		putchar ('\n');
	}
	return 0;
}
