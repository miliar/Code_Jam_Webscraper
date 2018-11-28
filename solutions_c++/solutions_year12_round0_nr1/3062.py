#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <list>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <utility>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstdio>

using namespace std;

#define REP(i,n) for((i)=0;(i)<(int)(n);(i)++)
#define foreach(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)

char tbl[26];

string phrase;

void table(){
	tbl[0] = 'y'; 
	tbl[1] = 'h';
	tbl[2] = 'e';
	tbl[3] = 's';
	tbl[4] = 'o';
	tbl[5] = 'c';
	tbl[6] = 'v';
	tbl[7] = 'x';
	tbl[8] = 'd';
	tbl[9] = 'u';
	tbl[10] = 'i';
	tbl[11] = 'g';
	tbl[12] = 'l';
	tbl[13] = 'b';
	tbl[14] = 'k';
	tbl[15] = 'r';
	tbl[16] = 'z';
	tbl[17] = 't';
	tbl[18] = 'n';
	tbl[19] = 'w';
	tbl[20] = 'j';
	tbl[21] = 'p';
	tbl[22] = 'f';
	tbl[23] = 'm';
	tbl[24] = 'a';
	tbl[25] = 'q';
}

char encode(char value) {
	return tbl[value - 'a'];
}

string process(){
	string result;
	char c[101];
	scanf("\n%[^\n]s",c);	
	phrase=c;
	result = "";
	int i = 0;
	REP(i, phrase.length()) {
		if (phrase.at(i) == ' ')
			result += " ";
		else
			result += encode(phrase.at(i));
	}
	return result;
}

int main(void){
	int t;
	scanf("%d", &t);
	phrase.resize(100);
	table();
	for (int tc = 1; tc <= t; ++tc) {
		printf("Case #%d: %s\n", tc, process().data());
	}	
}