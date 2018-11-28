// jam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <string>
#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <map>

using namespace std;

static const string str = "welcome to code jam";
int DP[510][30];
int mem[510][30];
string s;
int slen;

int calc(int si, int pi)
{
	if (pi>=str.length()) return 1;
	if (si>=slen) return 0;
	if (mem[si][pi]) return DP[si][pi];

	int val = 0;
	for (int i=si;i<slen;i++)
		if (s[i]==str[pi])
		{
			val += calc(i+1, pi+1);
			val = val%10000;
		}

	mem[si][pi] = 1;
	DP[si][pi] = val;
	return val;
}

int _tmain(int argc, _TCHAR* argv[])
{
	int N;
	char buf[65536];
	cin >> N;
	cin.getline(buf, 65536);
	for (int i=0;i<N;i++)
	{
		cin.getline(buf, 65536);
		s = buf;
		slen = s.length();
		memset(DP, 0, sizeof(DP));
		memset(mem, 0, sizeof(mem));
		int res = calc(0, 0);
		cout << "Case #" << (i+1) << ": ";
		if (res<1000) cout << "0";
		if (res<100) cout << "0";
		if (res<10) cout << "0";
		cout << res << endl;
	}

	return 0;
}

