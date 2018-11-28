#include <iostream>
#include <fstream>
#include <vector>
#include <cstdlib>
#include <algorithm>
#include <queue>
using namespace std;

ifstream fin ("botTrust.in");
ofstream fout ("botTrust.out");

int numcase, N;

int main() {
	fin >> numcase;
	
	for (int c = 1; c <= numcase; c++) {
		int time = 0;
		int O = 1, B = 1;
		queue<int> olist, blist;
		char robot[100];
		
		fin >> N;
		for (int i = 0; i < N; i++) {
			char clr;
			int but;
			fin >> clr >> but;
			if (clr == 'O')
				olist.push(but);
			else if (clr == 'B')
				blist.push(but);
			robot[i] = clr;
		}
		
		for (int i = 0; i < N; i++) {
			if (robot[i] == 'O') {
				int travel = abs(olist.front() - O) + 1;
				O = olist.front();
				time += travel;
				olist.pop();
				
				if (!blist.empty()) {
					if (abs(blist.front() - B) > travel) {
						if (blist.front() > B)
							B += travel;
						else
							B -= travel;
					}
					else
						B = blist.front();
				}
			}
			else if (robot[i] == 'B') {
				int travel = abs(blist.front() - B) + 1;
				B = blist.front();
				time += travel;
				blist.pop();
				
				if (!olist.empty()) {
					if (abs(olist.front() - O) > travel) {
						if (olist.front() > O)
							O += travel;
						else
							O -= travel;
					}
					else
						O = olist.front();
				}
			}
		}
		
		fout << "Case #" << c << ": " << time << "\n";
	}
	exit(0);
}