#include <iostream>
#include <stdio.h>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <math.h>
#include <algorithm>
#include <map>
#include <set>
#include <limits.h>
#include <memory.h>

using namespace std;

#define LL              	long long
#define pb              	push_back
#define mp              	make_pair
typedef vector <int> 		vi;
typedef vector <string> 	vs;
typedef pair   <int,int>    pii;

int k,res,len;
string s;

int cnt(const string& s)
{
	int r = 1;
	for (int i=1; i<s.length(); i++) if (s[i]!=s[i-1]) r++;
	return r;
}

void process()
{
	int i,j;
	vi p;

	for (i=0; i<k; i++) p.pb(i);

	len = s.length();
	string tmp(len,' ');

	res = INT_MAX;
	do {
		for (i=0; i<len; i+=k)
		{
			for (j=0; j<k; j++) tmp[i+j] = s[i+p[j]];
		}
		res = min(res, cnt(tmp));
	} while (next_permutation(p.begin(),p.end()));
}

int main()
{
	int numtest;

	cin >> numtest;
	for (int i=1; i<=numtest; i++)
	{
		cin >> k >> s;
		process();
		cout << "Case #" << i << ": " << res << endl;
	}
	return 0;
}
