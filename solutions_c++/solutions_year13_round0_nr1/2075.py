//
//  main.cpp
//  Tic-Tac-Toe-Tomek
//
//  Created by dmp on 4/13/13.
//  Copyright (c) 2013 dmp. All rights reserved.
//

#include <iostream>
#include <vector>
#include <map>
#include <list>

using namespace std;

#define QuickCheckCompleted(C) if(C == '.') { printf("Game has not completed"); return; } 

void processCase()
{
	char field[4][4];
	int OCount[4] = {0}, XCount[4] = {0};
	int dotCount = 0;
	
	for(int i = 0; i < 4; i++)
	{
		string s;
		cin >> s;
		
		for(int j = 0; j < 4; j++)
			field[i][j] = s[j];
	}
	
	for(int i = 0; i < 4; i++)
	{
		XCount[0] = XCount[1] = OCount[0] = OCount[1] = 0;
		
		for(int j = 0; j < 4; j++)
		{
			if( field[i][j] == 'T') {
				OCount[0]++;
				XCount[0]++;
			}

			if( field[j][i] == 'T') {
				OCount[1]++;
				XCount[1]++;
			}
			
			if( field[i][j] == 'X') XCount[0]++;
			if( field[i][j] == 'O') OCount[0]++;

			if( field[j][i] == 'X') XCount[1]++;
			if( field[j][i] == 'O') OCount[1]++;
			
			if(field[i][j] == '.') dotCount++;
		}
		
		if( (XCount[0] == 4) || (XCount[1] == 4)) { printf("X won"); return; }
		if( (OCount[0] == 4) || (OCount[1] == 4)) { printf("O won"); return; }
		
		
		if( field[i][i] == 'T') {
			OCount[2]++;
			XCount[2]++;
		}
		
		if( field[i][3 - i] == 'T') {
			OCount[3]++;
			XCount[3]++;
		}
		
		if( field[i][i] == 'X') XCount[2]++;
		if( field[i][i] == 'O') OCount[2]++;

		if( field[i][3 - i] == 'X') XCount[3]++;
		if( field[i][3 - i] == 'O') OCount[3]++;
	}
	
	for(int i = 2; i < 4; i++)
	{
		if(XCount[i] == 4) { printf("X won"); return; }
		if(OCount[i] == 4) { printf("O won"); return; }
	}
	
	if(dotCount == 0) printf("Draw");
	else printf("Game has not completed");
}

int main(int argc, const char * argv[])
{
	int T;
	cin >> T;
		
	for (int i = 0; i < T; i++) {
		printf("Case #%d: ", i + 1);
		processCase();
		printf("\n");
	}
	
    return 0;
}
