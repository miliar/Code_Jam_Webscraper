#define _CRT_SECURE_NO_DEPRECATE
#include<cstdio>
#include<vector>
#include<queue>
#include<string>
#include<sstream>
#include<iostream>
using namespace std;

#define FOR(i,s,n) for(int i = (s); i < (n); ++i)
#define REP(i,n) FOR(i,0,n)
#define sz(x) int((x).size())
#define pb push_back
#define mp make_pair
#define X first
#define Y second
#define all(x) (x).begin(),(x).end()

typedef vector<int> VI;
typedef pair<int, int> PII;
typedef stringstream SS;

int main() {
	freopen("b-large.in","r",stdin);
	freopen("b-large.out","w",stdout);

	int tc;
	cin >> tc;
	string s;
	FOR(ttt,1,tc+1) {
		cin >> s;
		if(next_permutation(all(s))) cout << "Case #" << ttt << ": " << s << endl;
		else {
			sort(all(s));
			s = "0"+s;
			REP(i,sz(s)) if(s[i] != '0') {
				s[0] = s[i];
				s[i] = '0';
				break;
			}
			cout << "Case #" << ttt << ": " << s << endl;
		}
	}
	return 0;
}