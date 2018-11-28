#include <iostream>
#include <string>
#include <vector>
#include <cstring>
#include <set>
#include <map>
#include <algorithm>
#include <utility>
#include <numeric>
#include <cmath>
#include <sstream>
#include <stack>
#include <queue>
using namespace std;

typedef pair<int,int> pii;
typedef pair<int,string> pis;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<pii> vpii;
typedef vector<vpii> vvpii;
typedef vector<string> vs;
typedef set<int> si;
typedef map<int,int> mii;
typedef map<int,string> mis;
typedef map<string,int> msi;
typedef long long ll;
typedef unsigned long long ull;
#define foreach(var, container) for(typeof((container).begin()) var = (container).begin(); var != (container).end(); ++var)
#define FOR(v, t) for(int v=0; v<int(t); ++v)
#define RNG(v, f, t) for(int v=int(f); v<=int(t); ++v)
#define MIN(x,y) std::min(x,y)
#define MAX(x,y) std::max(x,y)

map<char,char> m;

int main()
{
	string g,e;
	g = "qz ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
	e = "zq our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";
	FOR(i, g.size()) m[g[i]]=e[i];
	cerr<<"size "<<m.size()<<endl;
	int T; cin>>T; cin.ignore(999, '\n');
	FOR(t, T)
	{
		char st[110];
		cin.getline(st, 105, '\n');
		cout<<"Case #"<<t+1<<": ";
		for(int i=0; st[i]; i++)
			cout<<m[st[i]];
		cout<<endl;
	}
	return 0;
}
