// Intersect.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <map>

using namespace std;

int T;
map<int, int, greater<int>> dict;

ifstream in;
ofstream out;

#define cin in
#define cout out

int _tmain(int argc, _TCHAR* argv[])
{
	in.open("A-small-attempt1.in");
	out.open("res.txt");
	cin >> T;
	int t = T;
	while(t-- > 0) {
		int N;
		cin >> N;
		for(; N > 0; --N) {
			int a, b;
			cin >> a >> b;
			dict[a] = b;
		}
		int currRight = -1;
		int count = 0;
		for(map<int, int, greater<int>>::iterator it = dict.begin();
			it != dict.end(); ++it) {
			if(currRight < 0) {
				currRight = (*it).second;
			} else {
				int right = (*it).second;
				if(right < currRight) {
					currRight = right;
				} else {
					map<int, int ,greater<int>>::iterator nit = it;
					while(nit != dict.begin() && (*--nit).second < right)
						count++;
				}
			}
		}
		dict.clear();
		cout << "Case #" << T - t << ": " << count << endl;
	}
	return 0;
}

