/*
 * main.cpp
 *
 *  Created on: 13.04.2013
 *      Author: HP-User
 */


#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main() {
	ifstream inFile("input.txt");
	int t,tx,ty;
	vector<string> line;
	string tempString;
	vector<int> outcome;
	bool draw,tFound,gComplete;
	if (!inFile.good()){
		cout << "inFile not good!"<< endl;
		return 1;
	}
	inFile >> t;

	line.resize(4);

	for (int i=0;i<t;i++) {
		for (int j=0;j<4;j++) {
			inFile>>line[j];
		}

/*
		for (int j=0;j<4;j++) {
			cout << line[j] << endl;
			}*/

		draw=true;
		tFound=false;
		gComplete=false;

		for (int j=0;j<4;j++){
			if (((line[j][0]=='X')||(line[j][0]=='T'))&&((line[j][1]=='X')||(line[j][1]=='T'))&&((line[j][2]=='X')||(line[j][2]=='T'))&&((line[j][3]=='X')||(line[j][3]=='T'))) {
				outcome.push_back(0);
				draw=false;
				gComplete=true;
				break;
			}


			if (((line[j][0]=='O')||(line[j][0]=='T'))&&((line[j][1]=='O')||(line[j][1]=='T'))&&((line[j][2]=='O')||(line[j][2]=='T'))&&((line[j][3]=='O')||(line[j][3]=='T'))) {
				outcome.push_back(1);
				draw=false;
				gComplete=true;
				break;
			}

			if (((line[0][j]=='X')||(line[0][j]=='T'))&&((line[1][j]=='X')||(line[1][j]=='T'))&&((line[2][j]=='X')||(line[2][j]=='T'))&&((line[3][j]=='X')||(line[3][j]=='T'))) {
				outcome.push_back(0);
				draw=false;
				gComplete=true;
				break;
			}


			if (((line[0][j]=='O')||(line[0][j]=='T'))&&((line[1][j]=='O')||(line[1][j]=='T'))&&((line[2][j]=='O')||(line[2][j]=='T'))&&((line[3][j]=='O')||(line[3][j]=='T'))) {
				outcome.push_back(1);
				draw=false;
				gComplete=true;
				break;
			}
		}

		if (((line[0][0]=='X')||(line[0][0]=='T'))&&((line[1][1]=='X')||(line[1][1]=='T'))&&((line[2][2]=='X')||(line[2][2]=='T'))&&((line[3][3]=='X')||(line[3][3]=='T'))) {
			outcome.push_back(0);
			draw=false;
			gComplete=true;
		}

		if (((line[0][0]=='O')||(line[0][0]=='T'))&&((line[1][1]=='O')||(line[1][1]=='T'))&&((line[2][2]=='O')||(line[2][2]=='T'))&&((line[3][3]=='O')||(line[3][3]=='T'))) {
			outcome.push_back(1);
			draw=false;
			gComplete=true;
		}

		if (((line[0][3]=='X')||(line[0][3]=='T'))&&((line[1][2]=='X')||(line[1][2]=='T'))&&((line[2][1]=='X')||(line[2][1]=='T'))&&((line[3][0]=='X')||(line[3][0]=='T'))) {
			outcome.push_back(0);
			draw=false;
			gComplete=true;
		}

		if (((line[0][3]=='O')||(line[0][3]=='T'))&&((line[1][2]=='O')||(line[1][2]=='T'))&&((line[2][1]=='O')||(line[2][1]=='T'))&&((line[3][0]=='O')||(line[3][0]=='T'))) {
			outcome.push_back(1);
			draw=false;
			gComplete=true;
		}

		if ((!gComplete)) {
			for (int j=0;j<4;j++) {
				for (int k=0;k<4;k++) {
					if (line[j][k]=='.') {
						draw=false;
						gComplete=false;
					}
				}
			}
			if (!draw)
				outcome.push_back(3);
		}
		if (draw)
			outcome.push_back(2);
	}

	inFile.close();

	ofstream outFile("output.txt");

	for (int i=0;i<t;i++) {
		switch(outcome[i]) {
		case 0:
			outFile << "Case #" << i+1 <<": X won" << endl;
			break;
		case 1:
			outFile << "Case #" << i+1 <<": O won" << endl;
			break;
		case 2:
			outFile << "Case #" << i+1 <<": Draw" << endl;
			break;
		case 3:
			outFile << "Case #" << i+1 <<": Game has not completed" << endl;
			break;
		default:
			cout << "Not handled" << endl;
		}
	}
	outFile.close();
	return 0;
}

