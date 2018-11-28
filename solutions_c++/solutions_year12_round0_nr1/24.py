#include <list>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <iomanip>
#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <cfloat>
#include <climits>
#include <numeric>
#include <ctime>

using namespace std;

const int oo = 0x3f3f3f3f;
const double eps = 1e-9;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pii;
typedef vector<ll> vll;
typedef vector<int> vi;
typedef vector<string> vs;

#define sz(c) int((c).size())
#define all(c) (c).begin(), (c).end()
#define FOR(i,a,b) for (int i = (a); i < (b); i++)
#define FORS(i,a,b,s) for (int i = (a); i < (b); i=i+(s))
#define FORD(i,a,b) for (int i = int(b)-1; i >= (a); i--)
#define FORIT(i,c) for (__typeof__((c).begin()) i = (c).begin(); i != (c).end(); i++)

char charmap[] = "yhesocvxduiglbkrztnwjpfmaq";

int main() {
	int tc;
	cin >> tc;
	string line;
	getline(cin,line);
	FOR(ctc,1,tc+1) {
		cout << "Case #" << ctc << ": ";
		getline(cin,line);
		FOR(i,0,sz(line))
			if(line[i]>='a' && line[i]<='z')
				line[i] = charmap[line[i]-'a'];
		cout << line << endl;
	}
	return 0;
}
