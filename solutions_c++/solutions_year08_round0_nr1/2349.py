#include <cstdio>
#include <vector>
#include <string>
#include <iostream>
#include <map>
#include <algorithm>

using namespace std;
char tmp[150];

int main(int argc, char **argv) {
	int nTests;
	scanf("%d", &nTests);
	for (int i = 0; i < nTests; ++i) {
		vector<string> engines;
		map<string, int> engNo;
		int switches[150];
		int nEngines;
		scanf("%d", &nEngines);
		fgets(tmp, 150, stdin);
		for (int j = 0; j < nEngines; ++j) {
			fgets(tmp, 150, stdin);
			string s(tmp);
			engNo[s] = engines.size();
			engines.push_back(s);
			switches[j] = 0;
		}
		int nQueries;
		scanf("%d", &nQueries);
		fgets(tmp, 150, stdin);
		for (int j = 0; j < nQueries; ++j) {
			fgets(tmp, 150, stdin);
			string s(tmp);
			map<string, int>::const_iterator it = engNo.find(s);
			if (it != engNo.end()) {
				// cerr << "hit: " << it->second << " with " << it->first;
				for (int k = 0; k < nEngines; ++k) {
					if (switches[k] > (switches[it->second]+1)) {
						switches[k] = switches[it->second] + 1;
					}
				}
				switches[it->second] = 1 << 30;
			}
			/*
			cerr << "Query: " << j << " and switches:";
			for (int k = 0; k < nEngines; ++k) {
				cerr << " " << switches[k];
			}
			cerr << endl;
			*/
		}
		int minimum = switches[0];
		for (int j = 1; j < nEngines; ++j) {
			if (switches[j] < minimum) {
				minimum = switches[j];
			}
		}
		printf("Case #%d: %d\n", i+1, minimum);
	}
}
