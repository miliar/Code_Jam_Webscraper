#include <iostream>
#include <queue>
#include <vector>
#include <string>
#include <stdio.h>
#include <math.h>
#include <algorithm>
using namespace std;

bool game_completed;


bool won(char matrix[4][4], char X){
	bool ans = false;
	//printf("Rows\n");
	for (int i=0; i<4; i++) {
		int count = 0;
		for (int j=0; j<4; j++) {
			
			
			if (matrix[i][j] == 'T' || matrix[i][j] == X) {
				count++;
			}
			else {
				break;
			}
		}
		if (count ==4) {
			ans = true;
			break;
		}
	}
	if (ans == true) {
		return true;
	}
	//printf("Columns\n");
	/// now check rows
	ans = false;
	
	for (int i=0; i<4; i++) {
		int count = 0;
		for (int j=0; j<4; j++) {
			
			if (matrix[j][i] == 'T' || matrix[j][i] == X) {
				count++;
			}
			else {
				ans = false;
				break;
			}
		}
		if (count ==4) {
			ans = true;
			break;
		}
	}
	if (ans == true) {
		return true;
	}
	
	ans = true;
	//printf("Diagonal1\n");
	/// now check diaganols
	for (int j=0; j<4; j++) {
		int count = 0;
		if (matrix[j][j] == 'T' || matrix[j][j] == X) {
			count++;
		}
		else {
			ans = false;
			break;
		}
		
	}
	if (ans == true) {
		return true;
	}
	
	ans = true;
	//printf("Diagonal2\n");
	/// now check diaganols
	for (int j=0; j<4; j++) {
		if (matrix[j][3-j] == 'T' || matrix[j][3-j] == X) {
		}
		else {
			ans = false;
			break;
		}
		
	}
	if (ans == true) {
		return true;
	}
	return false;
	
}

int main ()
{
	int no_testcases;
	scanf("%d", &no_testcases);
	
	
	for (int i=0; i<no_testcases; i++) {
		char c;
		
		char matrix[4][4];
		
		
		game_completed = true;
		
		scanf("%c",&c);
		for (int k=0; k<4; k++) {
			for (int j=0; j<4; j++) {
				scanf("%c",&c);
				matrix[k][j] = c;
				if (matrix[k][j] == '.') {
					game_completed = false;
				}
			}
			scanf("%c",&c);
		}
		
		if (won(matrix,'X')) {
			printf("Case #%d: X won\n",i+1);
			continue;
		}
		if (won(matrix,'O')) {
			printf("Case #%d: O won\n",i+1);
			continue;
		}
		if (game_completed == false) {
			printf("Case #%d: Game has not completed\n",i+1);
			continue;
		}
		printf("Case #%d: Draw\n",i+1);
		
		
		
	}
	
	return 0;
}