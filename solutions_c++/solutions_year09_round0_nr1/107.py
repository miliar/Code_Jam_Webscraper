#include <stdio.h>
#include <vector>
#include <iostream>
#include <set>
#include <string>
#include <cassert>
#include <list>

using namespace std;

list<string> dict;

int main() {
	int L, D, N;
	scanf("%d %d %d\n",&L,&D,&N);
	for (int i = 0; i < D; i++) {
		char buff[20];
		gets(buff);
		dict.push_back(string(buff));
	}
	for (int i = 0; i < N; i++) {
		list<string> valid = dict;
		set<char> pchars;
		char buff[30000];
		gets(buff);
		bool inPars = false;
		int idx = 0;
		int si = 0;
		while (buff[idx] != '\n' && buff[idx] != '\r' && buff[idx] != 0) {
			if (buff[idx] == '(') {
				assert(!inPars);
				inPars = true;
				pchars.clear();
			} else if (buff[idx] == ')') {
				assert(inPars);
				inPars = false;
				list<list<string>::iterator> toremove;
				for (list<string>::iterator it = valid.begin(); it != valid.end(); ++it) {
					if (pchars.count((*it)[si]) == 0) {
						toremove.push_back(it);
					}
				}
				for (list<list<string>::iterator>::iterator it = toremove.begin(); it != toremove.end(); ++it) {
					valid.erase(*it);
				}
				si++;
			} else {
				if (inPars) {
					pchars.insert(buff[idx]);
				} else {
					list<list<string>::iterator> toremove;
					for (list<string>::iterator it = valid.begin(); it != valid.end(); ++it) {
						if ((*it)[si] != buff[idx]) {
							toremove.push_back(it);
						}
					}
					for (list<list<string>::iterator>::iterator it = toremove.begin(); it != toremove.end(); ++it) {
						valid.erase(*it);
					}
					si++;
				}
			}
			idx++;
		}
		printf("Case #%d: %d\n", i + 1, valid.size());
	}
	return 0;
}