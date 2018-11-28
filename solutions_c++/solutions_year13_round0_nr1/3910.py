#include <algorithm>
#include <iostream>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string>

void main() {
	bool draw,tflag;
	int i,j,T,Trun = 1;
	int length,total,end;
	std::string input;
	std::cin >> T;
	while (Trun <= T) {
		draw = true, end = 0, total = 0, tflag = 0;
		char** d = new char*[4];
		for( i = 0; i < 4; i++ ) 
			d[i] = new char[4];
		for( i = 0; i < 4; i++ ) {
			std::cin >> input;
			length=input.length();
			char *p1 = new char[length+1];
			p1[length] = 0;
			memcpy(p1, input.c_str(), input.size());
			for( j = 0; j < length; j++ ) {
				if ( p1[j] == 'X' )
					d[i][j] = 1;
				else if ( p1[j] == 'O' )
					d[i][j] = -1;
				else if ( p1[j] == 'T' )
					d[i][j] = 2;
				else if ( p1[j] == '.')
					d[i][j] = 0;
				else
				d[i][j] = p1[j];
				// printf("%c\n",p1[j]);
			}
		}
		// for( i = 0; i < 4; i++ ) {
		// 	for( j = 0; j < 4; j++ )
		// 		printf("%c",d[i][j]);
		// 	printf("\n");
		// }
		for ( i = 0, total = 0, tflag = 0; i < length; i++ ) {
			if ( d[i][i] == 0 )
				draw = false;
			else if ( d[i][i] == 2 )
				tflag = true;
			else
				total += d[i][i];
		}
		if ( total == 4 || total == -4 || (( total == 3 || total == -3 ) && tflag ))
			end = total/abs(total);
		for ( i = 0, total = 0, tflag = 0; i < length; i++ ) {
			if ( d[i][3-i] == 0 )
				draw = false;
			else if ( d[i][3-i] == 2 )
				tflag = true;
			else
				total += d[i][3-i];
		}
		if ( total == 4 || total == -4 || (( total == 3 || total == -3 ) && tflag ))
			end = total/abs(total);
		if (!end)
			for ( i = 0; i < 4; i++ ) {
				for ( j = 0, total = 0, tflag = 0; j < length; j++ ) {
					if ( d[i][j] == 0 )
						draw = false;
					else if ( d[i][j] == 2 )
						tflag = true;
					else
						total += d[i][j];
				}
				if ( total == 4 || total == -4 || (( total == 3 || total == -3 ) && tflag )) {
					end = total/abs(total);
					break;
				}
			}
		if (!end)
			for ( i = 0; i < 4; i++ ) {
				for ( j = 0, total = 0, tflag = 0; j < length; j++ ) {
					if ( d[j][i] == 0 )
						draw = false;
					else if ( d[j][i] == 2 )
						tflag = true;
					else
						total += d[j][i];
				}
				if ( total == 4 || total == -4 || (( total == 3 || total == -3 ) && tflag )) {
					end = total/abs(total);	
					break;
				}
			}
		if (end == 1) 
			printf("Case #%d: X won\n", Trun++);
		else if (end == -1)
			printf("Case #%d: O won\n", Trun++);
		else if (!draw) 
			printf("Case #%d: Game has not completed\n", Trun++);
		else if (draw)
			printf("Case #%d: Draw\n", Trun++);
		else
			printf("Case #%d: error\n", Trun++);
		
		for( i = 0; i < 4; i++ )
			delete[] d[i];
		delete[] d;
	}
}

