#include <iostream>
#include <vector>
#include <functional>

using namespace std;

int main()
{
	int t;
	cin >> t;
	
	for (int i=0; i<t; ++i) {
		int n;
		cin >> n;
		vector<int> u(n), v(n);
		for (int j=0; j<n; ++j) {
			cin >> u[j];
		}
		for (int j=0; j<n; ++j) {
			cin >> v[j];
		}
		sort(u.begin(),u.end());
		sort(v.begin(),v.end(),greater<int>());
		
		int res = 0;
		for (int j=0; j < n; ++j) {
			res += (u[j]*v[j]);
		}
		
		cout << "Case #" << i+1 << ": " << res << '\n';
	}
}

