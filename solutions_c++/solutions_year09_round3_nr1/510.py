#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <queue>
#include <set>
#include <cmath>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
const int inf=(1<<30);
#define mset(a,x) memset(a,x,sizeof(a))
#define ABS(a) ((a) >= 0 ? (a) : -(a))
#define dbg(x) cerr<<#x<<" : "<<x<<endl
int T;
ll n;
string str;
set<char> Map;
map<char, int> val;
int base;
int main() 
{
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	scanf("%d", &T);
	int Case=0;
	while (T--) {
		   Map.clear();
		   val.clear();
		   base = 0;
	       cin >> str;
           for (int i = 0; i < str.size(); i++) {
		        if (Map.find(str[i]) == Map.end()) {
				    Map.insert(str[i]);
                    base++;
				}
		   }
		   base = max(base, 2);
		   int cnt=0;
		   for (int i = 0; i < str.size(); i++) {
		        if (val.find(str[i]) == val.end()) {
				    if (cnt==0) {
	                    val[str[i]] = 1;			    
				    }
					else if (cnt==1) {
					    val[str[i]] = 0;
					}
					else {
					    val[str[i]] = cnt;
					}
					cnt++;
				}
		   }
		   ll res = 0;
		   for (int i = 0; i < str.size(); i++) {
		        res = res*base+val[str[i]];
		   }
		   printf("Case #%d: ", ++Case);
		   cout << res << endl;
	}
    return 0;
}
