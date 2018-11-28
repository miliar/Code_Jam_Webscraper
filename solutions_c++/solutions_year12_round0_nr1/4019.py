#define _CRT_SECURE_NO_WARNINGS
#define _USE_MATH_DEFINES
#pragma comment(linker, "/STACK:16777216")

#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <iostream>
#include <map>
#include <stack>
#include <set>
#include <queue>
#include <numeric>
#include <algorithm>
#include <utility>
#include <bitset>
#include <cmath>
#include <sstream>
#include <fstream>

#define all(a) (a).begin(),(a).end()
#define sz(a) (int)(a).size()

using namespace std; 

typedef long long int64;
typedef vector<int> vi;
typedef vector< vi > vvi;
typedef vector<double> vd;
typedef vector< vd > vvd;
typedef vector< string > vs;
typedef pair< int, int > pii;
typedef vector< pii > vpii;


char a[26] = {
	'y', //a
	'n', //b
	'f', //c
	'i', //d
	'c', //e
	'w', //f
	'l', //g
	'b', //h
	'k', //i
	'u', //j
	'o', //k
	'm', //l
	'x', //m
	's', //n
	'e', //o
	'v', //p
	'z', //q
	'p', //r
	'd', //s
	'r', //t
	'j', //u
	'g', //v
	't', //w
	'h', //x
	'a', //y
	'q' //z
};
char b[26];
string Convert(string &s)
{
	string sout(s);
	for (int i = 0; i < sz(s); i++)
	{
		if (!isalpha(sout[i]))
			continue;
		sout[i] = b[sout[i] - 'a'];
	}
	return sout;
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif
	for (int i = 0; i < 26; i++)
		b[a[i] - 'a'] = 'a' + i;
	int t = 0;
	cin >> t;
	for (int i = 0; i < t; i++)
	{
		cout << "Case #" << i + 1 << ": ";
		string s = "";
		while (s == "")
			getline(cin, s);
		cout << Convert(s) << endl;
	}
	return 0;
}