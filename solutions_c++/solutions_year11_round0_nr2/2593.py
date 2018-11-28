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
using namespace std;

#define forn(a, n) for(int a = 0; a<(n); ++a)
#define forsn(a,s,n) for(int a = (s); a<(n); ++a)
#define forall(a, all) for(typeof((all).begin()) a = (all).begin(); a != (all).end(); ++a)

#define dforn(a, n) for(int a = (n)-1; a>=0; --a)
#define dforsn(a,s,n) for(int a = (n)-1; a>=(s); --a)
#define dforall(a, all) for(typeof((all).rbegin()) a = (all).rbegin(); a != (all).rend(); ++a)

#define contains(mask, bit) ((mask & (1LL<<bit)) != 0LL)

typedef long long tint;

map<char, set<char> > need, op;
map<pair<char, char>, char> result;

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	
	int T;
	cin >> T;
	
	forn(p, T){
		int c,d,n;
		string elements;
		cin >> c;
		need.clear(); op.clear(); result.clear();
		forn(i, c){
			string str;
			cin >> str;
			need[str[0]].insert(str[1]);
			need[str[1]].insert(str[0]);
			result[make_pair(min(str[0], str[1]), max(str[0], str[1]))] = str[2];
		}
		
		cin >> d;
		forn(i, d){
			string str;
			cin >> str;
			op[str[0]].insert(str[1]);
			op[str[1]].insert(str[0]);
		}
		
		cin >> n >> elements;
		string ret;
		
		forn(i, n){
			char kn = ret[ret.size()-1];
			if(need[kn].count(elements[i])){
				ret = ret.substr(0, ret.size()-1);
				ret += result[make_pair(min(kn, elements[i]), max(kn, elements[i]))];
			}else
				ret += elements[i];
			
			forn(j, ret.size())
				if(op[ret[ret.size()-1]].count(ret[j]))
					ret = "";
			
//			cout << ret << endl;
		}
		
		printf("Case #%i: [", p+1);
		forn(i, ret.size()){
			if(i)
				printf(", ");
			printf("%c", ret[i]);
		}
		printf("]\n");
	}

	return 0;
}
