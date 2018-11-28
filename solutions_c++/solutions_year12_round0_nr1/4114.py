
/***** Author : Kunal *****/
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>

#include <cmath>
#include <cstdio>
#include <queue>
#include <list>
#include <stack>
#include <utility>
#include <numeric>
#include <map>
#include <cctype>
#include <cstring>
#include <sstream>
#include <cstdlib>
#include <cassert>
#include <iomanip>
#include <set>
#include <fstream>

using namespace std;

#define REP(a,b) for(int a=0;a<b;a++)
#define FOR(a,b,c) for(int a=b;a<c;a++)
#define FORD(a,b,c) for(int a=b;a>=c;a--)

#define S scanf
#define P printf

#define LEN(x) ((int)x.length())
#define SZ(x) ((int)x.size())
#define ALL(x) x.begin(), x.end()
#define MP(x,y) make_pair(x,y)
#define PB(x) push_back(x)
#define INF 1000000000

typedef long long LL;
typedef pair<int,int> PII;
typedef pair<int, PII> PIII;
typedef vector<int> VI;
typedef vector<bool> VB;
typedef vector<string> VS;

//int d[][2]={{-1.0},{1,0},{0,-1},{0,1}};

char A[26];
void init() {
	A['a'-'a'] = 'y';
	A['b'-'a'] = 'h';
	A['c'-'a'] = 'e';
	A['d'-'a'] = 's';
	A['e'-'a'] = 'o';
	A['f'-'a'] = 'c';
	A['g'-'a'] = 'v';
	A['h'-'a'] = 'x';
	A['i'-'a'] = 'd';
	A['j'-'a'] = 'u';
	A['k'-'a'] = 'i';
	A['l'-'a'] = 'g';
	A['m'-'a'] = 'l';
	A['n'-'a'] = 'b';
	A['o'-'a'] = 'k';
	A['p'-'a'] = 'r';
	A['q'-'a'] = 'z'; //
	A['r'-'a'] = 't';
	A['s'-'a'] = 'n';
	A['t'-'a'] = 'w';
	A['u'-'a'] = 'j';
	A['v'-'a'] = 'p';
	A['w'-'a'] = 'f';
	A['x'-'a'] = 'm';
	A['y'-'a'] = 'a';
	A['z'-'a'] = 'q';
}

int main()
{
	init();
	int t; S("%d", &t);
	string str;
	getline(cin, str);
	REP(tc, t) {
		getline(cin, str);
		int l = LEN(str);
		REP(i, l) if(str[i]>='a' && str[i]<='z') str[i] = A[str[i]-'a'];
		cout << "Case #" << tc+1 << ": " << str << endl;
	}
	return 0;
}
