#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>

#define forn(X,Y) for (int X = 0;X < Y;X++)
#define debug(x) cout << '>' << #x << ':' << x << '\n';

#define rep(X,Y,Z) for (int X = Y;X < Z;X++)
#define reset(Z,Y) memset(Z,Y,sizeof(Z))

#define sz(Z) ((int)Z.size())
#define all(W) W.begin(), W.end()
#define pb push_back

#define mp make_pair
#define A first
#define B second

#define inf 1023123123
#define eps 1e-11

#define MX(Z,Y) Z = max((Z),(Y))
#define MN(X,Y) X = min((X),(Y))

#define forit(X,Y) for(typeof((Y).begin()) X = (Y).begin();X!=(Y).end();X++)

using namespace std;

typedef long long ll;
typedef double db;
typedef vector<int> vint;

//clockwise
vector<string> rotate90degrees(vector<string> abc) {
	vector<string> def = vector<string>(sz(abc[0]),string(sz(abc),'.'));
	forn(i,sz(abc)) {
		forn(j,sz(abc[0])) {
			def[sz(abc[0]) - 1 - j][i] = abc[i][j];
			}
		}
	return def;
	}	
	
vector<string> enframe(vector<string> abc, char impassable) {
	string huhu(sz(abc[0]) + 2,impassable);
	forn(i,sz(abc)) abc[i] = impassable + abc[i] + impassable;
	abc.insert(abc.begin(),huhu);
	abc.push_back(huhu);
	return abc;
	}

int main() {
	
	int nc;
	scanf("%d",&nc);
	forn(z,nc) {
		printf("Case #%d: ",z+1);
		int n,jejer;
		scanf("%d%d\n",&n,&jejer);
		vector<string> st(n,string(n,'.'));
		forn(i,n) {
			forn(j,n) {
				char x;
				scanf("%c",&x);
				st[i][j] = x;
				}
			scanf("\n");
			}
		
		st=rotate90degrees(st);
		st=rotate90degrees(st);
		st=rotate90degrees(st);
		//forn(i,sz(st)) debug(st[i]);
		forn(j,n) {
			for (int i = n-1;i >= 0;i--) {
				char ok = '.';
				if (st[i][j] != '.') continue;
				for (int k = i-1;k >= 0;k--) if (st[k][j] != '.') {
					ok=st[k][j];
					st[k][j] = '.';
					break;
					}
				st[i][j] = ok;
				}
			}
		forn(i,jejer) st=enframe(st,'.');
		//forn(i,sz(st)) debug(st[i]);
		int vic[2]={0,0};
		string batu = "RB";
		int dx[] = {1,1,1,0,0,-1,-1,-1};
		int dy[] = {1,0,-1,1,-1,1,0,-1};
		forn(i,n) forn(j,n) forn(k,2) forn(m,8) {
			int valid = 1;
			int x=i+jejer,y=j+jejer;
			forn(l,jejer) {
				if (st[x][y] != batu[k]) valid = 0;
				x += dx[m];
				y += dy[m];
				}
			if (valid) vic[k] = 1;
			}
		if (vic[0] && vic[1]) printf("Both\n");
		if (vic[0] && !vic[1]) printf("Red\n");
		if (vic[1] && !vic[0]) printf("Blue\n");
		if (!vic[1] && !vic[0]) printf("Neither\n");
		}
				
		
	
	return 0;
	}


//Powered by [KawigiEdit] 2.0!









