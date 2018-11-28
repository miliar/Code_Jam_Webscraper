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
#include <cstdio>
#include <cstdlib>
#include <ctime>
 
#define PI 3.1415926535897932384626433832795
#define sz(a) int((a).size()) 
#define pb push_back 
#define all(c) (c).begin(),(c).end() 
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++) 
#define rep(i,s,n) for(int i=s; i<n; i++)
#define repe(i,s,n) for(int i=s; i<=n; i++)
#define len(s) int((s).length()) 
#define pv(v) tr(v,i) cout << *i << " "; cout << endl
#define pr(i) cout << i << endl
#define valid(i,j,n,m) (i >= 0 && i < n && j >= 0 && j < m) 

using namespace std;

int main() {
	int le,d,t,c=0;
	cin >> le >> d >> t;
	vector<string> words(d);
	rep(i,0,d) cin >> words[i];
	
	while(t--) {
		c++;
		string pat;
		cin >> pat;
		vector<string> sub_pat(le,"");
		int j = 0;
		rep(i,0,le) {
			if(pat[j] == '(') {
				j++; 
				while(pat[j] != ')') { sub_pat[i] += pat[j]; j++; }
				j++;
			}
			else { sub_pat[i] += pat[j]; j++; }
			
			//cout << sub_pat[i] << " "; 
		}
		//cout << endl;
		int ans = 0;
		rep(i,0,d) {
			bool flag = true;
			rep(j,0,le) {
				if(find(all(sub_pat[j]),words[i][j]) == sub_pat[j].end())  { flag = false; break;}			
			}
			if(flag) ans++;
		}
		cout<<"Case #"<<c<<": "<<ans;
		if(t != 0) cout << endl; 
		
	}	
	return 0;
}
