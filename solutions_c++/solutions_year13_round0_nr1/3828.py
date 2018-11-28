#include <iostream>
#include <stdio.h>

/*
Input 
 	
Output 
 
6
XXXT
....
OO..
....

XOXT
XXOO
OXOX
XXOO

XOX.
OX..
....
....

OOXX
OXXX
OX.T
O..O

XXXO
..O.
.O..
T...

OXXX
XO..
..O.
...O

Case #1: X won
Case #2: Draw
Case #3: Game has not completed
Case #4: O won
Case #5: O won
Case #6: O won

*/
using namespace std;

int caseNum;
char str[6];
char result[6];
char result_row;

int main(){
	//0:아직 1:진행중 2:X 3:O 
	int print_num;
	int row_x;

	cin >> caseNum;

	for(int i = 1; i <= caseNum; ++i){
		print_num = 0;
		row_x = 3;
		memset(result, 127, sizeof(char)*6);

		for(int e = 0; e < 4; ++e){
			result_row = 127;
			scanf("%s", &str);
			if(print_num == 2 || print_num == 3) continue;
			for(int ee = 0; ee < 4; ++ee){
				if(str[ee] == 'T') continue;
				if(e == ee){
					result[4] = result[4] & str[ee];
				}else if(row_x == ee){
					result[5] = result[5] & str[ee];
				}
				if(str[ee] == '.') print_num = 1;

				result[ee] = result[ee] & str[ee];
				result_row = result_row & str[ee];
			}
			if(result_row == 'X'){
				print_num = 2;
			}else if(result_row == 'O'){
				print_num = 3;
			}
			--row_x;
		}
		if(print_num == 0 || print_num == 1){
			for(int k = 0; k < 6; ++k){
				if(result[k] == 'X'){
					print_num = 2;
					break;
				}else if(result[k] == 'O'){
					print_num = 3;
					break;
				}
			}
		}
		
		switch(print_num){
		case 0 :
			printf("Case #%d: Draw\n", i);
			break;
		case 1 :
			printf("Case #%d: Game has not completed\n", i);
			break;
		case 2 :
			printf("Case #%d: X won\n", i);
			break;
		case 3 :
			printf("Case #%d: O won\n", i);
			break;
		}
	}


	return 0;
}