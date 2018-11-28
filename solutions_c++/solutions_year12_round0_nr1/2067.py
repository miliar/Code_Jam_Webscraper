//============================================================================
// Name        : codejam_2012_q.cpp
// Author      : festony
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================


#include <iostream>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
using namespace std;

char trans_g_to_e_table [26] = {
		'y',	// a
		'h',	// b
		'e',	// c
		's',	// d
		'o',	// e
		'c',	// f
		'v',	// g
		'x',	// h
		'd',	// i
		'u',	// j
		'i',	// k
		'g',	// l
		'l',	// m
		'b',	// n
		'k',	// o
		'r',	// p
		'z',	// q
		't',	// r
		'n',	// s
		'w',	// t
		'j',	// u
		'p',	// v
		'f',	// w
		'm',	// x
		'a',	// y
		'q',	// z
};

void trans(char * buf, int len) {
	for(int i=0; i<len; i++) {
		if(buf[i] <='z' && buf[i] >= 'a') {
			buf[i] -= 'a';
			buf[i] = trans_g_to_e_table[buf[i]];
		}
	}
}

static string process(int caseNum) {
	char buf[10240];
	string temp_str = "";
	string result = "";

	cin.getline(buf, 10240);
	trans(buf, strlen(buf));

	temp_str.append(buf);

	sprintf(buf, "Case #%d: %s\n", caseNum + 1, temp_str.c_str());
	result.append(buf);
	return result;
}

int main() {
	int caseNum = 0;
	cin >> caseNum;
	cin.ignore(256, '\n');
	char buf[10240];

	string result = "";

	for (int i = 0; i < caseNum; i++) {
		result.append(process(i));
	}
	cout << result;

	return 0;
}


