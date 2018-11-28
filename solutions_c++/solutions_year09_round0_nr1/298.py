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

string s[5001];
set<char> k[15];

int l,d,n;

int ok(int x) {
	FOR(i,l) {
		if(!k[i].count(s[x][i])) return 0;
	}
	return 1;
}

int main() {
	scanf("%d %d %d" , &l, &d, &n);
	FOR(i,d) {
		cin >> s[i];
	}
	string a;
	FOR(t,n) {
		printf("Case #%d: ", t+1);
		FOR(i,l) k[i].clear();
		cin >> a;
		int p = 0;
		FOR(i, sz(a)) {
			if(a[i] == '(') {
				i++;
				while(a[i] != ')') {
					k[p].insert(a[i]);
					i++;
				}
			}
			else {
				k[p].insert(a[i]);
			}
			p++;
		}

		int rr = 0;
		FOR(i,d) {
			if(ok(i)) rr++;
		}
		printf("%d\n", rr);
	}

    return 0;
}

