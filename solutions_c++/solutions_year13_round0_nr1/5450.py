#include <iostream>
#include <stdio.h>
using namespace std;

void printtable(char c[][4]){
	int i, j;
	for(i=0; i<4; ++i) {
		for(j=0; j<4; ++j) {
			printf("%c", c[i][j]);
		}
		
		//printf("\n");
	}
}

int main()
{
  int T = 0, xc, oc, i, j;
  char cell[4][4], tmp;
  bool t, d;
  
  scanf("%d", &T);
  for(int idx =1; idx <= T; idx++) {
  
	//read the table
	for(i=0; i<4; ++i) {
			scanf("%s", &cell[i]);
		
		//scanf("%c", &tmp);
	}
	
	//check rows
	d = false;
	for(i=0; i<4; ++i) {
		xc = oc = 0, t = false;
		for(j=0; j<4; ++j) {
			switch(cell[i][j]) {
				case 'X': ++xc; break;
				case 'O': ++oc; break;
				case 'T': t = true; break;
				case '.': d = true;
			}
		}
		
		//printtable(cell);
		
		if(xc == 4 || (xc == 3 && t == true)) {
			printf("Case #%d: X won\n", idx);
			goto NextCase;
		}
		
		if(oc == 4 || (oc == 3 && t == true)) {
			printf("Case #%d: O won\n", idx);
			goto NextCase;
		}
	}
	
	//check columns
	d = false;
	for(j=0; j<4; ++j) {
		xc = oc = 0, t = false;
		for(i=0; i<4; ++i) {
			switch(cell[i][j]) {
				case 'X': ++xc; break;
				case 'O': ++oc; break;
				case 'T': t = true; break;
				case '.': d = true;
			}
		}
		
		if(xc == 4 || (xc == 3 && t == true)) {
			printf("Case #%d: X won\n", idx);
			goto NextCase;
		}
		
		if(oc == 4 || (oc == 3 && t == true)) {
			printf("Case #%d: O won\n", idx);
			goto NextCase;
		}
	}
	
	//check diagonals
	xc = oc = 0, t = d = false;
	for(i=0; i<4; ++i) {
		switch(cell[i][i]) {
			case 'X': ++xc; break;
			case 'O': ++oc; break;
			case 'T': t = true; break;
			case '.': d = true;
		}
		
		if(xc == 4 || (xc == 3 && t == true)) {
			printf("Case #%d: X won\n", idx);
			goto NextCase;
		}
		
		if(oc == 4 || (oc == 3 && t == true)) {
			printf("Case #%d: O won\n", idx);
			goto NextCase;
		}
	}
	
	xc = oc = 0, t = d = false;
	for(i=0; i<4; ++i) {
		switch(cell[i][3-i]) {
			case 'X': ++xc; break;
			case 'O': ++oc; break;
			case 'T': t = true; break;
			case '.': d = true;
		}
		
		if(xc == 4 || (xc == 3 && t == true)) {
			printf("Case #%d: X won\n", idx);
			goto NextCase;
		}
		
		if(oc == 4 || (oc == 3 && t == true)) {
			printf("Case #%d: O won\n", idx);
			goto NextCase;
		}
	}
	
	
	if(d == true)
		printf("Case #%d: Game has not completed\n", idx);
	else
		printf("Case #%d: Draw\n", idx);
		
NextCase:
	scanf("%c", &tmp);
  }
}
   