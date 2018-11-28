// A.cpp : 定义控制台应用程序的入口点。
//
#include "stdafx.h"
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string>
#include <functional>
#include <fstream>
using namespace std;


int main()
{
	char chmap[250];
	char chmap_inverse[250];

	memset(chmap, 0, sizeof(chmap));
	memset(chmap_inverse, 0, sizeof(chmap_inverse));
	chmap[32] = 32;
	chmap['a'] = 'y';
	chmap['b'] = 'n';
	chmap['c'] = 'f';
	chmap['d'] = 'i';
	chmap['e'] = 'c';
	chmap['f'] = 'w';
	chmap['g'] = 'l';
	chmap['h'] = 'b';
	chmap['i'] = 'k';
	chmap['j'] = 'u';
	chmap['k'] = 'o';
	chmap['l'] = 'm';
	chmap['m'] = 'x';
	chmap['n'] = 's';
	chmap['o'] = 'e';
	chmap['p'] = 'v';
	chmap['q'] = 'z';
	chmap['r'] = 'p';
	chmap['s'] = 'd';
	chmap['t'] = 'r';
	chmap['u'] = 'j';
	chmap['v'] = 'g';
	chmap['w'] = 't';
	chmap['x'] = 'h';
	chmap['y'] = 'a';
	chmap['z'] = 'q';

	chmap_inverse[' ']=' ';

	for(char c='a'; c<='z'; c++)
		chmap_inverse[chmap[c]] = c;

	char chline[10000];
	ifstream inf("in.txt");
	ofstream outf("out.txt");
	inf.getline(chline, 10000);
	istringstream iss(chline);

	int cnt;
	iss>>cnt;
	for(int zi=0; zi<cnt; zi++)
	{
		inf.getline(chline, 10000);
		string ss = chline;
		outf<<"Case #"<<zi+1<<": ";
		for(int ci=0; ci<ss.length(); ci++)
			outf<<chmap_inverse[ss[ci]];
		outf<<endl;
	}

	inf.close();
	outf.close();
	return 0;
}

