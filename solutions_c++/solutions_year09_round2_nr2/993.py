#include <complex>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int n;
char orig[1000];
char curr[1000];
void readInput() {
	scanf( "%s", orig);
	n = strlen(orig);
	strcpy(curr, orig);
}


void swap0s() {
	int i = 0;
	bool change;
	while(curr[i] == '0') {
		change = false;
		for( int j = i + 1; j < n; j++) {
			if( curr[j] != '0') {
				curr[i] = curr[j];
				curr[j] = '0';
				change = true;
				break;
			}
		}
		if(change) i = 0;
		else i++;
	}

}
void insert0(){

	swap0s();

	for(int i = n; i > 1; i-- ) {
		curr[i] = curr[i-1];
	}
	curr[1] = '0';
	curr[++n] = '\0';

}

void solveTestCase() {

	next_permutation (curr,curr+n);

	if( strcmp(curr, orig) <= 0 ) {
		insert0();
	}

}

void printOutput(int testcase) {

		printf( "Case #%d: %s\n" , testcase, curr);

}


int main() {

	int testcases;

//	freopen( "sample.in", "r", stdin);
//	freopen( "small.in" , "r", stdin);
//	freopen( "large.in" , "r", stdin);

//	freopen( "small.out", "w", stdout);
//	freopen( "large.out", "w", stdout);
	
	scanf( "%d", &testcases);
	for( int i = 1; i <= testcases; i++ ) {
		readInput();
		solveTestCase();
		printOutput(i);
	}

	return 0;
}
