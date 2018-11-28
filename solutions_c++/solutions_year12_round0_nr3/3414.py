// 2012_Q_A.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <set>
#include <string>
#include <map>
#include <fstream>
#include <iostream>

using namespace std;

set<size_t> nos;
size_t count(size_t number, size_t min, size_t max);

int _tmain(int argc, _TCHAR* argv[]) {

	size_t T = 0;
	cin >> T;
	for (size_t j = 0; j < T; ++j) {
		nos.clear();
		size_t A = 0;
		size_t B = 0;
		cin >> A;
		cin >> B;
		size_t counter = 0;
		for (size_t i = A ; i < B; ++i) {
			if (nos.find(i) == nos.end())
				counter += count(i, A, B);
		}
		cout << "Case #" << j+1 << ": " << counter << endl;

	}
	return 0;
}

size_t getsize(size_t max) {
	size_t size = 0;
	if (0 == max) 
		return size;
	do {
		size++;
		max /= 10;
	}while(max != 0);
	return size;
}

size_t pow(size_t value) {
	size_t powv = 1;
	while (value-- != 0) 
		powv *= 10;
	return powv;
}

size_t factorial(size_t value) {
	if (value == 0) return 1;
	static map<size_t, size_t> facmap;
	map<size_t, size_t>::iterator itr = facmap.find(value);
	if (itr != facmap.end()) return itr->second;
	facmap[value] = value * factorial(value -1);
	return facmap[value];
}

size_t count(size_t number, size_t min, size_t max) {
	size_t org = number;
	set<size_t> track;
	track.insert(number);
	const size_t size = getsize(number);
	size_t pos = 1;
	for (size_t i = 0; i < size; ++i) {
		const size_t psize = getsize(number);
		if (psize < size)
			number *= 10;
		else {
			const size_t powv = pow(size -1);
			const size_t left = number/powv;
			number = number - left *powv;
			number = number * 10 + left;
		}
		const size_t nsize = getsize(number);
		if (nsize != size) continue;
		if (number <= max && number >= min && (track.find(number) == track.end()) ) {
			pos++;
			nos.insert(number);
			track.insert(number);
		}
	}
	if (pos == 1) 
		return 0;
	nos.insert(org);
	return factorial(pos)/(factorial(2) * factorial(pos-2));

}