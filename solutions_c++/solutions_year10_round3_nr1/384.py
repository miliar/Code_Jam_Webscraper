#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

const int N = 10005;
struct Node {
	int a, b;
	bool operator < (Node& t)
	{
		return a < t.a;
	}
};
Node node[N];

int main()
{
	freopen("data.in", "r", stdin);
	freopen("result.out", "w", stdout);
	int tn, curt;
	cin >> tn;
	for(curt = 1; curt <= tn; ++curt) {
		int n;
		int i, j;
		cin >> n;
		for(i = 0; i < n; ++i) cin >> node[i].a >> node[i].b;
		sort(node, node+n);

		int ans = 0;
		for(i = 0; i < n; ++i) {
			for(j = i-1; j >= 0; --j) {
				if(node[j].b > node[i].b) ans++;
			}
		}

		cout << "Case #" << curt << ": ";
		cout << ans << endl;
	}
	return 0;
}