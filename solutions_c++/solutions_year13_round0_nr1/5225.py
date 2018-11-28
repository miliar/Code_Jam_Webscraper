// next.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include "tclass.h"
#include <vector>
#include <string>
#include "Windows.h"



void printX(int i) {
	std::cout << "Case #" << i+1 << ": X won" << std::endl;
}

void printO(int i) {
	std::cout << "Case #" << i+1 << ": O won" << std::endl;
}

void printDraw(int i) {
	std::cout << "Case #" << i+1 << ": Draw" << std::endl;
}

void printIncomplete(int i) {
	std::cout << "Case #" << i+1 << ": Game has not completed" << std::endl;
}

void increment(char ch, int &x, int &o) {
	switch (ch) {
		case 'X':
			x++;
			break;
		case 'O':
			o++;
			break;
		case 'T':
			x++;
			o++;
			break;
	}
}

int _tmain(int argc, _TCHAR* argv[])
{
	int T = 0;
	std::cin >> T;
	//Sleep(10*1000);
	for (int t = 0; t < T; ++t) {
		char arr[4][4];
		bool oneEmpty = false;
		for (int i = 0; i < 4; ++i) {
			for (int j = 0; j < 4; ++j) {
				char ch;
				std::cin >> ch;
				arr[i][j] = ch;
				if (ch == '.')
					oneEmpty = true;
			}
		}
		// Check Rows
		bool done = false;
		int x = 0;
		int o = 0;
		for (int i = 0; i < 4; ++i) {
			x = o = 0;
			for (int j = 0; j < 4; ++j) 
				increment(arr[i][j], x, o);
			if (x == 4 || o == 4) {
				done  = true;
				break;
			}
		}
		
		if (false == done) {
			for (int i = 0; i < 4; ++i) {
				x = o = 0;
				for (int j = 0; j < 4; ++j)
					increment(arr[j][i], x, o);
				if (x == 4 || o == 4) {
					done  = true;
					break;
				}
			}
		}
		
		if (!done) {
			x = o = 0;
			for (int i = 0; i < 4; ++i) 
				increment(arr[i][i], x, o);
			if (x == 4 || o == 4) 
				done  = true;
		}
		if (!done) {
			x = o = 0;
			increment(arr[3][0], x, o);
			increment(arr[0][3], x, o);
			increment(arr[1][2], x, o);
			increment(arr[2][1], x, o);
			if (x == 4 || o == 4) 
				done  = true;
		}

		if (4 == x)
			printX(t);
		else if (4 == o)
			printO(t);
		else if (oneEmpty == true)
			printIncomplete(t);
		else 
			printDraw(t);

	}
}

