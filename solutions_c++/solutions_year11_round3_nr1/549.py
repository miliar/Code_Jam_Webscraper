// codejam7.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream in("in.txt");
	ofstream out("out.txt");
	int T;
	in >> T;
	for(int t = 0; t < T; t++){
		int R, C;
		char pic[50][50];
		in >> R >> C;
		for(int r = 0; r < R; r++){
			string str;
			in >> str;
			for(int c = 0; c < C; c++)
				pic[r][c] = str[c];
		}
		for(int r = 0; r < R - 1; r++)
			for(int c = 0; c < C - 1; c++){
				if(pic[r][c] == '#'){
					if(pic[r + 1][c] == '#' && pic[r][c + 1] == '#' 
						&& pic[r+1][c+1] == '#'){
						pic[r][c] = '/';
						pic[r+1][c] = '\\';
						pic[r][c+1] = '\\';
						pic[r+1][c+1] = '/';
					}
				}
			}
		bool canSolve = true;
		for(int r = 0; r < R; r++)
			for(int c = 0; c < C; c++)
				if(pic[r][c] == '#')canSolve = false;
		if(!canSolve)out << "Case #" << t + 1 << ":" << endl << "Impossible" << endl;
		else{
			out << "Case #" << t + 1 << ":" << endl;
			for(int r = 0; r < R; r++){
				for(int c = 0; c < C; c++)
					out << pic[r][c];
				out << endl;
			}
		}
	}
	return 0;
}