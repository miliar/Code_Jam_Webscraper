#include <iostream>
#include <stdio.h>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <utility>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>

using namespace std;

#define ff(i,x,y) for(int i = (x);i < (y);++i)
#define rep(i,n) ff(i,0,n)
#define st(v) sort(v.begin(),v.end())
#define st2(v,f) sort(v.begin(),v.end(),f)
#define rvs(v) reverse(v.begin(),v.end())
#define cnt(v,n) count(v.begin(),v.end(),n)
#define pb push_back
bool myfunction (int i,int j) { return (i<j); }
#define fact(x) for(i=x-1;i>0;i--){x=x*i;}
#define F first
#define S second
#define LL long long
#define ULL unsigned long long
#define VI vector<int>
#define VVI vector<VI>

#define LOCAL 1
#ifdef LOCAL
ifstream in("in.txt");
#else
in = &cin;
#endif

map<char,char> onto;
int T;
string S;

string solve(string s)
{
	string res;
	res.resize(s.size());
	for(int i = 0;i < s.size();++i)
	{
		if(s[i] == ' ')
			res[i] = s[i];
		else
			res[i] = onto[s[i]];
	}
	return res;
}

int main()
{
	onto['y'] = 'a';
	onto['n'] = 'b';
	onto['f'] = 'c';
	onto['i'] = 'd';
	onto['c'] = 'e';
	onto['w'] = 'f';
	onto['l'] = 'g';
	onto['b'] = 'h';
	onto['k'] = 'i';
	onto['u'] = 'j';
	onto['o'] = 'k';
	onto['m'] = 'l';
	onto['x'] = 'm';
	onto['s'] = 'n';
	onto['e'] = 'o';
	onto['v'] = 'p';
	onto['z'] = 'q';
	onto['p'] = 'r';
	onto['d'] = 's';
	onto['r'] = 't';
	onto['j'] = 'u';
	onto['g'] = 'v';
	onto['t'] = 'w';
	onto['h'] = 'x';
	onto['a'] = 'y';
	onto['q'] = 'z';
	ofstream fout;
	fout.open("output.txt");
	in >> T;

	char tmp[102];
	in.getline(tmp,102);
	for(int i = 0;i < T;++i)
	{
		memset(tmp,'\0',sizeof tmp);
		in.getline(tmp,102);
		S = tmp;
		fout << "Case #" << i+1 << ": " << solve(S) << endl;
	}
	fout.close();
	return 0;
}