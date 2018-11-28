#define _CRT_SECURE_NO_DEPRECATE

#include <iostream>
#include <fstream>
#include <cmath>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <algorithm>
#include <ctime>

using namespace std;

#define forn(i, n) for(int i = 0; i < (int)(n); ++i)
#define fore(i, a, b) for(int i = a; i < (int)(b); ++i)
#define pii pair<int,int>
#define pb push_back
#define mp make_pair
#define all(a) a.begin,a.end()
#define ll long long

int a[555][555];

int main(){
#ifndef ONLINE_JUDGE
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif

	int t;
	cin >> t;
	forn(tt, t){
		int n, m, d;
		cin >> n >> m >> d;
		string s;
		getline(cin, s);
		forn(i, n){
			getline(cin, s);
			forn(j, m){
				a[i][j] = s[j] - '0';
			}
		}
		bool ok = 0;
		int res = -1;
		for(int k = min(n, m); k >= 3; k--) {
			if(ok)break;
			forn(i, n - k + 1){
				forn(j, n - k + 1){
					int si = 0, sj = 0;
					int mm = 0;
					fore(ii, i, i + k){
						fore(jj, j , j + k){
							if(!((i == ii && j == jj) || (ii == i + k - 1 && jj == j) ||
								(ii == i && jj == j + k - 1) || (ii == i + k - 1 && jj == j + k - 1)) )
							{
								si += (ii) * (d + a[ii][jj]);
								sj += (jj) * (d + a[ii][jj]);
								mm += (d + a[ii][jj]);
							}
						}
					}
					if(si * 2 == mm * (i + i + k - 1) && sj * 2 == mm * (j + j + k - 1) ) {
						ok = 1;
						res = k;
						break;
					}
				}
			}
		}

		printf("Case #%d: ", tt + 1);
		if(res < 0)
			puts("IMPOSSIBLE");
		else
			printf("%d\n", res);
	}
	
	return 0;
}