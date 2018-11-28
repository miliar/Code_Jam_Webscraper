#include <iterator>
#include <cstring>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <bitset>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <fstream>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <numeric>
#include <vector>
#include <set>
#include <complex>
#include <list>
#include <valarray>
#ifdef _MSC_VER
#include <hash_set>
#include <hash_map>
using namespace stdext;
#else
#include <ext/hash_set>
#include <ext/hash_map>
using namespace __gnu_cxx;
#endif
using namespace std;

#define SZ(v)                   (int)v.size()
#define FOR(i,a,b)				for(int i=(a);i<(b);++i)
#define rev(i,a,b)				for(int i=(b);i>=(a);--i)
#define sz(v)                   (int)v.size()
#define all(v)					v.begin(), v.end()
#define rall(v)					v.rbegin(), v.rend()
#define pb						push_back
#define mp						make_pair
typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pi;
typedef vector<pi> vpi;
const int OO = 1 << 28;

int di[] = { -1, 0, 1, 0 };
int dj[] = { 0, 1, 0, -1 };
#define Nd 0
#define Ed 1
#define Sd 2
#define Wd 3


bool won(string s, char c){
	FOR(i,0,4){
		if(s[i] != c && s[i] != 'T')
			return 0;
	}
	return 1;
}

int main() {
#ifndef ONLINE_JUDGE
	freopen("in.in", "rt", stdin);
	freopen("out.out", "wt", stdout);
#endif
	int t;
	cin >> t;
	string r[4],c[4];
	string s;
	bool hasDots = 0;
	FOR(cs,1,t+1){
		hasDots = 0;
		printf("Case #%d: ",cs);
		FOR(i,0,4){
			cin >> r[i];
		}
		FOR(i,0,4){
			if(won(r[i],'X')){
				printf("X won\n");
				goto next;
			} else if (won(r[i],'O')){
				printf("O won\n");
				goto next;
			}
		}
		hasDots=0;
		FOR(j,0,4){
			c[j].resize(4);
			FOR(i,0,4){
				c[j][i] = r[i][j];
				hasDots |= (r[i][j] == '.');
			}
			if(won(c[j],'X')){
				printf("X won\n");
				goto next;
			} else if (won(c[j],'O')){
				printf("O won\n");
				goto next;
			}
		}
		s = "";
		FOR(i,0,4)
			s+=r[i][i];
		if(won(s,'X')){
			printf("X won\n");
			goto next;
		} else if (won(s,'O')){
			printf("O won\n");
			goto next;
		}

		s ="";
		rev(i,0,3)
			s+= r[3-i][i];

		if(won(s,'X')){
			printf("X won\n");
			goto next;
		} else if (won(s,'O')){
			printf("O won\n");
			goto next;
		}
		if(hasDots)
			printf("Game has not completed\n");
		else
			printf("Draw\n");
		next:;
	}
	return 0;
}




