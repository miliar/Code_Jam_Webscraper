/*
 * Question: Find words matching the pattern
 * Author: Divye Kapoor
 * Date: 3 Sep 2009
 * 
 */
#include <iostream>
#include <cstring>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <vector>
#include <list>
#include <algorithm>
#include <functional>
#include <iterator>
#include <utility>
#include <stack>
#include <cstdio>
#include <cstdlib>
#include <iomanip>
#include <cassert>
#include <sstream>

using namespace std;

#define FOR(i, l, u) for(int i =(int)(l); i < (int)(u); ++i)
#define REP(i, u) FOR(i, 0, u)
#define LET(x, a) __typeof(a) x(a)
#define IFOR(it, b, e) for(LET(it,b); it != e; ++it)
#define SHIFTL(i, n) ((i) << (n))
#define SHIFTR(i, n) ((i) >> (n))
#define POW2(n) (1 << (n))

typedef vector<int> v_i;
typedef vector<string> v_s;
typedef set<int> set_i;
typedef set<string> set_s;
typedef map<string,int> map_si;
typedef pair<int,int> p_i;

int L, D, N;
set<string> dict;
int main() {
	string s;
	scanf("%d %d %d", &L, &D, &N);
	getline(cin, s);
	REP(i, D) {
		getline(cin, s);
		dict.insert(s);
	}

	REP(cases, N) {
		set<string> localdict = dict;
		set<char> options;
		getline(cin, s); // pattern

		char c;
		int count = 0;
		istringstream i(s);
		while(count < L) {
			options.clear();
			i >> c;
			if(c == '(') {
				i >> c;
				while(c != ')') {
					options.insert(c);
                    i >> c;
				}
			} else 
				options.insert(c);

			list<set<string>::iterator> dellist;
			IFOR(k, localdict.begin(), localdict.end()) {
				if(options.find((*k)[count]) == options.end())
                    dellist.push_back(k);
			}

			IFOR(k, dellist.begin(), dellist.end()) {
				localdict.erase(*k);
			}
			count++;
		}
		printf("Case #%d: %d\n", cases+1, localdict.size());
	}

	return 0;
}
