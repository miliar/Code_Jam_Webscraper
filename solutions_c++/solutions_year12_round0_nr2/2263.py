#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <algorithm>
#include <string>
#include <string.h>
#include <vector>
#include <set>
#include <map>
#include <complex>

using namespace std;

const int inf = (int)1e9;

int d[200][200];

inline void solve(int test){
	int n, s, p;
	scanf("%d %d %d", &n, &s, &p);
	for(int i = 0; i <= n; i++){
		for(int j = 0; j <= s; j++){
			d[i][j] = -inf;
		}
	}
	d[0][0] = 0;
	for(int i = 1; i <= n; i++){
		int t;
		scanf("%d", &t);
		bool f1 = false, f2 = false, f3 = false, f4 = false;
		for(int j = 0; j <= 10; j++){
			for(int z = 0; z <= 10; z++){
				for(int h = 0; h <= 10; h++){
					if(j + z + h != t){
						continue;
					}
					int maxd = max(abs(j - z), max(abs(j - h), abs(z - h)));
					if(maxd > 2){
						continue;
					}
					int best = max(j, max(z, h));
					if(maxd < 2 && best < p){
						f1 = true;
					}
					if(maxd < 2 && best >= p){
						f2 = true;
					}
					if(maxd == 2 && best < p){
						f3 = true;
					}
					if(maxd == 2 && best >= p){
						f4 = true;
					}
				}
			}
		}
		for(int j = 0; j <= s; j++){
			if(f1){
				d[i][j] = max(d[i][j], d[i - 1][j]);
			}
			if(f2){
				d[i][j] = max(d[i][j], d[i - 1][j] + 1);
			}
			if(j > 0 && f3){
				d[i][j] = max(d[i][j], d[i - 1][j - 1]);
			}
			if(j > 0 && f4){
				d[i][j] = max(d[i][j], d[i - 1][j - 1] + 1);
			}
		}
	}
	printf("Case #%d: %d\n", test, d[n][s]);
}

int main(){
	//freopen("abelian.in", "r", stdin);
	//freopen("abelian.out", "w", stdout);
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d\n", &t);
	for(int i = 0; i < t; i++){
		solve(i + 1);
	}
	return 0;
}