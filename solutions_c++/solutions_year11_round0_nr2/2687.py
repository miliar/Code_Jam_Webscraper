#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>
#include <utility>
#include <algorithm>

using namespace std;

int main(int argc, char* argv[]) {
	if (argc != 2) {
		cerr << "wrong parameter" << endl;
		return -1;
	}

	ifstream inf(argv[1]);
	if (!inf) {
		cerr << "cannot open file " << argv[1] << endl;
		return -1;
	}

	string ln;
	inf >> ln;
	int caseNum = atoi(ln.c_str());
	for (int i=0; i<caseNum; i++) {
		// read combine elements
		map< pair<char, char>, char > mapCombine; 
		inf >> ln;
		int eleNum = atoi(ln.c_str());
		for (int j=0; j<eleNum; j++) {
			inf >> ln; 
			pair<char, char> pa(ln[0], ln[1]);
			mapCombine[pa] = ln[2];
		}

		// read oppose elements
		vector< pair<char, char> > vecOppose;
		inf >> ln;
		eleNum = atoi(ln.c_str());
		for (int j=0; j<eleNum; j++) {
			inf >> ln;
			vecOppose.push_back(pair<char, char>(ln[0], ln[1]));
		}

		// read input string
		inf >> ln;
		int inLen = atoi(ln.c_str());
		inf >> ln;

		// find solution
		vector<char> vecResult;
		for (int id=0; id<inLen; id++) {
			if (vecResult.size() == 0) {
				vecResult.push_back(ln[id]);
			}
			else {
				pair<char, char> pa1(ln[id], vecResult.back()), 
					             pa2(vecResult.back(), ln[id]);
				if (mapCombine.find(pa1) != mapCombine.end()) {
					// find combine elements
					vecResult.pop_back();
					vecResult.push_back(mapCombine[pa1]);
				}
				else if (mapCombine.find(pa2) != mapCombine.end()) {
					// find combine elements
					vecResult.pop_back();
					vecResult.push_back(mapCombine[pa2]);
				}
				else {
					// find oppose elements
					int opposeNum=0;
					for (; opposeNum<vecOppose.size(); opposeNum++) {
						if (ln[id] == vecOppose[opposeNum].first) {
							if (find(vecResult.begin(), vecResult.end(), 
								vecOppose[opposeNum].second) != vecResult.end()) {
									vecResult.clear();
									break;
							}
						}
						else if (ln[id] == vecOppose[opposeNum].second) {
							if (find(vecResult.begin(), vecResult.end(), 
								vecOppose[opposeNum].first) != vecResult.end()) {
									vecResult.clear();
									break;
							}
						}
					}
					if (opposeNum == vecOppose.size()) {
						vecResult.push_back(ln[id]);
					}
				}
			}
		}
		cout << "Case #" << i+1 << ": [";
		if (!vecResult.empty()) {
			cout << vecResult[0];
			for (int ri=1; ri<vecResult.size(); ri++) {
				cout << ", ";
				cout << vecResult[ri];
			}
		}
		
		cout << "]" << endl;
	}
	return 0; 
}