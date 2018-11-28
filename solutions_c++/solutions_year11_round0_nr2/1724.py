#include <iostream>
#include <cstdio>
#include <map>
#include <string>
#include <set>
#include <cmath>

namespace gcj {
	using namespace std;
	string ls;
	map<char, char> combine[256];
	map<char, char>::iterator comItr;
	set<char> opposed[256];
	//set<char>::iterator oppItr;
	//int charNumber[256];

	void init() {
		ls.clear();
		for (int  i = 0; i < 256; i ++) {
			combine[i].clear();
			opposed[i].clear();
		}
		//memset(charNumber, 0, sizeof(charNumber));
	}

	void solve() {
		int t, c, d, n;
		char comStr[5], oppStr[5];
		char input[105];
		scanf(" %d", &t);
		for (int i = 0; i < t; i ++) {
			init();

			scanf(" %d", &c);
			for(int j = 0; j < c; j ++) {
				scanf(" %s", comStr);
				combine[comStr[0]][comStr[1]] = combine[comStr[1]][comStr[0]] = comStr[2];
			}

			scanf(" %d", &d);
			for(int j = 0; j < d; j ++) {
				scanf(" %s", oppStr);
				opposed[oppStr[0]].insert(oppStr[1]);
				opposed[oppStr[1]].insert(oppStr[0]);
			}

			scanf(" %d", &n);
			scanf(" %s", input);
			for(int j = 0; j < n; j ++) {
				char key = input[j];
				bool run = true;
				//oppItr = opposed[key].begin();

				if (ls.size() > 0) {
					if ((comItr = combine[key].find(ls.back())) != combine[key].end()) {
						//charNumber[ls.back()] --;
						ls.pop_back();
						ls.push_back(comItr->second);
						//charNumber[comItr->second] ++;
						run = false;
					}

					if (run) {
						for (int k = 0; k < ls.size(); k ++) {
							if (opposed[key].find(ls[k]) != opposed[key].end()) {
								//ls = ls.substr(0, k);
								ls.clear();
								run = false;
							}
						}
					}
					//while (run && oppItr != opposed[key].end()) {
					//	if (charNumber[*oppItr] > 0) {
					//		while(ls.back() != *oppItr) {
					//			charNumber[ls.back()] --;
					//			ls.pop_back();
					//		}
					//		charNumber[ls.back()] --;
					//		ls.pop_back();
					//		run = false;
					//	}
					//	oppItr ++;
					//}
				}

				if (run) {
					ls.push_back(key);
					//charNumber[key] ++;
				}
			}

			printf("Case #%d: [", i + 1);
			for (int j = 0; j < ls.size(); j ++) {
				if (j > 0) {
					putchar(',');
					putchar(' ');
				}
				putchar(ls[j]);
			}
			puts("]");
		}

	}
}



int main () {

	//freopen("d:/GCJ/B-large.in", "r", stdin);
	//freopen("d:/GCJ/B-large.out", "w", stdout);

	gcj::solve();
	return 0;
}