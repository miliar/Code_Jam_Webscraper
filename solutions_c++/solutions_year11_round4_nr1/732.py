//USER LGQ
#include <cstdio>
#include <iostream>
#include <cstring>
#include <string>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>
#include <stack>
#include <cmath>
#include <set>
#include <deque>

using namespace std;

const int maxn = 100010;
const double eps = 1e-10;

struct Node{
	int b, e, w;
	Node(){}
	Node(int bb, int ee, int ww) {
		b = bb, e = ee, w = ww;
	}
	void input(){
		scanf("%d %d %d", &b, &e, &w);
		if (b > e)
			swap(b, e);
	}
	void out(){
		printf("%d %d %d\n", b, e, w);
	}

}node[maxn];

bool cmp1(const Node &x, const Node &y) {
	return x.b < y.b;
}
bool cmp(const Node &x, const Node &y) {
	return x.w < y.w;
}
int main() {
	int T;
	scanf("%d", &T);
	int x, s, r, t, n;
	int cas = 1;
	while (T--) {
		scanf("%d %d %d %d %d", &x, &s, &r, &t, &n);
		for (int i = 0; i < n; i++) {
			node[i].input();
		}
		sort(node, node + n, cmp1);
		int m = n;
		int now = 0;
		for (int i = 0; i < n; i++) {
			if (now < node[i].b) {
				node[m++] = Node(now, node[i].b, 0);
			}
			now = node[i].e;
		}
		if (now != x){
			node[m] = Node(node[n-1].e, x, 0);
			m++;
		}
		n = m;
		//for (int i = 0; i < n; i++) {
		//	node[i].out();
		//}
		double sum = 0;        double res = 0;        bool flag = 0;		sort(node, node + n, cmp);        for (int i = 0; i < n; i++) {            Node tmp = node[i];            if (flag == true) 			{                res += 1.0*(tmp.e - tmp.b)/(tmp.w+s);            } 			else 			{                double tttmp = 1.0*(tmp.e - tmp.b)/(tmp.w+r);                if (tttmp + sum + eps > t) {                    flag = 1;					res += (1.0 * t - sum);                    res += 1.0 * (tmp.e - tmp.b - (tmp.w + r) * (1.0 * t - sum) ) / ( tmp.w + s );                } else {                    res += tttmp;                    sum += tttmp;                }            }        }
		printf("Case #%d: %.9lf\n", cas++, res);
	}


	return 0;
}