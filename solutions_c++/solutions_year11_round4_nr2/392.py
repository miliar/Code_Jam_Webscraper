#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <iostream>
#include <vector>
#include <list>
#include <algorithm>
#include <functional>
#include <map>
#include <set>
#include <cstring>
#include <string>
#include <cctype>
#include <cassert>

using namespace std;

#define pb push_back
#define mp make_pair
#define rep(i,n) for(int i = 0; i < (n); i++)
#define repr(i,b,e) for(int i = (b); i <= (e); i++)
#define INF (1001001001)
#define EPS (1e-15)

#define pr(x) do{cout << (#x) << " = " << (x) << endl;}while(0)
#define pri(x,i) do{cout << (#x) << "[" << i << "] = " << (x[i]) << endl;}while(0)
#define pra(x,n) rep(__i,n) pri(x,__i);
#define prar(x,b,e) repr(__i,b,e) pri(x,__i);

typedef long long llint;
typedef pair<int, int> pint;
typedef vector<int> vint;

int in() {
	int a;
	scanf("%d ", &a);
	return a;
}

int W, H;
int sheet[512][512];
int sum[512][512];

int s(int y, int x) {
	if(x < 0 || y < 0) return 0;
	else return sum[y][x];
}

int getSum(int y, int x, int height, int width) {
	int y2 = y + height - 1;
	int x2 = x + width - 1;
	y--;
	x--;
	return s(y2, x2) - s(y2, x)- s(y, x2)+ s(y, x);
}

int main() {
	int T = in();
	rep(tst, T) {
		printf("Case #%d: ", tst + 1);
		
		H = in();
		W = in();
		int d = in();
		
		rep(y, H) {
			char temp[1024];
			scanf("%s ", temp);
			int yoko = 0;
			rep(x, W) {
				sheet[y][x] = temp[x] - '0';
				yoko += sheet[y][x];
				sum[y][x] = yoko;
				if(y > 0) sum[y][x] += sum[y - 1][x];
			}
		}
		/*
		rep(y, H) {
			rep(x, W) printf("%3d", sum[y][x]);
			cout << endl;
		}
		*/
		
		int N = min(W, H);
		for(int ans = N; ans >= 3; ans--) {
			for(int y = 0; y + ans <= H; y++) {
				for(int x = 0; x + ans <= W; x++) {
					int width = ans / 2;
					int next = ans % 2 == 1 ? (ans + 1) / 2 : ans / 2;
					//bool ok = y == 1 && x == 1 && ans == 5;
					
					int hidariue = sheet[y][x];
					int migiue = sheet[y][x + ans - 1];
					int hidarisita = sheet[y + ans - 1][x];
					int migisita = sheet[y + ans - 1][x + ans - 1];
					
					int sum1 = 0, sum2 = 0;
					
					rep(i, ans) {
						int weigh = i * 2 - ans + 1;
						int hoge = getSum(y, x + i, ans, 1);
						if(i == 0) hoge -= hidariue + hidarisita;
						if(i == ans - 1) hoge -= migiue + migisita;
						
						sum1 += weigh * hoge;
					}
					if(sum1 != 0) continue;
					
					rep(i, ans) {
						int weigh = i * 2 - ans + 1;
						int hoge = getSum(y + i, x, 1, ans);
						if(i == 0) hoge -= hidariue + migiue;
						if(i == ans - 1) hoge -= hidarisita + migisita;
						
						sum2 += weigh * hoge;
					}
					if(sum2 != 0) continue;
					
					/*
					int sum1 = getSum(y, x, ans, width) - hidariue - hidarisita;
					int sum2 = getSum(y, x + next, ans, width) - migiue - migisita;
					if(sum1 != sum2) continue;
					
					int sum3 = getSum(y, x, width, ans) - hidariue - migiue;
					int sum4 = getSum(y + next, x, width, ans) - hidarisita - migisita;
					if(sum3 != sum4) continue;
					/*
					pr(width);
					pr(next);
					pr(sum1);
					pr(sum2);
					pr(sum3);
					pr(sum4);
					*/
					cout << ans << endl;
					goto HOGE;
				}
			}
		}
		
		cout << "IMPOSSIBLE" << endl;
		HOGE:;
	}
	return 0;
}
