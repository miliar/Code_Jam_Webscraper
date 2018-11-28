#include <iostream>
#include <math.h>
#include <stdlib.h>
#include <iomanip>
#include <vector>
#include <string>
#pragma comment (linker, "/STACK:16000000")
using namespace std;
#define inf 2123456789
#define INPUT "in.in"
#define OUTPUT "out.out"

int main()
{
	freopen(INPUT, "r", stdin);
	freopen(OUTPUT, "w", stdout);
	int t; cin >> t;
	long long n, A, B, C, D, x, y, M;
	for (int i=0; i<t; i++) {
		cin >> n >> A >> B >> C >> D >> x >> y >> M;
		long long s[101][2];
		s[0][0] = x; s[0][1] = y;
	//	cout << x << ' ' << y << endl;
		for (int u=1; u<n; u++) {
			x = (A * x + B) % M;
			y = (C * y + D) % M;
			s[u][0] = x; s[u][1] = y;
		//	cout << x << ' ' << y << endl;
		}
		int sum = 0;
		for (int u=0; u<n; u++) {
			for (int t=u+1; t<n; t++) {
				for (int r=t+1; r<n; r++) {
					if ((s[u][0] + s[t][0] + s[r][0]) % 3 == 0 &&
						(s[u][1] + s[t][1] + s[r][1]) % 3 == 0)
						sum++;
				}
			}
		}
		cout << "Case #" << i+1 << ": " << sum << endl;
	}


	return 0;
}