// BEGIN CUT HERE

// END CUT HERE
#include <algorithm>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <cstring>
#include <climits>
using namespace std;
#define PB push_back
#define MP make_pair
#define REP(i,n) for(i=0;i<(n);++i)
#define FOR(i,l,h) for(i=(l);i<=(h);++i)
#define FORD(i,h,l) for(i=(h);i>=(l);--i)
#define foreach(itr, cont) for (typeof(cont.begin()) itr = cont.begin(); itr != cont.end(); itr++)
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
typedef long long LL;
typedef pair<int,int> PII;

static const string from("ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv");
static const string to("our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up");
		
int mp[256];
int used[256];
void build_map() {
	memset(mp, -1, sizeof(mp));

	memset(used, 0, sizeof(used));
	for (int i = 0; i < from.length(); i ++) {
		//if (mp[from[i]] != -1 && mp[from[i]] != to[i]) cout << "error" << endl;
		mp[from[i]] = to[i];
		used[to[i]] = 1;
	}

	/*
	int dest = 0, src = 0;
	for (int i = 'a'; i <= 'z'; i ++) {
		if (mp[i] == -1) src = i;
		if (used[i] == 0) dest = i;
	}
	mp[src] = dest;
	*/
	mp['z'] = 'q';
	mp['q'] = 'z';
}

int main() {
	int N;
	//string str;
	char str[256];
	int size;

	ifstream in("A-small-attempt3.in");
	ofstream out("A-small-attempt3.out");

	build_map();
	in >> N;
	in.getline(str, 256);
	for (int cs = 1; cs <= N; cs ++) {
		out << "Case #" << cs << ": ";
		in.getline(str, 256);
		size = strlen(str);
		//cout << str << endl;
		for (int i = 0; i < size; i ++) {
			//if (mp[str[i]] == -1) cout << endl << "error" << endl;
			out << (char)mp[str[i]];
		}
		out << endl;
	}
	return 0;
}
