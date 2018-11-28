#pragma comment (linker, "/STACK:90000000")
#define _CRT_SECURE_NO_DEPRECATE
#define _CRT_SECURE_NO_WARNINGS
#include <string>
#include <vector>
#include <cmath>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <iostream>
#include <cfloat>
#include <cstdio>
#include <sstream>
#include <utility>
#define forn(i, n) for (int i = 0; i < (int)(n); ++i)
#define forv(i, v) for (int i = 0; i < (int)(v.size()); ++i)
#define fors(i, s) for (int i = 0; i < (int)(s.length()); ++i)
#define all(a) a.begin(), a.end()
#define pb push_back
#define PII pair<int, int>
#define mp make_pair
#define VI vector<int>
#define VS vector<string>
#define lng long long
using namespace std;

char src[100][100];

void solve(int tc){
	int n, m;
	scanf("%d %d\n", &n,  &m);
	forn(i,n)gets(src[i]);
	bool ok = true;
	for(;;){
		bool found=false;
		forn(i,n)forn(j,m){
			if (src[i][j]=='#'){
				found=true;
				if ((i==0||src[i-1][j]=='.'||src[i-1][j]=='/'||src[i-1][j]=='\\')&&(j==0||src[i][j-1]=='.'||src[i][j-1]=='/'||src[i][j-1]=='\\')){
					if (i+1<n&&j+1<m&&src[i+1][j]=='#'&&src[i][j+1]=='#'&&src[i+1][j+1]=='#'){
						src[i][j]=src[i+1][j+1]='/';
						src[i+1][j]=src[i][j+1]='\\';
						goto l1;
					}else ok=false;
				}else ok=false;
			}
		}
		l1:
		if (!ok)break;
		if (!found)break;
	}
	printf("Case #%d:\n", tc);
	if (!ok)printf("Impossible\n");else {
		forn(i,n){
			forn(j,m)cout<<src[i][j];
			cout<<endl;
		}
		
	}

}

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int tc;
	cin >> tc;
	forn(i, tc)solve(i+1);
	return 0;
}
