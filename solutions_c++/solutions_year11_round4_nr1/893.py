#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
struct node{
	int a, b, c;
	node(int x = 0, int y = 0, int z = 0) : a(x), b(y), c(z){}
};

bool operator < (const node &p1, const node &p2){
	return p1.c < p2.c;
}

vector<node> data;
int main(){
	int cases;
	scanf("%d", &cases);
	for (int tt = 0; tt < cases; ++tt){
		int x, s, r, t, n;
		data.clear();
		scanf("%d%d%d%d%d", &x, &s, &r, &t, &n);
		int prev = 0;
		for (int i = 0; i < n; ++i){
			int b, e, w;
			scanf("%d%d%d", &b, &e, &w);
			if (prev != b){
				data.push_back(node(prev, b, s));
			}
			data.push_back(node(b, e, w + s));
			prev = e;
		}
		data.push_back(node(prev, x, s));
		sort(data.begin(), data.end());
		double res = 0;
		int i = 0;
		double rest = t;
		while (i < data.size()){
			double nt = (double)(data[i].b - data[i].a) / (data[i].c + r - s);
			if (nt < rest + 1e-6){
				res += nt;
				rest -= nt;
				++i;
			} else {
				res += rest;
				res += (nt - rest) * (data[i].c + r - s) / (data[i].c);
				++i;
				break;
			}
		}
		for (; i < data.size(); ++i){
			res += (double)(data[i].b - data[i].a) / data[i].c;
		}
		printf("Case #%d: %.10lf\n", tt + 1, res);
	}
}