#include <iostream>
#include <fstream>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <cmath>
#include <cctype>
#include <cstdio>
#include <vector>
#include <deque>
using namespace std;

#define db(x) cout << #x << " = " << x << endl;
#define rep(i,n) for (int i=0, j=n; i < j; i++)
const int MAXTIME = 100 * 100 +100;

int getDelay (int &place, int &to) {
	return abs (place - to) + 1; //go there and press button
}

void update (int &place, const int &delay, int &ind, const vector < pair<char, int> > &instructions){
	if (ind >= instructions.size())return;
	
	//find where I'm going
	int to = instructions [ind].second;
	int maxMove = delay;
	
	if (abs(to - place) <= maxMove) 
		place = to;
	else {
		if (to >= place) 
			place = place + maxMove;
		else place -= maxMove;
	}
}
			

int main () {
	ifstream fin ("A.in");
	ofstream fout ("output.txt");
	int nCases = 0;
	fin >> nCases;
	
	for (int ij = 0; ij < nCases; ij++) {
		int nInstructions;
		fin >> nInstructions;
		vector < pair<char, int> > instructions;
		vector < pair <char, int> > oinstructions;
		vector < pair <char, int> > pinstructions;
		int ans = 0;
		rep (i,nInstructions) {
			char c;
			int n;
			fin >> c >> n;
			instructions.push_back (make_pair (c,n));
			if (c == 'O') {
				oinstructions.push_back (make_pair(c,n));
			} else {
				pinstructions.push_back (make_pair(c,n));
			}
		}
		int oind = 0;
		int pind = 0;
		int oplace = 1;
		int pplace = 1;
		//for each instruction
		rep (i, nInstructions) {
			//do current instruction and update other positions given time delay
			
			char target = instructions [i].first;
			int to = instructions [i].second;
			
			int delay = 0;
			if (target == 'O') {
				delay = getDelay (oplace, to);
				oplace = to;
				update (pplace, delay, pind, pinstructions);
				oind++;
			} else {
				delay = getDelay (pplace, to);
				pplace = to;
				update (oplace, delay, oind, oinstructions);
				pind++;
			}
			//db (delay); db (oplace); db (pplace);
			ans += delay;
		}
		fout << "Case #" << ij + 1 << ": " << ans << endl;
	}
	cout << "Done" << endl;
	int z;
	cin >> z;
	return 0;
}
