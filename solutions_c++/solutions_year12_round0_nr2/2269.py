#include <iostream>
#include <string>

using namespace std;

int main(int argc, char* argv[])
{
	int t, n, s, p, x;
	cin >> t;
	for (int tcase = 1; tcase <= t; ++tcase) {
		cin >> n >> s >> p;	
		int ans = 0;
		while(n-- > 0) {
			cin >> x;
			int avg = x / 3;
			if (avg >= p) {
				++ans;
				continue;
			}
			switch (x % 3) {
			case 0: 
				if (avg + 1 == p && avg -1 >= 0 && s-- > 0) ++ans;
				break;
			case 1: 
				if (avg + 1 == p) ++ans;
				break;
			case 2: 
				if (avg + 1 == p || avg + 2 == p && s-- > 0) ++ans;
				break;
			}
		}
		cout << "Case #" << tcase << ": " << ans; 
		if (tcase != t)	cout << endl;
	}
	return 0;
}