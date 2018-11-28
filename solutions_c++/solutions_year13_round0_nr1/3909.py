//============================================================================
// Name        : tic-tac-toe-tomek.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
#include <set>
#include <sstream>
using namespace std;

int main() {
	cout << "!!!Hello World!!!" << endl; // prints !!!Hello World!!!
    ofstream outfile("large.out");
	ifstream myfile("large.txt");
	int lines;
	myfile >> lines;
	set<string> x;
	x.insert("XXXX");
	x.insert("XXXT");
	x.insert("XXTX");
	x.insert("XTXX");
	x.insert("TXXX");
	set<string> y;
	y.insert("OOOO");
	y.insert("OOOT");
	y.insert("OOTO");
	y.insert("OTOO");
	y.insert("TOOO");
	string l;
	getline(myfile, l);
	//cout <<" first line : " <<l <<"\n";
	for(int i = 1; i <= lines; ++i){
		string line;
		string matrix[4];
		stringstream result;
		result << "Case #" << i << ": ";
		for(int j = 0; j < 4; ++j){
			getline(myfile, line);
			matrix[j] = line;
		}
		//solve
		stringstream d1;
		d1 << matrix[0][0] << matrix[1][1] << matrix[2][2] << matrix[3][3];
		string diag1 = d1.str();
		stringstream d2;
		d2 << matrix[3][0] << matrix[2][1] << matrix[1][2] << matrix[0][3];
		string diag2 = d2.str();
		//cout << "diag1 "<< diag1 <<"\n"<<"diag2 " <<diag2 <<"\n";
		bool empty = false;
		bool foundSolution = false;
		for(int j = 0; j < 4; ++j){
			size_t found = matrix[j].find(".");
			if(found != std::string::npos){
				empty = true;
			}
			stringstream l;
			l <<matrix[0][j] << matrix[1][j] << matrix[2][j] << matrix[3][j];
			string line = l.str();

			if((x.count(matrix[j]) == 1) ||
			   (x.count(line) == 1) ||
			   (x.count(diag1) == 1) ||
			   (x.count(diag2) == 1)){
				result << "X won";
				foundSolution = true;
			//	cout << i<< " X  " << line <<" j  " << j << "\n";
				break;
			}


			if((y.count(matrix[j]) == 1) ||
			   (y.count(line) == 1) ||
			   (y.count(diag1) == 1) ||
			   (y.count(diag2) == 1 )){
				result << "O won";
				cout << i<<" Y  " << line <<" j  " << j << "\n";
				foundSolution = true;
				break;
			}
		}
		if(!foundSolution){
			if(empty){
				result << "Game has not completed";
			}else{
				result << "Draw";
			}
		}
		//
		//cout << result.str() << "\n";
		outfile << result.str();
		if(i != lines)
			outfile <<"\n";

		getline(myfile, line);
	}
    myfile.close();
    outfile.close();
	return 0;
}
