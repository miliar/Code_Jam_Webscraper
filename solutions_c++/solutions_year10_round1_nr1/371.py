#include <iostream>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
#include <vector>
#include <string>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <sstream>
using namespace std;

#define sz(A) (int)(A).size()
#define vs vector<string>
#define vi vector<int>
#define ll long long
#define FOR(A,B) for(int A=0; A < (int) (B);A++)
#define pb push_back
#define pii pair<int,int>
#define inf (1<<25)
#define infL 10000000000000000LL
#define F first
#define S second
#define all(x) x.begin() , x.end()

int n,k;

string tab[100];

void jogaPraDireita(int x, int y) {
	for(int j = y+1; j < n; j++) {
		if(tab[x][j] != '.') break;
		swap( tab[x][j], tab[x][j-1] );
	}
}

void roda() {
	FOR(i,n) {
		for(int j = n-1; j >= 0; j--) {
			if(tab[i][j] != '.')
				jogaPraDireita(i,j);
		}
	}
}

int contaLinha(int x, char c) {
	int ja = 0, r = 0;
	FOR(j,n) {
		if(tab[x][j] == c) ja++;
		else ja = 0;
		r = max(r, ja);
	}
	return r;
}

int contaColuna(int y, char c) {
	int ja = 0, r = 0;
	FOR(j,n) {
		if(tab[j][y] == c) ja++;
		else ja = 0;
		r = max(r, ja);
	}
	return r;
}

int contaDiag1(int x, int y, char c) {
	int ja = 0, r = 0;
	while(x < n && y < n) {
		if(tab[x][y] == c) ja++;
		else ja = 0;
		r = max(r, ja);
		x++; y++;
	}
	return r;
}

int contaDiag2(int x, int y, char c) {
	int ja = 0, r = 0;
	while(x < n && y >= 0) {
		if(tab[x][y] == c) ja++;
		else ja = 0;
		r = max(r, ja);
		x++; y--;
	}
	return r;
}



int conta(char c) {
	int r = 0;
	FOR(i,n) {
		r = max(r, contaLinha(i, c));
		r = max(r, contaColuna(i, c));
	}
	FOR(i,n) FOR(j,n) {
		r = max(r, contaDiag1(i,j,c));
		r = max(r, contaDiag2(i,j,c));
	}
	return r;
}

int main() {
	int T;
	scanf("%d", &T);
	FOR(t,T) {
		printf("Case #%d: " , t+1);
		cin >> n >> k;
		FOR(i, n) {
			cin >> tab[i];
		}
		roda();
		int r = conta('R');
		int b = conta('B');
		if(r >= k && b >= k) cout << "Both" << endl;
		else if(r >= k) cout << "Red" << endl;
		else if(b >= k) cout << "Blue" << endl;
		else cout << "Neither" << endl;
	}

    return 0;
}

