#include <vector>
#include <algorithm>
#include <sstream>
#include <deque>
#include <string.h>
#include <stdio.h>
#include <iostream>
#include <map>
#include <set>

using namespace std;

char m[4][4];

int check(char c, int i, int j, int dx, int dy){

	int incx, incy;
	incx = dx;
	incy = dy;

	for (int ii = 0; ii < 3; ii++){
		
		if ((i+dx) < 4 and (i+dx) >= 0 and (j+dy) < 4 and (j+dy) >= 0){
			if (m[i+dx][j+dy] != c and m[i+dx][j+dy] != 'T')
				return 0;
				
			dx += incx;
			dy += incy;
		}
		else return 0;
	}
	return 1;
}


int main(){
	
	char s[12], c;
	int t, flag;
	
	scanf("%d\n", &t);
	
	for (int i = 0; i < t; i++){
		
		for (int ii = 0; ii < 4; ii++){
			scanf("%s", s);
			m[ii][0] = s[0]; m[ii][1] = s[1]; m[ii][2] = s[2]; m[ii][3] = s[3];
		}
		
		flag = 0;
		for (int ii = 0; ii < 4 and !flag; ii++){
			for (int j = 0; j < 4 and !flag; j++){
				c = m[ii][j];
				if (m[ii][j] != '.'){
					flag = check(m[ii][j], ii, j, -1, -1);
					if (flag)break;
					flag = check(m[ii][j], ii, j, -1, 0);
					if (flag)break;
					flag = check(m[ii][j], ii, j, -1, 1);
					if (flag)break;
					flag = check(m[ii][j], ii, j, 0, -1);
					if (flag)break;
					flag = check(m[ii][j], ii, j, 0, 1);
					if (flag)break;
					flag = check(m[ii][j], ii, j, 1, -1);
					if (flag)break;
					flag = check(m[ii][j], ii, j, 1, 0);
					if (flag)break;
					flag = check(m[ii][j], ii, j, 1, 1);
				}
			}
		}
		
		if (flag){
			if (c == 'X')cout << "Case #" << i+1 << ":" << " X won" << endl;
			else{
				cout << "Case #" << i+1 << ":" << " O won" << endl;
			}
		}
		else{
			for (int ii = 0; ii < 4 and !flag; ii++){
				for (int j = 0; j < 4 and !flag; j++){
					if (m[ii][j] == '.')flag = 1;
				}
			}
			if (flag)cout << "Case #" << i+1 << ":" << " Game has not completed" << endl;
			else{
				cout << "Case #" << i+1 << ":" << " Draw" << endl;
			}
		}
		
	}

	return 0;
}