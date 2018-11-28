#include <iostream>
#include <vector>
#include <cmath>
#include <string>
#include <fstream>
using namespace std;
#define FOR(i,n) for(i=0;i<n;i++)
#define VI vector<int>
#define FORR(i,a,b) for(i=a;i<b;i++)
#define pb(a) push_back(a)

int dx[] = {-1,0,0,1};
int dy[] = {0,-1,1,0};
int a[110][110], d[110][110];
int i,j,k,l,n,m,p,r,t;

char c;
	vector<string> s;
char solve(int x, int y) {
	if (s[x][2*y-2] == ' ') {
	r = -1;
	FOR(k, 4) if (r==-1 || a[x+dx[k]][y+dy[k]] < a[x+dx[r]][y+dy[r]]) r = k; 
	if (a[x+dx[r]][y+dy[r]] >= a[x][y]) s[x][2*y-2] = c++; else
	s[x][2*y-2] = solve(x+dx[r], y+dy[r]);
	}
	return s[x][2*y-2];
}

int main() {
	ifstream cin("B.in.txt");
	ofstream cout("B.out.txt");
	
	cin >> t;
	

	FOR(i, 110) a[0][i] = a[i][0] = 1000000;
	FORR(p,1,t+1) {
		cin >> n >> m;
		c = 'a';
		FOR(i, 110) a[n+1][i] = a[i][m+1] = 1000000;
		s.clear();
		s.pb("");
		FOR(i, n) {s.pb(""); FOR(j, m) {
			cin >> a[i+1][j+1];
			if (j==m-1) s[i+1]+= " "; else
				s[i+1] += "  ";
		} }
		
		FORR(i,1,n+1) FORR(j,1,m+1) solve(i,j);
		cout << "Case #" << p << ":"<<endl;
		FORR(i,1,n+1) cout << s[i] << endl;
	}

	return 0;
}