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

map<ii, bool> dp;

bool _dp(int a, int b){
	if(a==b) return false;
	if(a<b) swap(a, b);

	if(a%b == 0) return true;
	if(a>(b*2)) return true;
	else return (_dp(a-b, b)^1);
}

int main(){
	freopen("C-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);

	int NC; cin >> NC;
	forn(nc, NC){
		int a1, a2, b1, b2;
		cin >> a1 >> a2 >> b1 >> b2;
		int res = 0;
		forsn(i, a1, a2+1){
			forsn(j, b1, b2+1){
				if(_dp(i, j)) res++;
			}
		}
		cout << "Case #" << nc+1 << ": " << res << endl;
	}
	return 0;
}
