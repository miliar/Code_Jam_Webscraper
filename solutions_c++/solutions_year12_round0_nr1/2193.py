#include <cstdio>
#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <cstring>
#include <string>
#include <queue>
#include <algorithm>
#include <cmath>
#include <sstream>
using namespace std;
#define PB push_back
#define REP(i,n) for(int i=0;i<(n);i++)
#define FOR(i,a,b) for(int i=(a);i<=(b);i++)
#define FORD(i,a,b) for(int i=(a);i>=(b);i--)
#define FORE(i,x) for(__typeof((x).begin()) i=(x).begin();i != (x).end();++i)
#define ALL(x) (x).begin(),(x).end()
#define CLR(x,w) memset((x),w,sizeof (x))
#define X first
#define Y second
typedef long long int lli;
typedef pair<int, int> P;
typedef vector<int> VI;

string a="ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jvzq\0";
string b="our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give upqz\0";

string s,w;
map<char, char> M;

int main(){ 
	int T;
	cin >> T;
	getline(cin,s);
	REP(i,a.size())
		M[a[i]] = b[i];
	FOR(t,1,T){
		cout << "Case #" << t << ":";
		getline(cin, s);
		stringstream ss(s);
		while(ss >> w) {
			FORE(i,w) *i = M[*i];
			cout << " " << w;
		}
		cout << endl;
	}
	//in
	//sol
	//out
    return 0;
}
