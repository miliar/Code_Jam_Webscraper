//
//  main.cpp
//  codejam-tttt
//
//  Created by Vlad Harbuz on 13/04/2013.
//  Copyright (c) 2013 Vlad Harbuz. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <string>
using namespace std;

// return codes:
// 0 - nothing
// 1 - X won
// 2 - O won
// 3 - draw

// vars
// x[0] -> rows
//		x[0][i] -> row i
// x[1] -> cols
//		x[1][i] -> col i
// x[2] -> diagonal
//		x[2][0] -> first diagonal
//		x[2][1] -> second diagonal

int checkStatus(int x[4][4], int o[4][4], int t[4][4], int dots){
	int i, j;

	for(i=0; i<3; i++){
		for(j=0; j<4; j++){
			if(i==2 && j>1) break;
			if(x[i][j] == 4 || (x[i][j] == 3 && t[i][j] == 1)){
				return 1;
			}
			if(o[i][j] == 4 || (o[i][j] == 3 && t[i][j] == 1)){
				return 2;
			}
		}
	}

	if(dots==0){
		return 3;
	}

	return 0;
}

int main(int argc, const char * argv[]) {
	ifstream in;
	ofstream out;
	string line;
	char square;
	int cases, i, j, k, status=0;
	int x[4][4], o[4][4], t[4][4];
	int dots;

	in.open("A-large.in");
	out.open("data.out");
	if(!in.is_open()){
		cout<<"Unable to open input file.";
		exit(0);
	}
	if(!out.is_open()){
		cout<<"Unable to open ouput file.";
		exit(0);
	}

	getline(in,line);
	cases = atoi(line.c_str());

	for(k=1; k<=cases; k++){
		memset(x,0,sizeof(x));
		memset(o,0,sizeof(o));
		memset(t,0,sizeof(t));
		dots = 0;
		for(i=0; i<4; i++){
			getline(in,line);
			for(j=0; j<4; j++){
				square = line.at(j);
				if(square == 'X'){
					x[0][i]++;
					x[1][j]++;
					if(i==j){ x[2][0]++; }
					if(i+j==3){ x[2][1]++; }
				}else if(square == 'O'){
					o[0][i]++;
					o[1][j]++;
					if(i==j){ o[2][0]++; }
					if(i+j==3){ o[2][1]++; }
				}else if(square == 'T'){
					t[0][i]++;
					t[1][j]++;
					if(i==j){ t[2][0]++; }
					if(i+j==3){ t[2][1]++; }
				}else if(square == '.'){
					dots++;
				}
			}
		}

		status = checkStatus(x, o, t, dots);

		out<<"Case #"<<k<<": ";
		switch(status){
			case 0:
				out<<"Game has not completed";
				break;
			case 1:
				out<<"X won";
				break;
			case 2:
				out<<"O won";
				break;
			case 3:
				out<<"Draw";
				break;
		}
		out<<endl;

		getline(in,line);
	}

	in.close();
    return 0;
}
