#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include<fstream>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
#include <string.h>
#define rep(x,n) for(int x=0;x<n;++x)
#define rep1(i,s) for(int i = 0; i < (int)s.size(); ++i)
#define mp(x,y) make_pair(x,y)
#define getBit(code, i) (code & (1 << i))
#define setBit(code, i) (code | (1 << i))
#define resetBit(code, i) (code & ~(1 << i))
#define PI acos(-1.0)
#define rd(x) scanf("%d", &x)
using namespace std;


int main()
{
	freopen("input.in", "rt", stdin);
	freopen("output.in", "w", stdout);
	string e[] = {"ejp mysljylc kd kxveddknmc re jsicpdrysi", "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "de kr kd eoya kw aej tysr re ujdr lkgc jv"};
	string d[] = {"our language is impossible to understand", "there are twenty six factorial possibilities", "so it is okay if you want to just give up"};
	map<char, char> mp;
	
	rep(i, 3)
		rep1(j, e[i])
			mp[e[i][j]] = d[i][j];
	mp['z'] = 'q';
	mp['q'] = 'z';
	int cases;
	cin >> cases;
	cin.ignore();
	string inp;
	rep(i, cases)
	{
		cout << "Case #" << i + 1 << ": ";
		getline(cin, inp);
		rep1(i, inp)
			cout << mp[inp[i]];
		cout << endl;
	}
	return 0;
}