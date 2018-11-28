#include <cassert>
#include <list>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <cfloat>
#include <numeric>

using namespace std;

const int oo = 0x3f3f3f3f;
const double eps = 1e-9;

typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pii;

#define sz(c) int((c).size())
#define all(c) (c).begin(), (c).end()
#define FOR(i,a,b) for (int i = (a); i < (b); i++)
#define FORD(i,a,b) for (int i = int(b)-1; i >= (a); i--)
#define FORIT(i,c) for (__typeof__((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define mp make_pair
#define pb push_back

int main() {
	
	int T;
	cin >> T;
	cin.get();
	FOR (t, 1, T+1) {
		string s;
		getline(cin,s);
		FOR(i, 0, s.size()) {
			switch(s[i]) {
				case 'a': s[i] = 'y'; break;
				case 'b': s[i] = 'h'; break;
				case 'c': s[i] = 'e'; break;
				case 'd': s[i] = 's'; break;
				case 'e': s[i] = 'o'; break;
				case 'f': s[i] = 'c'; break;
				case 'g': s[i] = 'v'; break;
				case 'h': s[i] = 'x'; break;
				case 'i': s[i] = 'd'; break;
				case 'j': s[i] = 'u'; break;
				case 'k': s[i] = 'i'; break;
				case 'l': s[i] = 'g'; break;
				case 'm': s[i] = 'l'; break;
				case 'n': s[i] = 'b'; break;
				case 'o': s[i] = 'k'; break;
				case 'p': s[i] = 'r'; break;
				case 'q': s[i] = 'z'; break;
				case 'r': s[i] = 't'; break;
				case 's': s[i] = 'n'; break;
				case 't': s[i] = 'w'; break;
				case 'u': s[i] = 'j'; break;
				case 'v': s[i] = 'p'; break;
				case 'w': s[i] = 'f'; break;
				case 'x': s[i] = 'm'; break;
				case 'y': s[i] = 'a'; break;
				case 'z': s[i] = 'q'; break;
				default: continue;
			}
		}
		cout << "Case #" << t << ": " << s << endl;
	}

	return 0;
}
