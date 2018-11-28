#include <iostream>
#include <list>
#include <vector>
#include <map>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <set>
#include <cctype>
using namespace std;

#define MAXS 100
#define MAXQ 1000

int S, Q, N;
map<string, bool> engines;
//string queries[MAXQ];

int
main()
{

	char temp[101];
	string query;
	int nvisited, answer;
	map<string, bool>::iterator it;
	scanf("%d\n", &N);
	
	for (int n = 1; n <= N; n++) {
		nvisited = 0;
		answer = 0;
		scanf("%d\n", &S);
		for (int i = 0; i < S; i++) {
			cin.getline(temp, 101);
			engines[string(temp)] = false;
			//cout << temp << endl;
		}
		scanf("%d\n", &Q);
		for (int i = 0; i < Q; i++) {
			cin.getline(temp, 101);
			query = string(temp);
			//cout << query << endl;
			if (! engines[query]) {
				engines[query] = true;
				++nvisited;
				
				if (nvisited == S) {
					it = engines.begin();
					
					for ( ; it != engines.end(); it++) {
						it->second = false;
					}
					engines[query] = true;
					nvisited = 1;
					++answer;
				}
			}
		}
		cout << "Case #" << n << ": " << answer << endl; 
	}


	return 0;
}
