#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
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
#include <iostream>
#include <climits>
#include <cstring>
#include <fstream>
using namespace std;

#define forn(a, n) for(int a = 0; a<(n); ++a)
#define forsn(a,s,n) for(int a = (s); a<(n); ++a)
#define forall(a, all) for(typeof((all).begin()) a = (all).begin(); a != (all).end(); ++a)

#define dforn(a, n) for(int a = (n)-1; a>=0; --a)
#define dforsn(a,s,n) for(int a = (n)-1; a>=(s); --a)
#define dforall(a, all) for(typeof((all).rbegin()) a = (all).rbegin(); a != (all).rend(); ++a)

#define contains(mask, bit) ((mask & (1LL<<bit)) != 0LL)

typedef long long tint;

string in = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jvzoq";
string out = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give upqkz";
int main()
{
#ifdef __YO__
	freopen("A-small.in", "r", stdin);
	freopen("A-small.out", "w", stdout);
#endif
	
	int T;
	string str;
	cin >> T;
	getline(cin, str);
	
	map<char, char> mm;
	forn(i, in.size())
		mm[in[i]] = out[i];
	
	forn(t, T){
		getline(cin, str);
		cout << "Case #" << t+1 << ": ";
		forn(i, str.size()) cout << char(mm[str[i]]);
		cout << endl;
	}

	return 0;
}
