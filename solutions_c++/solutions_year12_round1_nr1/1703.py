//============================================================================
// Name        : codejam_2012_r1a.cpp
// Author      : festony
// Version     :
// Copyright   : festony@gmail.com
// Description : Hello World in C++, Ansi-style
//============================================================================


#include <iostream>
#include <fstream>
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

//int power_of_two(int pow) {
//	if(pow == 0) {
//		return 0;
//	}
//	int r = 1;
//	for(int i=1; i<pow; i++) {
//		r = r << 1;
//	}
//	return r;
//}
//
//int get_binary_one_count(int x) {
//	unsigned int u = (unsigned int)x;
//	int r = 0;
//	for(;u != 0; u &= u-1) {
//		r++;
//	}
//	return r;
//}

double * p_i;
int A, B;

double calc_correct_property_press_n_backspace(int n) {
	double r = 0;
	for(int i=0; i<=n; i++) {
		double p = 1;
		for(int j=0; j<A; j++) {
			if(j<A-i) {
				p *= p_i[j];
			} else {
				p *= (1-p_i[j]);
			}
		}
		r += p;
	}

	return r;
}

int calc_keystrike_if_correct_press_n_backspace(int n) {
	return n * 2 + B - A + 1;
}

int calc_keystrike_if_incorrect_press_n_backspace(int n) {
	return n * 2 + B - A + 1 + B + 1;
}

int get_actual_binary_len_without_heading_zero(int x, int expected_len = 0) {
	//int expected = pow(2, expected_len + 1);
	return 0;
}


static string process(int caseNum, fstream & in) {
	char buf[10240];
	string temp_str = "";
	string result = "";

	in >> A >> B;

	p_i = new double [A];
	for(int i=0; i<A; i++) {
		in >> p_i[i];
	}

	double total = 0;
	// continue typing.
	total = calc_correct_property_press_n_backspace(0) * (B - A + 1) + (1 - calc_correct_property_press_n_backspace(0)) * (B - A + 1 + B + 1);
	// directly press enter.
	if(total > B + 2)
		total = B + 2;
	// press backspace.
	for(int i=1; i<=A; i++) {
		double temp = calc_correct_property_press_n_backspace(i) * calc_keystrike_if_correct_press_n_backspace(i) + (1 - calc_correct_property_press_n_backspace(i)) * calc_keystrike_if_incorrect_press_n_backspace(i);
		if(total > temp)
			total = temp;
	}
//	total /= A + 1;

//	int threshold = ceil(((double)A+1.0) / 2.0) - 1;
//	cout << "t:" << threshold << endl;
//
//	double fai = 0;
//	double ave = 0;
//	for(int i=0; i<=threshold; i++) {
//		double p = 1;
//		for(int j=0; j<A; j++) {
//			if(j<A-i) {
//				p *= p_i[j];
//			} else {
//				p *= (1-p_i[j]);
//			}
//		}
//		cout << p << endl;
//		fai += p;
//		cout <<  p * (i * 2 + B - A + 1) << endl;
//		ave += p * (i * 2 + B - A + 1);
//	}
//	ave += (1 - fai) * (B + 2);

	sprintf(buf, "%f", total);
	temp_str = buf;

	delete p_i;

	sprintf(buf, "Case #%d: %s\n", caseNum + 1, temp_str.c_str());
	result.append(buf);
	return result;
}

int main() {
	int caseNum = 0;
	fstream in("/home/festony/Downloads/codejam/testin.txt");
	fstream out("/home/festony/Downloads/codejam/testout.txt");


	in >> caseNum;
	in.ignore(256, '\n');
	char buf[10240];

	string result = "";

	for(int i=0; i<caseNum; i++) {
		result.append(process(i, in));
	}
	cout << result;
	out << result;
	in.close();
	out.close();

//	cout << get_binary_one_count(654564) << endl;
//	cout <<

	return 0;
}


