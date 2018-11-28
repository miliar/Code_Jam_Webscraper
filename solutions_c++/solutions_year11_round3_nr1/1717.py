/* -*- Mode: C; indent-tabs-mode: t; c-basic-offset: 4; tab-width: 4 -*- */
/*
 * main.cc
 * Copyright (C) Albert Bendicho 2011 <albert.codejam@mailinator.com>
 * 
 */
#include <fstream>
#include <string>

using namespace std;
fstream fin;
fstream fout;


int main()
{
	 fin.open("A-large.in", fstream::in);
	 fout.open("A-large.out", fstream::out);

	int t;
	fin>>t;
	for (int testcase=0; testcase<t ; testcase++) {
		int h,b;
		fin >> h >>b;
		string board [h];
		for (int ih=0; ih<h; ih++){
			fin >> board[ih];
		}
		bool possible=true;
		for (int ih=0; ih<h; ih++){
			for (int ib=0;ib<b;ib++) {
				if (board[ih][ib]=='#') {
					if (
						(ih<h-1)&&
						(ib<b-1)&&
						(board[ih][ib+1]=='#')&&
						(board[ih+1][ib]=='#')&&
						(board[ih+1][ib+1]=='#')
						) {
						board[ih][ib]='/';
						board[ih][ib+1]='\\';
						board[ih+1][ib]='\\';
						board[ih+1][ib+1]='/';		
					} else {
						possible=false;
					}//rules ok
				}//#
			}//ib
		} //for ih

		fout<<"Case #"<<testcase+1<<": "<<endl;
		if (possible) {
			for (int ih=0; ih<h; ih++){
				for (int ib=0;ib<b;ib++) {
					fout<<board[ih][ib];
				}
				fout<<endl;
			}
		} else {
			fout<<"Impossible"<<endl;
		}
	}
	return 0;
}
