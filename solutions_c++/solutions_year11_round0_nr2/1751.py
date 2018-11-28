#include <iostream>
using namespace std;

char com[256][256], opp[256][256];
char a[10000];

void solve()
{
	memset(com, 0, sizeof(com));
	memset(opp, 0, sizeof(opp));
	int n;
	cin >> n;
	for(int i = 0; i < n; ++i) {
		char c1, c2, c3;
		cin >> c1 >> c2 >> c3;
		com[c1][c2] = com[c2][c1] = c3;
	}

	cin >> n;
	for(int i = 0; i < n; ++i) {
		char c1, c2;
		cin >> c1 >> c2;
		opp[c1][c2] = opp[c2][c1] = 1;
	}

	int len = 0;
	cin >> n;
	for(int i = 0; i < n; ++i) {
		char c;
		cin >> c;
		a[len++] = c;
		while (len >= 2) {
			char c1 = a[len - 1], c2 = a[len - 2];
			if (com[c1][c2]) {
				a[len - 2] = com[c1][c2];
				--len;
				continue;
			}
			for(int i = 0; i < len - 1; ++i)
				if (opp[a[i]][a[len - 1]]) {
					len = 0;
				}
			break;
		}
	}

	cout << '[';
	for(int i = 0; i < len - 1; ++i)
		cout << a[i] << ", ";
	if (len)
		cout << a[len - 1];
	cout << "]\n";
}

int main()
{
	freopen("in.txt", "rt", stdin);
	freopen("out.txt", "wt", stdout);
	int t; 
	cin >> t;
	for(int i = 0; i < t; ++i) {
		printf("Case #%d: ", i + 1);
		solve();
	}
	return (0);
}
