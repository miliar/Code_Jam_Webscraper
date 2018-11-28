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

#define db(x) fout << #x << " = " << x << endl;
#define rep(i,n) for (int i=0, j=n; i < j; i++)

int main () {
	ifstream fin ("B.in");
	ofstream fout ("output.txt");
	int nCases = 0;
	fin >> nCases;
	rep (ij, nCases) {
		map <string, char> replaceMap;
		vector <string> clearStrings;
		int nReplace; fin >> nReplace;
		
		
		rep(i,nReplace) {
			string s; fin >> s;
			string s2 = string() + s[0]; s2  += s[1];
			
			sort (s2.begin(), s2.end());
			replaceMap [s2] = s[2];
		}
		
		int nClear; fin >> nClear;
		rep (i, nClear) {
			string s; fin >> s;
			clearStrings.push_back (s);
		}
		
		int nCharsInString; fin >> nCharsInString;
		string inputString; fin >> inputString;
		
		//do simulation
		string curString;
		int charCount [200] = {0};
		rep (i, inputString.size()) {
			curString += inputString [i];
			charCount [inputString[i]]++;
			//check for replacement then check for clear
			int curStringSize = curString.size();
			if (curStringSize >= 2) {
				//get last 2 chars
				string lastTwo = string() + curString [curStringSize - 2] + curString [curStringSize - 1];
				sort (lastTwo.begin(), lastTwo.end());
				//is in replace?
				if (replaceMap.count(lastTwo) > 0) {
					//take off last two and add new char
					charCount [curString[curString.size() - 1] ] --;
					curString.erase (curString.begin() + curString.size() - 1);
					
					charCount [curString[curString.size() - 1]] --;
					curString.erase (curString.begin() + curString.size() - 1);
					
					
					curString += replaceMap [lastTwo];
					charCount [replaceMap[lastTwo]]++;
				}
				//clear check
				rep (k, clearStrings.size()) {
					char c1 = clearStrings [k][0], c2 = clearStrings[k][1];
					if (charCount [c1] && charCount [c2]) {
						curString.clear();
						rep(l,200) {
							charCount[l] = 0;
						}
					}
				}
			//	db (inputString[i]); db (curString);
			}
		}
		fout << "Case #" << ij + 1 << ": [";
		rep (i, curString.size() ) {
			if (i < curString.size() - 1 ) {
				fout << curString[i] << ", ";
			} else {
				fout << curString[i];
			}
		}
		fout << "]\n";
	}
	cout << "Done" << endl;
	int z;
	cin >> z;
	return 0;
}
