#include<algorithm>
#include<iostream>
#include<string>
#include<vector>
#include<cstdio>
#include<cstdlib>
#include<sstream>
#include<cmath>
#include<fstream>
#include<map>

#define MAX(x, y) ((x) > (y) ? (x) : (y))
#define MIN(x, y) ((x) < (y) ? (x) : (y))
#define ABS(x) ((x) > 0 ? (x) : -(x))

#define SWAP(x, y) {(x) += (y); (y) = (x) - (y); (x) -= (y);}

using namespace std;

int table[19][501];

string ref = "welcome to code jam";

int process(string line){

	int n = line.size(), c, r;
	if(n < 19)
		return 0;

	memset(table, 0, sizeof(table));

	table[0][0] = (line[0] == ref[0]? 1: 0);

	for(c = 1; c < n; c++){

		table[0][c] = (table[0][c - 1] + (line[c] == ref[0] ? 1: 0)) % 10000;
		for(r = 1; r < 19; r++){

			table[r][c] = (table[r][c - 1] + (line[c] == ref[r]? table[r - 1][c - 1]: 0)) % 10000;

		}
	}

	return table[18][n - 1];


}
int main()

{
	
	int N, caseIdx;

	string line;

	cin >> N;
	getline(cin, line);

	for(caseIdx = 1; caseIdx <= N; caseIdx++){
		getline(cin, line);

		printf("Case #%d: %04d\n", caseIdx, process(line));

	}
	
	return 0;
}

/*
 * vim: ts=2 sw=2
 * Local variables:
 * tab-width: 2
 * End:
 */
