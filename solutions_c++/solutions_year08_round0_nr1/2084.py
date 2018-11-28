#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <string>
#include <map>
#include <vector>
#include <sstream>

using namespace std;

string SearchEngine[110];
string Query[1100];
map <string, int> Hash;
int DP[1100][110];

int main() {
	int nTC;
	string kalimat;
	getline(cin, kalimat);
	stringstream sa(kalimat);
	sa >> nTC;
	for (int kasus=1; kasus<=nTC; kasus++) {
		int nSearchEngine, nQuery;
		
		getline(cin, kalimat);
		stringstream ss(kalimat);
		ss >> nSearchEngine;
		
		for (int i=0; i<nSearchEngine; i++)
			getline(cin, SearchEngine[i]);
		
		getline(cin, kalimat);
		stringstream s1(kalimat);
		s1 >> nQuery;
		
		for (int i=0; i<nQuery; i++)
			getline(cin, Query[i]);
		
		memset(DP, 0x1f, sizeof(DP));
		if (nQuery)
			for (int i=0; i<nSearchEngine; i++)
				if (Query[0]!=SearchEngine[i])
					DP[0][i]=0;
		
		for (int i=1; i<nQuery; i++) {
			for (int j=0; j<nSearchEngine;  j++) {
				if (Query[i]!=SearchEngine[j]) {
					DP[i][j]=min(DP[i-1][j], DP[i][j]);
					for (int k=0; k<nSearchEngine; k++)
						if (k!=j)
							DP[i][j]=min(DP[i-1][k]+1, DP[i][j]);
				}
			}
		}
		
		int nswitch=1000000000;
		if (nQuery) {
			for (int i=0; i<nSearchEngine; i++)
				if (DP[nQuery-1][i]<nswitch)
					nswitch=DP[nQuery-1][i];
		} else {
			nswitch=0;
		}
		
		printf("Case #%d: %d\n", kasus, nswitch);
	}
	return 0;
}
