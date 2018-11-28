#include <iostream>
#include <math.h>
#include <stdlib.h>
#include <iomanip>
#include <vector>
#include <string>
#pragma comment (linker, "/STACK:16000000")
using namespace std;
#define inf 2123456789
#define INPUT "A-large.in"
#define OUTPUT "ans.out"

char s[101][101] = {0}, q[1001][101] = {0};
int main()
{
	freopen(INPUT, "r", stdin);
	freopen(OUTPUT, "w", stdout);
	int t; cin >> t;
	for (int n,m,i=0; i<t; i++) {
		cin >> n;
		cin.getline(s[0], 122);
		for (int u=0; u<n; u++) cin.getline(s[u], 122);
		cin >> m;
		cin.getline(q[0], 122);
		for (int u=0; u<m; u++) cin.getline(q[u], 122);

		int t[1001] = {0};
		for (int u=m-1; u>=0; u--) {
			for (int y=0; y<n; y++) {
				if (strcmp(s[y], q[u]) == 0) {
					int min = inf;
					for (int yy=0; yy<n; yy++)
						if (yy != y && t[yy] < min)
							min = t[yy];
					t[y] = min+1;
					break;
				}
			}
		}
		int min = inf;
		for (int yy=0; yy<n; yy++)
			if (t[yy] < min)
				min = t[yy];
		cout << "Case #" << i+1 << ": " << min << endl;
	}
	return 0;
}