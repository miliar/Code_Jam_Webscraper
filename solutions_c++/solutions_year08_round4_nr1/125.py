#include <iostream>
#include <vector>

using namespace std;

const int INFTY = 1 << 28;

struct Node
{
	int g;
	int c;
	int n0;
	int n1;

public:
	Node() : g(2), c(0), n0(INFTY), n1(INFTY)
	{
	}
};

int main()
{
	int nCase;
	cin >> nCase;

	for(int iCase = 1; iCase <= nCase; iCase++) {
		int m, v;
		cin >> m >> v;

		vector<Node> a(m);

		int n = (m - 1) / 2;

		for(int i = 0; i < n; i++)
			cin >> a[i].g >> a[i].c;

		for(int i = n; i < m; i++) {
			int k;
			cin >> k;
			if(k == 0) { a[i].n0 = 0; } else { a[i].n1 = 0; }
		}

		for(int i = n - 1; i >= 0; i--) {
			// OR
			if(a[i].g == 0 || a[i].c == 1) {
				int extra = (a[i].g == 0) ? 0 : 1;
				a[i].n0 = min(a[i].n0, a[2*i+1].n0 + a[2*i+2].n0 + extra);
				a[i].n1 = min(a[i].n1, a[2*i+1].n1 + a[2*i+2].n0 + extra);
				a[i].n1 = min(a[i].n1, a[2*i+1].n0 + a[2*i+2].n1 + extra);
				a[i].n1 = min(a[i].n1, a[2*i+1].n1 + a[2*i+2].n1 + extra);
			}
			// AND
			if(a[i].g == 1 || a[i].c == 1) {
				int extra = (a[i].g == 1) ? 0 : 1;
				a[i].n0 = min(a[i].n0, a[2*i+1].n0 + a[2*i+2].n0 + extra);
				a[i].n0 = min(a[i].n0, a[2*i+1].n1 + a[2*i+2].n0 + extra);
				a[i].n0 = min(a[i].n0, a[2*i+1].n0 + a[2*i+2].n1 + extra);
				a[i].n1 = min(a[i].n1, a[2*i+1].n1 + a[2*i+2].n1 + extra);
			}
		}

		int ans = (v == 0) ? a[0].n0 : a[0].n1;

		cout << "Case #" << iCase << ": ";
		if(ans == INFTY) { cout << "IMPOSSIBLE"; } else { cout << ans; }
		cout << endl;
	}
}
