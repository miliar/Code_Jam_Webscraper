#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>

using namespace std;

#define FOR(i,a,b)	for(int i=(a); i<(b); ++i)
#define REP(iter,v) for(typeof((v).begin()) iter = (v).begin(); iter != (v).end(); ++iter)
#define MP make_pair
#define PB push_back
#define SZ size()
#define iss istringstream 

#define SORT(x) sort(x.begin(), x.end())
#define ALL(x) x.begin(), x.end()
#define UNIQUE(x) x.erase(unique(x.begin(),x.end()),x.end()) 
#define dbg(x) cerr << #x << " -> '" << (x) << "'\t"
#define dbge(x) cerr << #x << " -> '" << (x) << "'\n"

typedef long long ll, int64;
typedef vector<int> VI;

int64 INF = 1000*1000*1001;

set<string> dict;

int main(void)	{
	int L, D, N;
	cin >> L >> D >> N;
	
	string s;
	
	FOR (k, 0, D)	{
		cin >> s;
		dict.insert(s);
	}
	

	FOR (nc, 1, N+1)	{
		cin >> s;

		set<char> lst[20];
		int idx = 0;	
		bool open = false;
		FOR (i, 0, s.size())	{
			if (s[i] == ')')	{
				idx++;
				open = false;
			}
			else if (s[i] == '(')	open = true;
			else {
				lst[idx].insert(s[i]);
				if (!open)	idx++;
			}
		}
		
		int cnt = 0;
		REP (iter, dict)	{
			string word = *iter;
			bool flag = true;
			FOR (i, 0, L)	{
				if (lst[i].find(word[i]) == lst[i].end())	{
					flag = false;
					break;
				}
			}
			if (flag)	cnt++;
		}
		cout << "Case #" << nc << ": " << cnt << endl;
	}
}
