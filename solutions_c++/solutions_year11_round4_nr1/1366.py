#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <map>
#include <hash_map>
#include <ctime>
#include <cstdio>
#include <cstdlib>
#pragma comment(linker, "/STACK:17000000")
using namespace std;
using namespace stdext;
ifstream cin("input.txt");
ofstream cout("output.txt");

const double eps = 1e-12;

struct ve{
	double b, e, w;
};

struct cmp{
	bool operator() (const ve & a, const ve & b){
		return (a.w < b.w);
	}
};

int main(){
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int counttest;
	cin >> counttest;
	for(int test = 1; test <= counttest; ++test){
		double n, X, S, R, T;
		cin >> X >> S >> R >> T >> n;
		vector<ve> a(n + 1);
		a[0].b = 0;
		double le = 0;
		a[0].w = 0;
		a[0].e = 0;
		for(int i = 1; i <= n; ++i){
			cin >> a[i].b >> a[i].e >> a[i].w;
			le += a[i].b - a[i - 1].e;
		}
		le += X - a[n].e;
		a[0].e = le;
		if (test == 12){
			bool fas = false;
		}
		sort(a.begin(), a.end(), cmp());
		if (test == 17){
			bool fa = false;
		}
		double ans = 0;
		for(int i = 0; i < n + 1; ++i){
			if (ans < T - eps){
				double he = (double)(a[i].e - a[i].b) / (double)(R + a[i].w);
				if (he + ans < T + eps)
					ans += he;
				else{
					double l = (a[i].e - a[i].b) - (double)(R + a[i].w) * ((double)T - ans);
					ans = (double)T + (double)l / (double)(S + a[i].w);
				}
			}
			else
				ans += (double)(a[i].e - a[i].b) / (double)(S + a[i].w);
		}
		printf("Case #");
		printf("%d", test);
		printf(": ");
		printf("%.6f", ans);
		printf("\n");
	}
}