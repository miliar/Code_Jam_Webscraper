#include <iostream>
#include <vector>
#include <string>
#include <cstring>
#include <algorithm>
#include <map>
#include <sstream>
#include <fstream>
#include <queue>

using namespace std;

#define forn(i, n) for(int i = 0; i<(int)(n); i++)
#define forsn(i, m, n) for(int i = (int)(m); i<(int)(n); i++)
#define si(x) x.size()
#define mp make_pair
#define pb push_back
#define all(x) x.begin(),x.end()

typedef vector<int> vi;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef pair<int, ii> iii;
typedef vector<vi> vvi;

typedef long long int tint;

int t, n;

int main(){
	cin >> t;
	forn(tt, t){
		
		cout << "Case #" << tt + 1 << ": ";
		
		int res = 0, tx = 0, mv = 10000000;
		cin >> n;
		forn(i, n){ int ea; cin >> ea; tx ^= ea; res += ea; mv = min(mv, ea); }
		if(tx != 0) { cout << "NO" << endl; continue; }
		res -= mv;
		cout << res << endl;
	}	

	return 0;	
}
