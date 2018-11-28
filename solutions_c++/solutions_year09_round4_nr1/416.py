#include <iostream>
#include <string>
using namespace std;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin>>t;
	for (int nt = 1; nt <= t; ++nt) {
		int v[41];
		int n;
		cin>>n;
		for (int i = 1; i <= n; ++i) {
			string str;
			cin>>str;
			v[i] = 0;
			for (int j = str.size(); j ; --j)
				if (str[j - 1] == '1')
				{v[i] = j; break;}
		}
		int ret = 0;
		for (int i = 1; i <= n; ++i) {
			if (v[i] > i) {
				for (int j = i + 1; true; ++j)
					if (v[j] <= i) {
						int x = v[j];
						for (int k = j; k > i; --k) {
							v[k] = v[k - 1];
						}
						v[i] = x;
						ret += j - i;
						break;
					}
				
			}
		}
		printf ("Case #%d: %d\n", nt, ret);
	}
	return 0;
}