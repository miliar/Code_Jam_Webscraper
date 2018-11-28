//============================================================================
// Name        : 190.cpp
// Author      :
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================
#include <vector>
#include <iostream>
#include <string.h>
#include <stdio.h>

using namespace std;

int main() {
	int l, d, n;
	static char words[5001][16];
	static char line[10000];
	static char c[16][10000];
	scanf("%d %d %d", &l, &d, &n);
	for (int i = 0; i < d; i++)
		scanf("%s", words[i]);

	scanf("\n");

	for (int caso = 1; caso <= n; caso++) {
		scanf("%s", line);
		int t = strlen(line);
		int pos = 0;
		int count = 0;
		for (int i = 0; i < t; i++) {
			if (line[i] == '(') {
				int p = 0;
				while (line[++i] != ')') {
					c[pos][p++] = line[i];
				}
				c[pos++][p] = 0;
			} else {
				c[pos][0] = line[i];
				c[pos++][1] = 0;
			}
		}


		/*for (int i = 0; i < pos; i++)
			printf("%s\n",c[i]);

		printf("\n");
*/
		for (int i = 0; i < d; i++) {
			//printf(">> %s\n", words[i] );
			int j = 0;
			for (j = 0; j < l && strchr(c[j], words[i][j]); j++)
				;
			if (j == l)
				count++;
		}
		printf("Case #%d: %d\n", caso, count);
	}
}
