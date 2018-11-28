#include <iostream>
#include <fstream>
#include <vector>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <queue>
using namespace std;

ifstream fin ("magicka.in");
ofstream fout ("magicka.out");

int numcase;

int elemcode(char elem) {
	switch (elem) {
		case 'Q': return 0;
		case 'W': return 1;
		case 'E': return 2;
		case 'R': return 3;
		case 'A': return 4;
		case 'S': return 5;
		case 'D': return 6;
		case 'F': return 7;
		default: return -1;
	}
}

int main() {
	fin >> numcase;
	for (int c = 1; c <= numcase; c++) {
		int combs, opps, elems;
		char table[8][8];
		bool clear[8][8];
		for (int i = 0; i < 8; i++)
			for (int j = 0; j < 8; j++) {
				table[i][j] = 0;
				clear[i][j] = false;
			}
		
		fin >> combs;
		for (int i = 0; i < combs; i++) {
			char str[3];
			fin >> str;
			table[elemcode(str[0])][elemcode(str[1])] = str[2];
			table[elemcode(str[1])][elemcode(str[0])] = str[2];
		}

		fin >> opps;
		for (int i = 0; i < opps; i++) {
			char str[2];
			fin >> str;
			clear[elemcode(str[0])][elemcode(str[1])] = true;
			clear[elemcode(str[1])][elemcode(str[0])] = true;
		}

		fin >> elems;
		char str[elems];
		fin >> str;
		vector<char> curr;
		curr.push_back(str[0]);
		
		int exist[8];
		for (int x = 0; x < 8; x++)
			exist[x] = 0;
		exist[elemcode(str[0])]++;
		for (int i = 1; i < elems; i++) {
			if (elemcode(curr.back()) >= 0 && table[elemcode(curr.back())][elemcode(str[i])] > 0) {
				char newelem = table[elemcode(curr.back())][elemcode(str[i])];
				exist[elemcode(curr.back())]--;
				curr.pop_back();
				curr.push_back(newelem);
			}
			else {
				curr.push_back(str[i]);
				exist[elemcode(str[i])]++;
			}
			
			for (int a = 0; a < 8; a++) {
				bool boom = false;
				if (exist[a] > 0)
					for (int b = a+1; b < 8; b++)
						if (exist[b] > 0 && clear[a][b]) {
							for (int x = 0; x < 8; x++)
								exist[x] = 0;
							curr.clear();
							boom = true;
							break;
						}
				if (boom)
					break;
			}
		}
		
		//output
		fout << "Case #" << c << ": [";
		bool front = true;
		for (int i = 0; i < curr.size(); i++) {
			if (front)
				front = false;
			else
				fout << ", ";
			fout << curr.at(i);
		}
		fout << "]\n";
	}
	exit(0);
}