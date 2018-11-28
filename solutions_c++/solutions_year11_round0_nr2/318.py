// AlexFetisov
// Accepted

#define _CRT_SECURE_NO_DEPRECATE
#pragma comment (linker, "/STACK:32000000")

#include <iostream>
#include <stdio.h>
#include <cstring>

void initf() 
{ 
	freopen("b.in", "r", stdin); 
	freopen("b.out", "w", stdout);
}

#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <queue>

using namespace std;

#define fr(i,a,b) for ( int i = ( a ); i <= ( b ); ++i )
#define fi( a ) for ( int i = 0; i < ( a ); ++i )
#define fj( a ) for ( int j = 0; j < ( a ); ++j )
#define fk( a ) for ( int k = 0; k < ( a ); ++k )
#define CLR( a, b ) memset( ( a ), ( b ), sizeof ( a ) )
#define clr( a ) CLR( ( a ), 0 )
#define pb push_back
#define mp make_pair
#define all( v ) ( v ).begin(), ( v ).end()

typedef unsigned int uint;
typedef unsigned long long ull;
typedef long long ll;
typedef vector < int > vi;
typedef pair < int, int > pii;

int gs, bs, n;
string tmp;
string s;
int g[26][26];
int g1[26][26];
string list;

void process() {
	if (list.size() <= 1) {
		return;
	}

	int L = list.length();
	char c = list[L-1], c1 = list[L-2];
	if (g[c-'A'][c1-'A'] != -2) {
		reverse(all(list));
		fi(2) {
			list.erase(list.begin());
		}                  
		reverse(all(list));
		list.pb((char)(g[c-'A'][c1-'A'] + 'A'));
		process();
		return;
   	}

	fi(list.size()) {
		fj(i) {
			if (g1[list[i]-'A'][list[j]-'A'] != -2) {
				list.clear();
				return;
			}
		}	
	}
}

void solve(int test_id) {
	printf("Case #%d: ", test_id);
	cin >> gs;
	clr(g);
	list.clear();
	fi(26) {
		fj(26) {
			g[i][j] = -2;
			g1[i][j] = -2;
		}
	}
	for (int i = 0; i < gs; ++i) {
		cin >> tmp;
		g[tmp[0]-'A'][tmp[1]-'A'] = g[tmp[1]-'A'][tmp[0]-'A'] = tmp[2] - 'A';
	}	
	cin >> bs;
	for (int i = 0; i < bs; ++i) {
		cin >> tmp;
		g1[tmp[0]-'A'][tmp[1]-'A'] = g1[tmp[1]-'A'][tmp[0]-'A'] = -1;			
	}
	cin >> n;
	cin >> s;
	for (int i = 0; i < n; ++i) {
		list.pb(s[i]);
		process();		
	}
	cout << "[";
	if (list.empty()) {
		cout << "]\n";
	} else if (list.size() == 1) {
		cout << list[0] << "]\n";
	} else {
		cout << list[0];
		fi(list.size()) if (i) {
			cout << ", " << list[i];			
		}
		cout << "]\n";
	}
}

int main() {
	initf();
	int T, i;
	scanf("%d", &T);
	for (i = 1; i <= T; ++i) { 
		solve(i);
	}
	return 0;
}
