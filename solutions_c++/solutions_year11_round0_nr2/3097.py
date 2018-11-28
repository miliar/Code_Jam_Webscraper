// Bottrust.cpp : Defines the entry point for the console application.
//
#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <set>
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

char attract[40][40];
char product[40];
char repel[40][40];
char arr[101];

std::set<char> base;

int checkCombine(char ch, int C, int len) {
	bool combine = false;
	//for (int i = 0 ; i < len; ++i) {
		int i = len - 1;
		if (base.find(arr[i]) != base.end()) {
			//continue;

		for (int j = 0; j < C; ++j) {
			if ( (attract[j][0] == arr[i] && attract[j][1] == ch) ||
				(attract[j][1] == arr[i] && attract[j][0] == ch) ) {
				arr[i] = product[j];
				combine = true;
				break;
			}
		}
		}
		//if (combine) break;
	//}
	if (!combine) {
		arr[len] = ch;
		len++;
		arr[len] = '\0';
	}
	return len;
}

int checkRepel(int D, int len) {
	bool clear = false;
	char ch = arr[len-1];
	for (int i = 0 ; i < len-1; ++i) {
		if (base.find(arr[i]) == base.end())
			continue;

		for (int j = 0; j < D; ++j) {
			if ( (repel[j][0] == arr[i] && repel[j][1] == ch) ||
				(repel[j][1] == arr[i] && repel[j][0] == ch) ) {
				clear = true;
				break;
			}
		}
		if (clear) break;
	}
	if (clear) {
		arr[0] = '\0';
		len = 0;
	}
	return len;

}

void compute() {
	unsigned int C = 0;
	cin >> C;
	for (int i = 0; i < C; ++i) {
		std::string tmp;
		cin >> tmp;
		attract[i][0] = tmp[0];
		attract[i][1] = tmp[1];
		product[i] = tmp[2];
	}

	unsigned int D = 0;
	cin >> D;
	for (int i = 0; i < D; ++i) {
		std::string tmp;
		cin >> tmp;
		repel[i][0] = tmp[0];
		repel[i][1] = tmp[1];
	}
	
	unsigned int N = 0;
	cin >> N;
	std::string tmp;
	cin >> tmp;
	arr[0] = '\0';
	
	int len = 0;
	for (int i = 0; i < N; ++i) {
		len = checkCombine(tmp[i], C, len);
		len = checkRepel(D, len);
	}

	cout << "[";
	for (int i = 0 ; i < 101; ++i) {
		if (arr[i] == '\0')
			break;
		if (i != 0) cout << ", ";
		cout << arr[i];
	}
	cout << "]" <<endl;
}

int _tmain(int argc, _TCHAR* argv[])
{
	base.insert('Q');
	base.insert('W');
	base.insert('E');
	base.insert('R');
	base.insert('A');
	base.insert('S');
	base.insert('D');
	base.insert('F');
	unsigned int T = 0;
	cin >> T;
	//Sleep(9000);
	for (int i = 0; i < T; ++i) {
		cout << "Case #" << i+1 << ": ";
		compute();
	}
	return 0;
}

/*
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
}*/