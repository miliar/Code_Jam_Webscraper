#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>
#include <iostream>
#include <sstream>
#include <string.h>
#include <string>

#include <algorithm>
#include <set>
#include <map>
#include <deque>
#include <vector>

#include <cmath>
#include <time.h>
#include <cassert>
using namespace  std;
#pragma comment(linker, "/STACK:32108864")

#define lint long long
template<typename T> T abs(T a){ if ( a < 0 ) return -a; return a; }
template<typename T> T sqr(T a) { return (a) * (a); }
template<typename T> int size(T& a) { return (int)((a).size()); }
#define all(a) (a).begin(),(a).end()


void initf(){
#ifdef air
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
}
const int maxn = 110;
char s[maxn][maxn];
int nx[maxn][maxn];
bool check(int n, int m){
	for(int i =0 ; i <= n; ++i)
		for(int j = 0; j <= m; ++j)
			if ( s[i][j] == '1' ) return false;
	return true;
}

int main(){


	initf();
	int test;
	scanf("%d", &test);
	

	for(int t = 0; t < test; ++t){

		memset(s, 0, sizeof(s));
		memset(nx, 0, sizeof(nx));

		int R;
		scanf("%d", &R);
		int maxx = 0, maxy = 0;
		for(int i = 0; i < R; ++i){
			int x1, y1, x2, y2;
			scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
			-- x1, -- y1, -- x2, -- y2;
			maxx = max(maxx, x2);
			maxy = max(maxy, y2);
			for(int u = x1; u <= x2; ++u)
				for(int w = y1; w <= y2; ++w)
					s[w][u] = '1';
		}
		for(int i = 0; i <= maxy; ++i)
			for(int j = 0; j <= maxx; ++j)
				if (s[i][j] != '1')s[i][j] = '0';
		int res = 0;
		while (true){
			if (check(maxy, maxx)) break;
			++res;
			for(int i = 0; i <= maxy; ++i)
				for(int j = 0; j <= maxx; ++j){
				  nx[i][j] = s[i][j];
				}
			for(int i = 0; i <= maxy ; ++i)
				for(int j = 0; j <= maxx ; ++j){
					if ( (i != 0 && s[i - 1][j] == '1')&& (j != 0 && s[i][j - 1] == '1'))nx[i][j] = '1';
					else if ( (i == 0 || s[i - 1][j] == '0') && (j == 0 || s[i][j - 1] == '0'))nx[i][j] = '0';
				}
			for(int i = 0; i <= maxy; ++i)
				for(int j = 0; j <= maxx; ++j){
					s[i][j] = nx[i][j];
				}
		}
		printf("Case #%d: %d\n", t + 1, res);

	}


	return 0;
}