#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <stack>
#include <list>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <queue>

using namespace std;

#define forn(i,n) for(int i=0;i<(int)(n);i++)
#define si(c) ((int)(c).size())
#define forsn(i,s,n) for(int i = (int)(s); i<((int)n); i++)
#define all(c) (c).begin(), (c).end()
#define pb push_back
#define mp make_pair

typedef long long int tint;
typedef vector<int> vi;
typedef vector<bool> vb;
typedef vector<string> vs;
typedef pair<int,int> ii;
typedef vector<ii> vii;

int main(){
	freopen("A-large.in","r",stdin);
	freopen("out.txt", "w", stdout);

	int NC; cin >> NC;
	forn(nc, NC){
		tint n, k;
		cin >> n >> k;
		tint pow = 1; forn(i, n) pow<<=1;
		k %= pow;
//		cout << k << " " << pow << " " << n << endl;
		cout << "Case #" << nc+1 << ": ";
		if(k+1 == pow) cout << "ON" << endl;
		else cout << "OFF" << endl;
	}

	return 0;
}
