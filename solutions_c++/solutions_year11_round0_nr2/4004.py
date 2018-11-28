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

void start() {
    int t; cin>>t;
    FOR(_i,t) {
		map<pair<char,char>, char> combine;
		set<pair<char,char> > opposed;

		int c;
		cin>>c;
		FOR(j,c) {
			string s; cin>>s;
			combine[make_pair(s[0],s[1])] = s[2];
			combine[make_pair(s[1],s[0])] = s[2];
		}
		int d;
		cin>>d;
		FOR(j,d) {
			string s; cin>>s;
			opposed.insert(make_pair(s[0],s[1]));
			opposed.insert(make_pair(s[1],s[0]));
		}

		int n; cin>>n;
		string s; cin>>s;

		string conv="";
		FOR(j,s.size()) {
			conv += s[j];

			int len = conv.size();
			if (len >= 2) {

				if (combine.count(make_pair(conv[len-1], conv[len-2])) != 0) {
					char c = combine[make_pair(conv[len-1], conv[len-2])];
					conv = conv.substr(0, len-2) + c;
				} else {
					FOR(i,conv.size()-1) {
						if (opposed.count(make_pair(conv[i], s[j])) != 0) {
							conv.clear();
							break;
						}
					}
				}
			}
		}

		string res = "[";
		FOR(j, conv.size()) {
			if (j!=0) res+=", ";
			res += conv[j];
		}
		res += "]";
		printf("Case #%d: %s\n", _i+1, res.c_str());
    }
}

int main(void) {
	start();

	return 0;
}
