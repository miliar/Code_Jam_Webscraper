#include <algorithm>
#include <fstream>
#include <string>
#include <queue>
#include <set>
#include <stack>
#include <map>
#include <sstream>
#include <iostream>
#include <cmath>
using namespace std;

typedef unsigned int uint;
typedef long long int64;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> pI;
typedef pair<string,int> pSI;
typedef pair<int,string> pIS;

#define FOR(i,n) for(int i=0, upTo##i=n; i<upTo##i; ++i)
#define REVFOR(i,n) for(int i=(n)-1; i>=0; --i)
#define FOR2(i,b,n) for(int i=b; i<(n); ++i)
#define REVFOR2(i,b,n) for(int i=(n)-1; i>=b; --i)
#define SC(i) scanf("%d", i)
#define ALL(C) (C).begin(), (C).end()
#define RALL(C) (C).rbegin(), (C).rend()
#define MIN(C) *min_element(ALL(C))
#define MAX(C) *max_element(ALL(C))
#define A first
#define B second

int char2int(int c) { return isdigit(c) ? c-'0' : c-'A'+10; }
char nextC(char c) { if (c == '9') return 'a'; else return c+1; }

int64 fromBase(const char *txt, int len, int base) {
	int64 res = 0;
	FOR(i,len) {
		if (char2int(txt[i]) >= base) return INT_MIN;
		res *= base;
		res += char2int(txt[i]);
	}
	return res;
}

int main(void) {
    int n; cin>>n;
    FOR(_i,n) {
        int64 res=0;

		string s;
		cin>>s;

		set<char> used;
		FOR(i,s.size()) {
			used.insert(s[i]);
		}

		int base = used.size() + 1;

		map<char,char> toDec;
		char first = s[0];
		toDec[first] = '1';
		s[0] = '1';
		char free = '2';
		bool used0 = false;
		FOR2(i, 1, s.size()) 
		{
			if (toDec.count(s[i]))
			{
				s[i] = toDec[s[i]];
			}
			else if (s[i] != first && !used0) 
			{
				toDec[s[i]] = '0';
				s[i] = '0';
				used0 = true;
			} 
			else 
			{
				toDec[s[i]] = free;
				s[i] = free;
				free = nextC(free);
			}
		}

		res = fromBase(s.c_str(), s.size(), char2int(free));

        printf("Case #%d: %lld\n", _i+1, res);
    }
    return 0;
}
