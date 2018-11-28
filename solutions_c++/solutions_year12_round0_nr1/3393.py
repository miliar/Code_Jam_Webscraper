#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>
#include <fstream>
#include <list>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <cmath>
#include <sstream>
#include <deque>
#include <utility>
#include <bitset>

using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define REV(i,a,b) for(int i=(a);i>=(b);i--)
#define mp make_pair
#define pb push_back
#define oo 2e9
#define MAX 10001
#define sz(v) (int)v.size()
#define all(c) (c).begin(),(c).end()
#define rall(c) (c).rbegin(),(c).rend()
#define iter(it,s) for(it=s.begin();it!=s.end();it++)
#define show(x) cerr<<#x<<" = "<<x<<endl;
#define mem(s,v) memset(s,v,sizeof(s))

typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pi;
typedef vector<pi> vpi;

int vis[MAX];
int memo[MAX];
int dx[] = { -1, 0 };
int dy[] = { 0, 1 };

int main() {
#ifndef ONLINE_JUDGE
	freopen("A.in", "rt", stdin);
	freopen("A.o", "wt", stdout);
#endif
	int t;
	cin >> t;
	string s;
	map<char, char> m;
	m[' '] = ' ';
	char b[26] = { 'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g',
			'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a',
			'q' };
	FOR (i , 'a' , 'z'+1){
		m[i] = b[i-'a'];
	}
	getline(cin, s);
	FOR (i , 0 , t) {
		getline(cin, s);
		FOR (j ,0 , sz(s))
			s[j] = m[s[j]];
		printf ("Case #%d: ", i+1);
		cout << s << endl;
	}
	return 0;
}
