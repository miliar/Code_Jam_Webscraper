#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <cctype>
#include <stack>
#include <queue>
#include <list>
#include <vector>
#include <map>
#include <sstream>
#include <cmath>
#include <bitset>
#include <utility>
#include <set>
#include <numeric>
#include <ctime>
#include <climits>
#include <cstdlib>
 
const double Pi=acos(-1.0);
typedef long long LL;
 
#define Set(a, s) memset(a, s, sizeof (a))
#define Rd(r) freopen(r, "r", stdin)
#define Wt(w) freopen(w, "w", stdout)
 
using namespace std;
 
string s = "yhesocvxduiglbkrztnwjpfmaq";

string getline() {
	string t;
	getline(cin, t);
	return t;
}

int main (int argc, char ** argv)
{
	int linen;
	stringstream(getline()) >> linen;
	for (int i = 1; i <= linen; i++) {
		cout << "Case #" << i << ": ";
		string t = getline();
		for (int j = 0; j < (int)t.size(); j++) {
			if (!isspace(t[j])) {
				cout << s[t[j] - 'a'];
			} else {
				cout << t[j];
			}
		}
		cout << '\n';
	}
	return 0;
}






