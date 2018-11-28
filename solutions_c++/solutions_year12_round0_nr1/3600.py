/*
 this code was written by Zanaty
 problem kind:
 */
#include<iostream>
#include<string.h>
#include<vector>
#include<stack>
#include<queue>
#include<algorithm>
#include<stdio.h>
#include<set> 
#include<cmath>
#include<fstream>
#include<memory.h>
#include<map>
#include<sstream>
#define OO 10e8
using namespace std;
int main() {
#ifndef ONLINE_JUDGE
	freopen("A-small-attempt1.in", "rt", stdin);
	freopen("res1.txt", "wt", stdout);
#endif
	int arr2[] = { 24, 7, 4, 18, 14, 2, 21, 23, 3, 20, 8, 6, 11, 1, 10, 17, 25,
			19, 13, 22, 9, 15, 5, 12, 0, 16 };
	int test;
	cin >> test;
	string temp;
	getline(cin,temp );
	for (int tt = 1; tt <= test; tt++) {
		string s1, s2;
		getline(cin, s1);

		for (int k = 0; k < s1.length(); k++) {
			if (s1[k] != ' ')
				s2 += arr2[s1[k] - 'a'] + 'a';
			else
				s2 += ' ';
		}

		cout <<"Case #"<<tt<<": "<< s2 << endl;

	}
	return 0;
}
