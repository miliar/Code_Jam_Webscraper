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

void left_rotate(char * buf) {
	int len = strlen(buf);
	char carry = buf[len-1];
	for(int i=len-1; i>0; i--) {
		buf[i] = buf[i-1];
	}
	buf[0] = carry;
}

int get_digit_num(long long x) {
	int dn = 0;
	while(x > 0) {
		x /= 10;
		dn ++;
	}

	return dn;
}

static string process(int caseNum) {
	char buf[10240];
	string temp_str = "";
	string result = "";

	long long A, B;
	long long temp_long;

	cin >> A >> B;

	int count = 0;

	int digit_num = get_digit_num(A);

	if(digit_num < get_digit_num(B)) {
		digit_num = get_digit_num(B);
	}

	set<long long> temps;

	for(long long i = A; i <= B; i++) {
		sprintf(buf, "%d", i);
		temps.clear();
		for(int j=0; j<digit_num-1; j++) {
			left_rotate(buf);
			temp_long = atoi(buf);
			if(temps.find(temp_long) != temps.end()) {
				continue;
			}
			temps.insert(temp_long);
			if(temp_long <= B && temp_long > i) {
//				cout << i << " " << temp_long << "   ";
				count ++;
			}
		}
	}

	sprintf(buf, "Case #%d: %d\n", caseNum + 1, count);
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

//	char buf[] = "01234567";
//	for(int i=0; i<10; i++) {
//	left_rotate(buf);
//	cout << buf << endl;
//	}

	return 0;
}


