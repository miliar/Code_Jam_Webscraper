#include <algorithm>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <memory.h>
#include <stdio.h>
#include <vector>
#include <fstream>
#include <math.h>
using namespace std;


#define R(x) scanf("%d",&x);
#define FOR(i,j) for(int i = 0;i < j;i++)
#define i64 long long


ofstream myfile ("/Users/mac/Desktop/ans.txt");

char inp [5][5];
int i = 1;

bool check(int i,int j,char r) {

	int count = 0;
	int x = i;
	int y = j;

	for(; y < 4;y++) {
		if(inp[x][y] == r || inp[x][y] == 'T')
			count++;
	}
	if(count == 4)
		return true;

	x = i;
	y = j;
	count = 0;
	for(; x < 4;x++) {
		if(inp[x][y] == r || inp[x][y] == 'T')
			count++;
	}
	if(count == 4)
		return true;

	x = i;
	y = j;
	count = 0;
	for(; x < 4 && y < 4;x++, y++) {
		if(inp[x][y] == r || inp[x][y] == 'T')
			count++;
	}
	if(count == 4)
		return true;


	x = i;
	y = j;
	count = 0;
	for(; x >= 0 && y < 4;x--, y++) {
		if(inp[x][y] == r || inp[x][y] == 'T')
			count++;
	}
	if(count == 4)
		return true;


	x = i;
	y = j;
	count = 0;
	for(; x < 4 && y > -1;x++, y--) {
		if(inp[x][y] == r || inp[x][y] == 'T')
			count++;
	}
	if(count == 4)
		return true;

	return false;
}


int process() {
	FOR(x,4) {
		FOR(y,4) {
			if(inp[x][y] != '.' && check(x,y,inp[x][y])) {

				if(inp[x][y] == 'X') {
					myfile << "Case #" << i << ": X won\n";
					return 0;
				}else{
					myfile << "Case #" << i << ": O won\n";
					return 0;
				}
			}
		}
	}

	FOR(x,4) {
		FOR(y,4) {
			if(inp[x][y] == '.') {
				myfile << "Case #" << i << ": Game has not completed\n";
				return 0;
			}
		}
	}

	myfile << "Case #" << i << ": Draw\n";
}

int main() {


	ifstream infile;
	infile.open ("/Users/mac/Desktop/A-small-attempt3.in");
	

	int n;
	infile >> n;

	for(;i<=n;i++) {
		FOR(x,4) {
			FOR(y,4) {
				infile >> inp[x][y];
			}
		}
		process();
	}
}



