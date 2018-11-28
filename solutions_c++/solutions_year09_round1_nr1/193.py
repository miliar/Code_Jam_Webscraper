#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
using namespace std;

#define REP(i,n) for(int i=0;i<(n);++i)
#define FOR(i,a,b) for(int i=(a);i<=(b);++i)
#define RFOR(i,a,b) for(int i=(a);i>=(b);--i)
#define FOREACH(it,c) for(typeof((c).begin())it=(c).begin();it!=(c).end();++it)
#define CLR(x) memset((x),0,sizeof((x)))
typedef long long LL;
typedef vector<int> VI;
typedef vector<string> VS;

vector<string> split( const string& s, const string& delim =" " ) {
    vector<string> res;
    string t;
    for ( int i = 0 ; i != s.size() ; i++ ) {
        if ( delim.find( s[i] ) != string::npos ) {
            if ( !t.empty() ) {
                res.push_back( t );
                t = "";
            }
        } else {
            t += s[i];
        }
    }
    if ( !t.empty() ) {
        res.push_back(t);
    }
    return res;
}

vector<int> splitInt( const string& s, const string& delim =" " ) {
    vector<string> tok = split( s, delim );
    vector<int> res;
    for ( int i = 0 ; i != tok.size(); i++ )
        res.push_back( atoi( tok[i].c_str() ) );
    return res;
}

int s2i(string s) {
    stringstream ss;
    ss << s;
    int res;
    ss >> res;
    return res;
}

string i2s(int n) {
    stringstream ss;
    ss << n;
    string res;
    ss >> res;
    return res;
}

string str;

bool ishappy(int n, int base) {
	map<int, bool> mp;
	map<int, bool>::iterator itr;

	while (true) {
		string s = i2s(n);

		int sum = 0;
		while (n) {
			int t = n % base;
			sum += t * t;
			n /= base;
		}

		if (sum == 1) return true;

		itr = mp.find(sum);
		if (itr == mp.end()) mp[sum] = true;
		else return false;

		n = sum;
	}
}

void run() {
	getline(cin, str);
	vector<int> mm = splitInt(str);

	int n = 2;
	while (true) {
		bool flag = true;

		REP(i,mm.size()) {
			if (!ishappy(n, mm[i])) {
				flag = false;
				break;
			}
		}

		if (flag) {
			cout << n << endl;
			return;
		}

		++n;
	}
}

int main() {
	int T;
	cin >> T;
	getline(cin, str);
	FOR(k,1,T) {
		cout << "Case #" << k << ": ";
		run();
	}
	return 0;
}
