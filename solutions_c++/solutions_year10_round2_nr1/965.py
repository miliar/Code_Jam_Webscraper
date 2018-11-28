#include<iostream>
#include<vector>
#include<map>
#include<sstream>
#include<math.h>
#include<set>
#include<fstream>
#include<algorithm>
#include<cstring>
#include<cassert> 
#include <list>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <iomanip>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <queue>

using namespace std;



#define debug(x) cout << #x << " = " << x << "\n";
#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()
#define sz size()
#define pb push_back
#define mp make_pair
#define fr(i, n) for(i=0;i<n;i++)
#define fr2(i, a, n) for(i=a;i<n;i++)
#define mem(a, n) memset(a, n, sizeof(a))
typedef vector<int> VI;
typedef long long LL;
typedef vector<string> VS;
typedef stringstream SS; 
const int INF = (int) 1e9;
#define LLMax LLONG_MAX

#define cs c_str()
#define frIt(it, s) for(typeof(s.begin()) it=s.begin();it!=s.end();it++)
typedef vector<double> VD;
#include <ext/hash_map> // include this header file

using namespace __gnu_cxx; // we have to include this
 
struct stringHash {
        size_t operator () (const string &s) const {
                        hash<const char *> h;
                                        return h(s.c_str());
        }
};

int main() {
	int t;
	cin >> t;
	int k;
	fr2(k, 1, t+1) {
		int n, r;
		cin >> n >> r;
		int i, j;
		hash_map<string, char, stringHash> m;
		m["/"] = 1;
		fr(i, n) {
			string s;
			cin >> s;
			s += "/";
			int l = s.sz;
			
			j = 0;
			string tmp = "";
			while(j<l) {
				tmp += s[j];
				if(s[j]=='/')
					m[tmp] = 1;
				j++;
			}
		}
		LL cnt = 0;
		fr(i, r) {
			string s;
			cin >> s;
			s += "/";
			int l = s.sz;
			j = 0;
			string tmp;
			while(j<l) {
				tmp += s[j];
				if(s[j]=='/') {
					if(m[tmp]);
					else {
						cnt++;
						m[tmp] = 1;
					}
				}
				j++;
			}
		}
		printf("Case #%d: %lld\n", k, cnt);
			
	}
}


