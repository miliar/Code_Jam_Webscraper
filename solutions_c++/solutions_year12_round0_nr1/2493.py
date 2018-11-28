//============================================================================
// Name        : Speaking.cpp
// Author      : alpc92
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;

#define PB push_back
#define MP make_pair
#define inf 0x3fffffff
#define REP(iterator,upperbound) for(int iterator(0);iterator<(upperbound);++iterator)
#define FOR(iterator,lowerbound,upperbound) for(int iterator(lowerbound);iterator<=(upperbound);++iterator)
#define FORD(iterator,upperbound,lowerbound) for(int iterator(upperbound);iterator>=(lowerbound);--iterator)
#define FORIT(iter,STL) for (typeof(STL.begin()) iter(STL.begin());iter!=STL.end();++iter)
#define SIZE(STL) ((int)STL.size())
#define CLEAR(STL) (STL.clear())
#define CLEAR0(array) memset(array,0,sizeof(array))
#define CLEAR1(array) memset(array,-1,sizeof(array))
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
typedef long long LL;
typedef pair<int, int> PII;
#define MAXLOOP 100
#define WORKERNUM 10
#define UPNUM 4
#define DOWNNUM 2
#define PASSWAY 1
template<class T>
inline void chkmax(T &a, T b) {
	if (a < b)
		a = b;
}
template<class T>
inline void chkmin(T &a, T b) {
	if (a > b)
		a = b;
}
string
		s1 =
				"ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv";
string
		s2 =
				"our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up";
int main() {
	map<char, char> mp;
	REP(i,(int)s1.size())
		mp[s1[i]] = s2[i];
	mp['z'] = 'q';
	mp['q']='z';
	FORIT(it,mp)printf("%c %c\n",it->first,it->second);
	printf("%d\n",(int)mp.size());
	int n;
	char s[200];
	freopen("in", "r", stdin);
	freopen("out.txt", "w", stdout);
	scanf("%d", &n);
	getchar();
	REP(cases,n) {
		gets(s);
		REP(i,strlen(s))
			s[i] = mp[s[i]];
		printf("Case #%d: %s\n", cases + 1, s);
	}
	return 0;
}
