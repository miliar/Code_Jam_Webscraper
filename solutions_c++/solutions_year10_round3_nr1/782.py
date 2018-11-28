#include <iostream>
#include <cstring>
#include <vector>
#include <set>

using namespace std;

struct segment {
	int x, y;
	bool operator < (const segment &a) const{ 
		return (x < a.x);
	}
} a[1010];

int main ()
{
	freopen ("a.in", "r", stdin);
	freopen ("a.out", "w", stdout);

	int T, n;

	cin >> T;

	for (int t = 0; t < T; t++) {
		int res = 0;
		cin >> n;
		for (int i = 0; i < n; i++) 
			cin >> a[i].x >> a[i].y;
		for (int i = 0; i < n-1; i++) {
			for (int j = i+1; j < n; j++) {
				if((a[i].x > a[j].x && a[i].y < a[j].y)
				|| (a[i].x < a[j].x && a[i].y > a[j].y)) res++;
			}
		}
		cout << "Case #" << t+1 << ": " << res << endl;
	}

	return 0;
}