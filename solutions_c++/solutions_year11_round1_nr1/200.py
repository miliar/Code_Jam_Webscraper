#include<cstdio>
#include<algorithm>
#include<vector>
#include<cstring>
#include<sstream>
#include<string>
#include<iostream>
#include<set>
#include<map>
#include<queue>
#include<stack>
#include<numeric>
#include<climits>
using namespace std;
typedef long long ll;
#define pb push_back
#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()

double eps = 1e-9;
int cmp(double a, double b = 0){
	return a + eps < b ? -1 : a - eps > b ? 1 : 0;
}

int main(){
	int tt; cin >> tt;
	for(int caso = 1; caso <= tt; caso++){

		ll n, pd, pg;
		cin >> n >> pd >> pg;
		ll mini = -1;
		for(ll i = 1; i <= 100; i++) if(pd * i % 100 == 0){
			mini = i;
			break;
		}
		bool can = false;
		
		if(mini == -1 || mini > n) can = false;
		else if(pg == 100 && pd != 100) can = false;
		else if(pg == 0 && pd != 0) can = false;
		else can = true;

		cout << "Case #" << caso << ":";
		if(can) cout << " Possible" << endl;
		else cout << " Broken" << endl;
	}
}
