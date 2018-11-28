#include<cstdio>
#include<iostream>
#include<cstring>
#include<string>
#include<sstream>
#include<map>
#include<queue>
#include<vector>

using namespace std;

#define re return
#define sf scanf
#define pf printf
#define pb push_back

#define DBG 0

int inf = 1000000000;

string G[40];
int R, C;

string bin(char c) {
	int a;
	if( c <= '9' ) a = c - '0';
	else a = c - 'A' + 10;
	int i;
	string s = "";
	for(i=3;i>=0;i--) {
		if( a & (1<<i) ) s += '1';
		else s += '0';
	}
	return s;
}

void populate(int r, string s) {
	int i;
	G[r] = "";
	for(i=0;i<s.size();i++) {
		string add = bin(s[i]);
		G[r] += add;
	}
}

int find_size(int r, int c, char ch) {
	int i, j, a;
	for(i=r+1, j=c+1; i < R && j < C; i++, j++) {
		char cc = ch;
		for(a=i;a>=r;a--) {
		 if(G[a][j] != cc ) break;
		 if( cc == '1' ) cc = '0';
		 else if( cc == '0' ) cc = '1';
	 	}
	 	if( a >= r ) break;
	 	cc = ch;
	 	for(a=j;a>=c;a--) {
			if( G[i][a] != cc) break;
			if( cc == '1' ) cc = '0';
			else if( cc == '0' ) cc = '1';
		}
		if( a >= c ) break;
	}
	return i - r;
}

int fun() {
	int i, j;
	int maxi, ii, jj;
	maxi = 0;
	for(i=0;i<R;i++) {
		for(j=0;j<C;j++) {
			if( G[i][j] != '2' ) {
				int s = find_size(i, j, G[i][j]);
				if( s > maxi ) {
				  maxi = s;
				  ii = i; jj = j;
				}
			}
		}
	}

	for(i=ii;i<ii+maxi;i++)
	 for(j=jj;j<jj+maxi;j++)
	   G[i][j] = '2';
	return maxi;
}

int main() {
	int t, cases = 1;
	int i;
	sf("%d", &t);
	while(t--) {
		cin >> R >> C;
		for(i=0;i<R;i++) {
			string s;
			cin >> s;
			populate(i, s);
//if( DBG ) cout << "ok" << endl;
		}
if( DBG ) { for(i=0;i<R;i++) cout << G[i] << endl; }
		int A[600] = {0};
		while(1) {
			int s = fun();
if( DBG )	cout << s << endl;
			if( s == 0 ) break;
			A[s]++;
		}
		int total = 0;
		for(i=0;i<=512;i++)
		 if( A[i] ) total++;
		pf("Case #%d: %d\n", cases++, total);
		for(i=512;i>=0;i--) {
			if( A[i] ) pf("%d %d\n", i, A[i]);
		}
	}

	return 0;
}
