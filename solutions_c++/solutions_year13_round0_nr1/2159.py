#include <fstream>
#include <iostream>
#include <cstdio>

using namespace std;

char table[4][4];
int  scores[10];		// függőlegesek, vízszintesek, átlósok

int convert(char c) {
	switch(c) {
		case 'O': return 0; break;
		case 'X': return 1; break;
		case 'T': return 5; break;
		case '.': return -100; break;
	}
	return -1000;
}

string solve() {
	for (int i = 0; i < 10; i++) {
		scores[i] = 0;
	}
	
	int temp;
	temp = convert(table[0][0]); scores[0] += temp; scores[4] += temp; scores[8] += temp;
	temp = convert(table[0][1]); scores[1] += temp; scores[4] += temp;
	temp = convert(table[0][2]); scores[2] += temp; scores[4] += temp;
	temp = convert(table[0][3]); scores[3] += temp; scores[4] += temp; scores[9] += temp;
	temp = convert(table[1][0]); scores[0] += temp; scores[5] += temp;
	temp = convert(table[1][1]); scores[1] += temp; scores[5] += temp; scores[8] += temp;
	temp = convert(table[1][2]); scores[2] += temp; scores[5] += temp; scores[9] += temp;
	temp = convert(table[1][3]); scores[3] += temp; scores[5] += temp;
	temp = convert(table[2][0]); scores[0] += temp; scores[6] += temp;
	temp = convert(table[2][1]); scores[1] += temp; scores[6] += temp; scores[9] += temp;
	temp = convert(table[2][2]); scores[2] += temp; scores[6] += temp; scores[8] += temp;
	temp = convert(table[2][3]); scores[3] += temp; scores[6] += temp;
	temp = convert(table[3][0]); scores[0] += temp; scores[7] += temp; scores[9] += temp;
	temp = convert(table[3][1]); scores[1] += temp; scores[7] += temp;
	temp = convert(table[3][2]); scores[2] += temp; scores[7] += temp;
	temp = convert(table[3][3]); scores[3] += temp; scores[7] += temp; scores[8] += temp;
	
	bool draw = true;
	for (int i = 0; i < 10; i++) {
		if (scores[i] == 0 || scores[i] == 5) {
			return "O won";
		} else if (scores[i] == 4 || scores[i] == 8) {
			return "X won";
		} else if (scores[i] < -50) {
			draw = false;
		}
	}
	
	if (draw) {
		return "Draw";
	} else {
		return "Game has not completed";
	}
}

int main() {
	ifstream f;
	f.open("input.txt");
	
	ofstream g;
	g.open("output.txt");
	
	int n;
	f >> n;
	
	//f >> buff;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < 4; j++) {
			for (int k = 0; k < 4; k++) {
				f >> table[j][k];
//cout << table[j][k];
			}
//cout << endl;
		}
		
		//cout << "Case #" << i+1 << ": " << solve() << endl;
		g << "Case #" << i+1 << ": " << solve() << endl;
	}
	
	
	f.close();
	g.close();
	return 0;
}
