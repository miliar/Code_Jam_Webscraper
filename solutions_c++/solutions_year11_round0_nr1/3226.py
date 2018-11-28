// Bottrust.cpp : Defines the entry point for the console application.
//
#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <sstream>
#include "stdafx.h"
#include <windows.h>

using namespace std;

template <typename T>
std::string toStr(const T &value) {
	std::stringstream str;
	str << value;
	return str.str();
}

template <typename T>
T toT(const std::string &value) {
	std::stringstream str(value);
	T tval;
	str >> tval;
	return tval;
}

unsigned int compute(){
	unsigned int pos[2], credit[2];
	for (int i = 0; i < 2; ++i) {
		pos[i]    = 1;
		credit[i] = 0;
	}
	unsigned int switches = 0;
	cin >> switches;
	unsigned int secs = 0;
	for (int i = 0; i < switches; i++) {
		char ch;
		int  location;
		cin >> ch;
		cin >> location;
		const unsigned int robot = (ch == 'O')? 0:1;
		int distance = pos[robot] - location;
		distance = (distance >=0)? distance:(-1*distance);
		distance = distance - credit[robot];
		credit[robot] = 0;
		distance = (distance >=0)? distance:(0);
		credit[!robot] = credit[!robot] + distance + 1;
		secs += distance + 1;
		pos[robot] = location;
	}
	return secs;
}

int _tmain(int argc, _TCHAR* argv[])
{
	unsigned int T = 0;
	cin >> T;
	//Sleep(9000);
	for (int i = 0; i < T; ++i) {
		cout << "Case #" << i+1 << ": " << compute() << std::endl;
	}
	return 0;
}

