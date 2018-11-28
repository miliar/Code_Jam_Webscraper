//  Speaking in Tongues.cpp
//  12/04/14.

#if 1

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <ctime>
#include <cassert>
#include <iostream>
#include <cctype>
#include <sstream>
#include <string>
#include <list>
#include <vector>
#include <queue>
#include <set>
#include <stack>
#include <map>
#include <utility>
#include <numeric>
#include <algorithm>
#include <iterator>
#include <bitset>
#include <complex>
#include <fstream>
using namespace std;
typedef long long ll;
const double EPS = 1e-9;
typedef vector<int> vint;
typedef pair<int, int> pint;
#define rep(i, n) REP(i, 0, n)
#define ALL(v) v.begin(), v.end()
#define MSG(a) cout << #a << " " << a << endl;
#define REP(i, x, n) for(int i = x; i < n; i++)
template<class T> T RoundOff(T a){ return int(a+.5-(a<0)); }
template<class T, class C> void chmax(T& a, C b){ if(a < b) a = b; }
template<class T, class C> void chmin(T& a, C b){ if(b < a) a = b; }
template<class T, class C> pair<T, C> mp(T a, C b){ return make_pair(a, b); }

int main()
{
	map<char, char> table;
	string str[3][2] = 
	{
		{"ejp mysljylc kd kxveddknmc re jsicpdrysizq", "our language is impossible to understandqz"},
		{"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "there are twenty six factorial possibilities"},
		{"de kr kd eoya kw aej tysr re ujdr lkgc jv", "so it is okay if you want to just give up"}
	};
	
	rep(i, 3) rep(j, str[i][0].size()) if(str[i][0][j] != ' ') table[str[i][0][j]] = str[i][1][j];
	
	table[' '] = ' ';
	
    int T;
	cin >> T;
	cin.ignore();
	
	for(int caseNumber = 1; caseNumber <= T; caseNumber++)
	{
		string line;
		getline(cin, line);
		
		rep(i, line.size()) line[i] = table[line[i]];
		
		cout << "Case #" << caseNumber << ": " << line << endl;
	}
}

#endif