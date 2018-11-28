#include <iostream>
using namespace std;
int n, v, leaf;
const int MAXN = 10011;
struct node{
	bool can, type;
	int x;
} data[MAXN];
int f[MAXN][2];
const int MAX = 999999999;
int Get(int);
int calc(int, int);
int GetValue(int x){
	if (x >= leaf) return data[x].x;
	if (data[x].type) data[x].x = GetValue(2 * x) & GetValue(2 * x + 1);
		else data[x].x = GetValue(2 * x) | GetValue(2 * x + 1);
	return data[x].x;
}
int Get(int x, int v){
	if (data[x].type){
		if (v == 1) return calc(2 * x, 1) + calc(2 * x + 1, 1); else{
			int temp = calc(2 * x, 1) + calc(2 * x + 1, 0);
			temp = min(temp, calc(2 * x, 0) + calc(2 * x + 1, 1));
			temp = min(temp, calc(2 * x, 0) + calc(2 * x + 1, 0));
			return temp;
		}
	} else {
		if (v == 0) return calc(2 * x, 0) + calc(2 * x + 1, 0); else{
			int temp = calc(2 * x, 1) + calc(2 * x + 1, 0);
			temp = min(temp, calc(2 * x, 0) + calc(2 * x + 1, 1));
			temp = min(temp, calc(2 * x, 1) + calc(2 * x + 1, 1));
			return temp;
		}
	}
}
int calc(int x, int v){
	if (data[x].x == v) return 0;
	if (x >= leaf) return MAX;
	if (f[x][v] != -1) return f[x][v];
	int ans = MAX;
	if (data[x].can){
		data[x].type = !data[x].type;
		ans = min(ans, Get(x, v) + 1);
		data[x].type = !data[x].type;
	}
	ans = min(ans, Get(x, v));
	return ans;
}
int main(){
	int cases;
	cin >> cases;
	for (int t = 0; t != cases; ++t){
		cin >> n >> v;
		memset(data, 0, sizeof(data));
		for (int i = 0; i != (n - 1) / 2; ++i){
			int g, c;
			cin >> g >> c;
			data[i + 1].type = (g == 1 ? true : false);
			data[i + 1].can = (c == 1 ? true : false);
		}
		leaf = (n - 1) / 2 + 1;
		for (int i = 0; i != (n + 1) / 2; ++i){
			int x; cin >> x;
			data[leaf + i].x = x;
		}
		GetValue(1);
		memset(f, -1, sizeof(f));
		int ans = calc(1, v);
		if (ans >= MAX) printf("Case #%d: IMPOSSIBLE\n", t + 1); else 
		printf("Case #%d: %d\n", t + 1, calc(1, v));
	}
	return 0;
}