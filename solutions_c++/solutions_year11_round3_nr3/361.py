// Paste me into the FileEdit configuration dialog

#include <cmath>
#include <ctime>
#include <iostream>
#include <string>
#include <vector>
using namespace std;
int a[10001];
int main(int argc, char *argv[]) {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tt;
	cin >> tt;
	for (int t = 1; t<=tt; ++t)
	{
		int n, r, c;
		cin >> n >> r >> c;
		for (int i = 0; i < n; ++i)
			cin >> a[i];

		int ans = -1;
		for (int d = r; d<=c; ++d)
		{
			bool ok = true;
			for (int j = 0; j < n; ++j)
				ok = ok && (a[j] % d == 0 || d % a[j] == 0);
			if (ok)
			{
				ans = d;
				break;
			}
		}
		cout << "Case #" << t << ": ";
		if (ans == -1)
			cout <<  "NO";
		else 
			cout << ans;
		cout << endl;
		
	}
	fclose(stdout);
}
