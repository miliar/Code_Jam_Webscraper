#include <map>
#include <set>
#include <math.h>
#include <deque>
#include <stack>
#include <queue>
#include <vector>
#include <iomanip>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <memory.h>
#include <stdio.h>

using namespace std;

#define pb push_back
#define all(v) v.begin(),v.end()
#define rep(i,s,m) for(int i=s;i<m;i++)
#define mem(a,b) memset(a,b,sizeof(a))
#define mp make_pair
#define PI = (2.0 * acos(0.0));
typedef stringstream ss;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<vector<int> > vii;
typedef long long ll;
#define OO ((int)1e9)
#define sz 10010

int di[] = { -1, 0, 1, 0 };
int dj[] = { 0, 1, 0, -1 };

int main() {
	freopen("in.txt","rt",stdin);
	freopen("out.txt","wt",stdout);
	map<char, char> m;
	m['a'] = 'y';
	m['b'] = 'h';
	m['c'] = 'e';
	m['d'] = 's';
	m['e'] = 'o';
	m['f'] = 'c';
	m['g'] = 'v';
	m['h'] = 'x';
	m['i'] = 'd';
	m['j'] = 'u';
	m['k'] = 'i';
	m['l'] = 'g';
	m['m'] = 'l';
	m['n'] = 'b';
	m['o'] = 'k';
	m['p'] = 'r';
	m['q'] = 'z';
	m['r'] = 't';
	m['s'] = 'n';
	m['t'] = 'w';
	m['u'] = 'j';
	m['v'] = 'p';
	m['w'] = 'f';
	m['x'] = 'm';
	m['y'] = 'a';
	m['z'] = 'q';
	m[' '] = ' ';
	int T;
	string s;
	cin>>T;
	getline(cin,s);
	for(int i = 1 ; i <= T ; i++){
		getline(cin,s);
		cout<<"Case #"<<i<<": ";
		for(int j = 0 ; j < s.size() ; j++)
			cout<<m[s[j]];
		cout<<endl;
	}
	return 0;
}
