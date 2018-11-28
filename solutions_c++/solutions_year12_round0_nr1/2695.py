#include <climits>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <cmath>
#include <algorithm>
#include <iostream>
#include <iomanip>
#include <numeric>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <set>
#include <map>

using namespace std;

#define REP(i,n)    for(int i=1;i<=(n);++i)
#define FORE(i,e,n) for(int i=(e);i<(n);++i)
#define FOR(i,n)    for(int i=0;i<(n);++i)

#define _(A,v) memset(A,v,sizeof(A))
#define all(A)  (A).begin(), (A).end()
#define rall(A) (A).rbegin(),(A).rend()
#define pb push_back

int main() {
	freopen("d.in",  "r", stdin);
	freopen("d.out", "w", stdout);

	int l;
	string IN;
	string OUT;
	char A[27];
	char BUFF[128];

	A['a' - 'a'] = 'y';
	A['b' - 'a'] = 'h';
	A['c' - 'a'] = 'e';
	A['d' - 'a'] = 's';
	A['e' - 'a'] = 'o';
	A['f' - 'a'] = 'c';
	A['g' - 'a'] = 'v';
	A['h' - 'a'] = 'x';
	A['i' - 'a'] = 'd';
	A['j' - 'a'] = 'u';
	A['k' - 'a'] = 'i';
	A['l' - 'a'] = 'g';
	A['m' - 'a'] = 'l';
	A['n' - 'a'] = 'b';
	A['o' - 'a'] = 'k';
	A['p' - 'a'] = 'r';
	A['q' - 'a'] = 'z';
	A['r' - 'a'] = 't';
	A['s' - 'a'] = 'n';
	A['t' - 'a'] = 'w';
	A['u' - 'a'] = 'j';
	A['v' - 'a'] = 'p';
	A['w' - 'a'] = 'f';
	A['x' - 'a'] = 'm';
	A['y' - 'a'] = 'a';
	A['z' - 'a'] = 'q';

	int tt;
	cin>>tt;
	cin.ignore(1, '\n');
	REP(t,tt) {
		printf("Case #%d: ", t);
		cin.getline(BUFF, 101);
		IN = BUFF;
		OUT = "";
		l = IN.length();
		FOR(i, l) {
			if(IN[i] == ' ') OUT += ' ';
			else OUT += A[IN[i] - 'a'];
		}
		cout << OUT << endl;
	}
	return 0;
}
