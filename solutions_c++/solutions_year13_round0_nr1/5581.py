//
//  main.cpp
//  round1_1
//
//  Created by wonhee jang on 13. 4. 13..
//  Copyright (c) 2013년 vanillabreeze. All rights reserved.
//

#include <iostream>

const char* check_flat(char form[4][4]) {
	bool x_won = false;
	bool o_won = false;
	int empty = 0;
	char first;
	int count;
	
	for(int i = 0; i < 4; i++) {
		
		first = form[i][0];
		count = 0;
		for(int j = 0; j < 4; j++) {
			char node = form[i][j];
			if(node == '.') {
				empty++;
			} else if(first == 'T') {
				count++;
				first = node;
			} if(node == 'T')
				count++;
			else if(first == node)
				count++;
		}
		if(count == 4) {
			if(first == 'X')
				x_won = true;
			else if(first == 'O')
				o_won = true;
		}
		
		
		first = form[0][i];
		count = 0;
		for(int j = 0; j < 4; j++) {
			char node = form[j][i];
			if(first == '.') {
			} else if(first == 'T') {
				count++;
				first = node;
			} if(node == 'T')
				count++;
			else if(first == node)
				count++;
		}
		if(count == 4) {
			if(first == 'X')
				x_won = true;
			else if(first == 'O')
				o_won = true;
		}
	}
	
	int x = 0;
	int y = 0;
	first = form[x][y];
	count = 0;
	for(int i = 0; i < 4; i++) {
		char node = form[x][y];
		if(first == '.') {
		} else if(first == 'T') {
			count++;
			first = node;
		} if(node == 'T')
			count++;
		else if(first == node)
			count++;
		x++;
		y++;
	}
	
	if(count == 4) {
		if(first == 'X')
			x_won = true;
		else if(first == 'O')
			o_won = true;
	}
	
	x=3;
	y=0;
	first = form[x][y];
	count = 0;
	for(int i = 0; i < 4; i++) {
		char node = form[x][y];
		if(first == '.') {
		} else if(first == 'T') {
			count++;
			first = node;
		} if(node == 'T')
			count++;
		else if(first == node)
			count++;
		
		x--;
		y++;
	}
	if(count == 4) {
		if(first == 'X')
			x_won = true;
		else if(first == 'O')
			o_won = true;
	}
	
	if(!x_won && !o_won) {
		if(empty == 0)
			return "Draw";
		return "Game has not completed";
	} else if(x_won && o_won)
		return "Draw";
	else if(x_won)
		return "X won";
	else
		return "O won";
};

int main(int argc, const char * argv[])
{

	FILE* f = fopen(argv[1], "r");
	int len = 0;
	fscanf(f, "%d", &len);
	fseek(f, SEEK_CUR, 1);
	for(int i = 0; i < len; i++) {
		char form[4][4] = {NULL,};
		for(int j = 0; j < 4; j++) {
			fread(form[j], sizeof(char), 4, f);
			fseek(f, SEEK_CUR, 1);
		}
		printf("Case #%i: %s\n", i+1, check_flat(form));
		fseek(f, SEEK_CUR, 1);
	}
	fclose(f);
	
    return 0;
}

