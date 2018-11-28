//============================================================================
// Name        : ProblemA.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include<stdio.h>

char m[4][6];

int main() {
	bool flag;
	int x, o;
	int blank;
	int t;
	int i, j, k;
	scanf("%d", &t);
	for (i = 0; i < t; i++) {
		flag = false;
		for (j = 0; j < 4; j++) {
			scanf("%s", m[j]);
		}
		blank = 0;
		for (j = 0; j < 4; j++) {
			x = 0;
			o = 0;
			for (k = 0; k < 4; k++) {
				if (m[j][k] == 'X')
					x++;
				if (m[j][k] == 'O')
					o++;
				if (m[j][k] == 'T') {
					x++;
					o++;
				}
				if (m[j][k] == '.')
					blank++;
			}
			if (x == 4) {
				printf("Case #%d: X won\n",i+1);
				flag = true;
				break;
			} else if (o == 4) {
				printf("Case #%d: O won\n",i+1);
				flag = true;
				break;
			}
		}
		if (flag)
			continue;
		for (j = 0; j < 4; j++) {
			x = 0;
			o = 0;
			for (k = 0; k < 4; k++) {
				if (m[k][j] == 'X')
					x++;
				if (m[k][j] == 'O')
					o++;
				if (m[k][j] == 'T') {
					x++;
					o++;
				}
			}
			if (x == 4) {
				printf("Case #%d: X won\n",i+1);
				flag = true;
				break;
			} else if (o == 4) {
				printf("Case #%d: O won\n",i+1);
				flag = true;
				break;
			}
		}
		if (flag)	continue;
		x=0;
		o=0;
		for (j = 0; j < 4; j++) {

			if (m[j][j] == 'X')
				x++;
			if (m[j][j] == 'O')
				o++;
			if (m[j][j] == 'T') {
				x++;
				o++;
			}
		}
		if (x == 4) {
			printf("Case #%d: X won\n",i+1);
			flag = true;
			continue;
		} else if (o == 4) {
			printf("Case #%d: O won\n",i+1);
			flag = true;
			continue;
		}
		x=0;
		o=0;
		for (j = 0; j < 4; j++) {

			if (m[j][3-j] == 'X')
				x++;
			if (m[j][3-j] == 'O')
				o++;
			if (m[j][3-j] == 'T') {
				x++;
				o++;
			}
		}
		if (x == 4) {
			printf("Case #%d: X won\n",i+1);
			flag = true;
			continue;
		} else if (o == 4) {
			printf("Case #%d: O won\n",i+1);
			flag = true;
			continue;
		}
		if(blank==0)	printf("Case #%d: Draw\n",i+1);
		else printf("Case #%d: Game has not completed\n",i+1);

	}
	return 0;
}
