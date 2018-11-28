#include <cstdio>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <sstream>
#include <iostream>
#include <algorithm>

using namespace std;

int m[1024];
int pr[10][512];

int tab[11][1024][11];

int main(){
	int tc, t;
	scanf("%d", &tc);
	for(t=0;t<tc;++t){
		int p;
		scanf("%d", &p);
		int n = 1<<p;
		for(int i=0; i<n; ++i){
			scanf("%d", &m[i]);
		}
		for(int i=p-1; i>=0; --i){
			for(int j=0; j<(1<<i); ++j){
				scanf("%d", &pr[i][j]);
			}
		}
		for(int i=0; i<n; ++i){
			for(int j=0; j<=p; ++j)
				tab[p][i][j] = 102400000;
			for(int j=0; j<=m[i]; ++j)
				tab[p][i][j] = 0;
		}
		for(int i=p-1; i>=0; --i){
			for(int j=0; j<(1<<i); ++j){
				//tab[i][j][0] = min(102400000, tab[i+1][j*2][0] + tab[i+1][j*2+1][0] + pr[i][j]);
				for(int k=0; k<p; ++k){
					int a, b;
					a = tab[i+1][j*2][k] + tab[i+1][j*2+1][k] + pr[i][j];
					b = tab[i+1][j*2][k+1] + tab[i+1][j*2+1][k+1];
					tab[i][j][k] = min(102400000, min(a, b));
				}
			}
		}
		int res = INT_MAX;
		for(int i=0; i<=p; ++i)
			res = min(res, tab[0][0][i]);
		printf("Case #%d: %d\n", t+1, tab[0][0][0]);
	}
}
