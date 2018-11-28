#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <fstream>
#include <sstream>
#include <set>
#include <map>
#include <vector>
#include <list>
#include <algorithm>
#include <cstring>
#include <cmath>
#include <string>
#include <queue>
#include <bitset>		//UWAGA - w czasie kompilacji musi byc znany rozmiar wektora - nie mozna go zmienic
#include <cassert>
#include <iomanip>		//do setprecision
#include <ctime>
#include <complex>
using namespace std;

#define FOR(i,b,e) for(int i=(b);i<(e);++i)
#define FORQ(i,b,e) for(int i=(b);i<=(e);++i)
#define FORD(i,b,e) for(int i=(b)-1;i>=(e);--i)
#define REP(x, n) for(int x = 0; x < (n); ++x)

#define ST first
#define ND second
#define PB push_back
#define MP make_pair
#define LL long long
#define ULL unsigned LL
#define LD long double

const double pi = 3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342;

string in = "ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jvz";
string out = "our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give upq";

bool donein[30], doneout[30];

int main()
{
	REP(i,(int)in.length()) donein[in[i]-'a'] = 1;
	REP(i,(int)in.length()) doneout[out[i]-'a'] = 1;
	int T;
	cin >> T;
	string s; getline(cin,s);
	REP(c,T)
	{
		getline(cin,s);
		string res = "";
		REP(i,(int)s.length())
		{
			bool ok = 0;
			REP(j,(int)in.length()) if(s[i] == in[j]) { res += out[j]; ok = 1; break; }
			if(!ok) res += 'z';
		}
		cout << "Case #" << c+1 << ": " << res+"\n";
	}
	return 0;
}