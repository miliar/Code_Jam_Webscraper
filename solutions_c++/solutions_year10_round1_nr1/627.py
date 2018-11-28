#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <ctype.h>
#include <string.h>
#include <string>
#include <sstream>
#include <iostream>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <algorithm>
#include <functional> 
#include <numeric>
using namespace std;
#define foreach(i,v) for(__typeof((v).end()) i=(v).begin();i!=(v).end();++i)
#define rforeach(i,v) for(__typeof((v).rend()) i=(v).rbegin();i!=(v).rend();++i)
#define FOR(i,b,e) for(int i=(b);i<(e);++i)
#define FORE(i,b,e) for(int i=(b);i<=(e);++i)
typedef long long LL;

int n, k;
string s[60];

bool check(char c){
	FOR(i,0,n)
		FOR(r,0,n){
			bool ok = true;
			if (i+k<=n){
				FOR(j,0,k)
					if (s[i+j][r]!=c) ok = false;
				if (ok) return true; 
			}

			if (r+k<=n){
				ok = true;
				FOR(j,0,k)
					if (s[i][r+j]!=c) ok = false;
				if (ok) return true; 
			}

			if (i+k<=n && r+k<=n){
				ok = true;
				FOR(j,0,k)
					if (s[i+j][r+j]!=c) ok = false;
				if (ok) return true; 
			}

			if (i+k<=n && r+k<=n){
				ok = true;
				FOR(j,0,k)
					if (s[i+k-1-j][r+j]!=c) ok = false;
				if (ok) return true; 
			}
		}
	return false;
}

int main(){
	int t;
	cin >> t;
	FORE(z,1,t){
		cin >> n >> k;
		FOR(i,0,n)
			cin >> s[i];
		FOR(i,0,n)
			for (int r=n-1;r>0;--r)
				if (s[i][r]=='.')
				for (int c=r-1;c>=0;--c){
					if (s[i][c]!='.') {
						s[i][r]=s[i][c];
						s[i][c]='.';
						break;
					}
				}
		bool B=check('B'), R=check('R');

		printf("Case #%d: ",z);
		if (B&&R) puts("Both");
		if (!B&&R) puts("Red");
		if (B&&!R) puts("Blue");
		if (!B&&!R) puts("Neither");
	}
	return 0;
}
