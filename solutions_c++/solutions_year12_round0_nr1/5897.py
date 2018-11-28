#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>
#include <fstream>

typedef long long ll;

using namespace std;

#define INF (1<<29)

int main(){
	freopen( "A-small-attempt1.in", "r", stdin );
	freopen( "output2.txt", "w", stdout );
	
	int T; cin >> T;
	string str;

	map<char, char> Map;
	string s = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
	string t = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";
	for ( int i = 0; i < (int)s.size(); i++ ){
		Map[s[i]] = t[i];
	}
	Map['q'] = 'z';
	Map['z'] = 'q';
	
	getline(cin, str);
	for ( int i = 0; i < T; i++ ){
		getline(cin, str);
		string res = "";
		for ( int j = 0; j < (int)str.size(); j++ ){
			res += Map[str[j]];
		}
		printf("Case #%d: %s\n", i+1, res.c_str());
	}
}