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

int n;
string tab[50];
int v[50];

int grande(int x) {
	FOR(j,n) {
		if((tab[x][j] == '1') && (j > x))
			return 1;
	}
	return 0;
}

void pinta() {
	printf("TO COM\n");
	FOR(i,n) cout << tab[i] << endl;
}

int arruma(int x) {
	if(v[x] <= x) return 0;
	int p = -1;
	for(int i = x+1; i < n; i++) {
		if(v[i] <= x) {
			p = i;
			break;
		}
	}
	if(p==-1) return inf;
	int r = 0;
	for(int j = p; j > x; j--) {
		swap(v[j], v[j-1]);
		r++;
	}
	return r;
}

int calc() {
	int rr = 0;

	FOR(i,n) {
		rr += arruma(i);
	}

	return rr;
}

int main() {
	int T;
	scanf("%d\n", &T);
	FOR(t,T) {
		printf("Case #%d: " , t+1);
		scanf("%d", &n);
		FOR(i,n) cin >> tab[i];
		memset(v, 0 ,sizeof(v));
		FOR(i,n) FOR(j,n) if(tab[i][j] == '1') v[i] = j;
		int r = calc();
		printf("%d\n", r);
	}

    return 0;
}

