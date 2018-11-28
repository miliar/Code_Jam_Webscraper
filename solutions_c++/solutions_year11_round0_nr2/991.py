/*
 *  File: Magicka.cpp
 *  ------------------
 *
 *  Created by Elina Robeva on 5/6/11.
 *
 */

#include "genlib.h"
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>
#include <vector>
using namespace std;


int main() {
	freopen("/Users/erobeva/Downloads/B-large.in","r",stdin);
	freopen("/Users/erobeva/Downloads/AAAAAAAAAAout.txt", "w", stdout);
	
	int T;
	cin >> T;
	for(int i = 0; i < T; ++i) {
		int C;
		cin >> C;

		vector < vector <int> > table(26);
		vector < vector <int> > table1(26);
		for(int j = 0; j < 26; ++j) {
			vector <int> row(26);
			vector <int> row1(26);
			table[j] = row;
			table1[j] = row1;
		}
		for(int j = 0; j < 26; ++j) {
			for(int k = 0; k < 26; ++k) {
				table[j][k] = -2;
				table1[j][k] = -2;
				
			}
		}
		
		
		for(int j = 0; j < C; ++j) {
			char c1, c2, c3;
			cin >> c1;
			cin >> c2;
			cin >> c3;
			int n1, n2, n3;
			n1 = c1 - 'A';
			n2 = c2 - 'A';
			n3 = c3 - 'A';
			table[n1][n2] = n3;
			table[n2][n1] = n3;
		}
		
		int D;
		cin >> D;

		for(int j = 0; j < D; ++j) {

			char c1, c2;
			cin >> c1;
			cin >> c2;

			int n1, n2;
			n1 = c1 - 'A';
			n2 = c2 - 'A';

			table1[n1][n2] = -1;
			table1[n2][n1] = -1;
		}
		int N;
		cin >> N;

		vector <char> final_List(N);
		int curLength = 0;
		for(int j = 0; j < N; ++j) {
			char c;
			cin >> c;

			int n = c - 'A';

			
			if(curLength > 0) {
				if(table[n][final_List[curLength-1]] >= 0) {
					final_List[curLength-1] = table[n][final_List[curLength-1]];
				} else {
					for(int k = 0; k < curLength; ++k) {
						if(table1[n][final_List[k]] == -1) {
							curLength = 0;
							break;
						}
					}
					if (curLength != 0) {
						final_List[curLength++] = n;
					}
				}
			} else {
				final_List[0] = n;
				curLength++;
			}
		}
		
		

		
		string result = "[";
		for(int j = 0; j < curLength; ++j) {
			char c = 'A' + final_List[j];
			result += c;
			if(j < curLength - 1) {
				result += ", ";
			}
		}
		result += "]";
		
		
		
		cout << "Case #" << i + 1 << ": " << result << endl;
		
	} 
	
	return 0;
}
