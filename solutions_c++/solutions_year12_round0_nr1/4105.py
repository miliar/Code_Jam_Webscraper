/*
 * main.cc
 *
 *  Created on: May 22, 2011
 *      Author: wujj
 */

#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <stdint.h>
#include <limits.h>
#include <map>

using namespace std;

const char *c1 = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
const char *c2 = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
const char *c3 = "de kr kd eoya kw aej tysr re ujdr lkgc jv";

const char *a1 = "our language is impossible to understand";
const char *a2 = "there are twenty six factorial possibilities";
const char *a3 = "so it is okay if you want to just give up";

map<char, char> qmap;

void codeJam();
void preProc();

int main() {

	preProc();

	int num_case;
	cin >> num_case;
	cin.get();

	for (int i = 0; i < num_case; i++) {
		cout << "Case #" << i+1 << ": ";
		codeJam();
	}

	return 0;
}

void codeJam() {

	char line[102];
	cin.getline(line, 101);
	char *p = line;
	while (*p) {
		cout << qmap[*p];
		p++;
	}
	cout << endl;

}

void preProc() {

	const char *pc = c1;
	const char *pa = a1;
	while (*pc) {
		qmap[*pc] = *pa;
		pc++;
		pa++;
	}
	pc = c2;
	pa = a2;
	while (*pc) {
		qmap[*pc] = *pa;
		pc++;
		pa++;
	}
	pc = c3;
	pa = a3;
	while (*pc) {
		qmap[*pc] = *pa;
		pc++;
		pa++;
	}

	qmap['q'] = 'z';
	qmap['z'] = 'q';

//	map<char, char>::iterator i;
//	for (i = qmap.begin(); i != qmap.end(); i++) {
//		cout << i->first << ":" << i->second << endl;
//	}

}
