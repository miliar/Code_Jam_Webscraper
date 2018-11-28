#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <cassert>
#include <ctime>
#include <map>
#include <set>
#define forn(i, n) for(int i = 0; i < int(n); i++)
#define X first
#define Y second
#define sz(s) (int)(s).size()
#define mp make_pair

using namespace std;

typedef long long li;
typedef pair<int, int> pt;
int t, p;
int m[100000];

int f[2000];
bool check(int lf, int rg){
	
	for(int i = lf; i <= rg; i++){
		
		if(m[i] < f[rg - lf]){
			return true;
			
		}
	}
	return false;
}
int solve(int lf, int rg){
	if(lf >= rg)
		return 0;
	int ans = 0;
	if(check(lf, rg)){
		return 1 + solve(lf, (lf + rg) >> 1) + solve(((lf + rg) >> 1) + 1, rg);
	}
	
	return 0;
}
int main(){
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	cin >> t;
	f[0] = 0;
	f[1] = 1;
	for(int j = 4; j < 2000; j *= 2)
		f[j - 1] = f[j / 2 - 1] + 1; 
		
	forn(q, t){
		
		memset(m, 0, sizeof(m));
		
		cin >> p;

		forn(i, (1 << p)){
			cin >> m[i];
		}
		forn(i, p){
			forn(j, (1 << (p - i - 1)) ){
				int k;
				cin >> k;
				if(k != 1){
					k = 1;
					throw 1;
				}
			}
		}
		int ans = solve(0, (1<< p) - 1); 
		cout << "Case #" << q + 1 << ": " << ans << endl;
	}
	return 0;
}