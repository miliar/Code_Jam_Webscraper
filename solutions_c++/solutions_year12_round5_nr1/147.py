#include <iostream>
#include <cstdio>
#include <set>
#include <stack>
#include <vector>
#include <map>
#include <string>
#include <cstring>
#include <cmath>
#include <memory.h>
#include <algorithm>
#include <cstdlib>
#include <cassert>
#include <sstream>
#include <fstream>
using namespace std;


#define pb push_back
#define mp make_pair

typedef long long li;
typedef vector<li> vi;
typedef pair<int, int> pi;
void solve();

int main() {
	freopen("input", "r", stdin);
	freopen("output", "w", stdout);
	ios_base::sync_with_stdio(false);
	int t;
	cin >> t;
	string s;
	getline(cin, s);
	cout << fixed;
	cout.precision(30);
	for (int i = 1; i <= t; ++i) {
		cout << "Case #" << i << ": ";
		solve();
		cout << '\n';
	}
	return 0;
}
struct x{
	int id,t,p;
	bool operator < (const x& b) const {
		return t *  b.p < b.t * p || (t *  b.p == b.t * p && id < b.id);
	}
};

x test[101010];
void  solve(){
	int n;
	cin>>n;
	for(int i=0;i<n;++i){
		cin>>test[i].t;
		test[i].id  = i;
	}
	for(int i=0;i<n;++i){
		cin>>test[i].p;
		test[i].id  = i;
	}
	
	sort(test, test + n);
	
	
	for(int i=0;i<n;++i){
		cout<<test[i].id<<' ';
	}
}
