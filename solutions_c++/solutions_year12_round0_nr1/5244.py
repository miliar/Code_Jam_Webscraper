#include <algorithm>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <vector>
#include <iomanip>
#include <cmath>
#include <stack>
#include <utility>
#include <cstdlib>
#include <climits>
using namespace std;

#define REP(i, n) for(typeof(n) i=0;i<(n);++i)
#define FOR(i,a,b) for(typeof(b) i=a;i<=b;++i)
#define FORD(i,a,b) for(typeof(b) i=a;i>=b;--i)
#define SZ(x) ((int)((x).size()))
#define all(c) (c).begin(), (c).end()
#define pb push_back
#define foreach(it, c)for(typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define present(c,x) (find(all(c),x) != (c).end()) 

int main() {
	// freopen("A-small-attempt0.in","r",stdin);
	// freopen("out","w",stdout);
	string s = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
	string s2 = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";
	
	map<char,char> m;
	REP(i,s.size()) m[s[i]]=s2[i];
	m['z']='q';
	m['q']='z';
	// foreach(it,m) cout<<it->first<< " " <<it->second<<endl;
	int t;
	cin >> t;
	while(isspace(cin.peek())) cin.ignore();
	REP(i,t) {
		cout << "Case #"<<i+1<<": ";
		string line;
		getline(cin,line);
		REP(i,line.size()) cout << m[line[i]];
		cout<<endl;
	}
	return 0;
}


