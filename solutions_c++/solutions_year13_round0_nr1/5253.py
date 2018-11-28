#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>
#include <fstream>
#include <list>
#include <set>
#include <climits>
#include <map>
#include <stack>
#include <queue>
#include <complex>
#include <cmath>
#include <sstream>
#include <deque>
#include <utility>
#include <bitset>

using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define REV(i,b,a) for(int i=(a);i>=(b);i--)
#define mp make_pair
#define pb push_back
#define oo 1e9
#define MAX 2001
#define sz(v) (int)v.size()
#define all(c) (c).begin(),(c).end()
#define rall(c) (c).rbegin(),(c).rend()
#define iter(it,s) for(it=s.begin();it!=s.end();it++)
#define show(x) cerr<<#x<<" = "<<x<<endl;
#define mem(s,v) memset(s,v,sizeof(s))

vector<string> v;
bool draw() {
	FOR(i , 0 , 4)
		FOR(j , 0 , 4)
			if (v[i][j] == '.')
				return false;
	return true;
}

bool won(char c) {
	bool wn = false;
	FOR(i , 0 , 4) {
		bool b1 = true, b2 = true;
		FOR(j , 0 , 4) {
			if (v[i][j] != c && v[i][j] != 'T')
				b1 = false ;
			if (v[j][i] != c && v[j][i] != 'T')
				b2 = false;
		}
		if(b1 || b2)
			wn = true;
	}
	bool b1 = true , b2 = true;
	FOR(i , 0 , 4) {
		if(v[i][i]!= c && v[i][i]!='T')
			b1 = false;
		if(v[i][3-i]!= c && v[i][3-i]!='T')
			b2 = false;
	}
	if(b1 || b2)
		wn = true;
	return wn;
}

int main() {
#ifndef ONLINE_JUDGE
	freopen("A-small-attempt0.in", "rt", stdin);
		freopen("o.txt", "wt", stdout);
#endif
	int t , cs = 1;
	cin >> t;
	while (t--) {
		v.clear(), v.resize(4);
		FOR(i , 0 ,4)
			cin >> v[i];
		if(won('X'))
			printf("Case #%d: X won\n" , cs++);
		else if (won('O'))
			printf("Case #%d: O won\n" , cs++);
		else if(draw())
			printf("Case #%d: Draw\n" , cs++);
		else
			printf("Case #%d: Game has not completed\n" , cs++);

	}
	return 0;
}
