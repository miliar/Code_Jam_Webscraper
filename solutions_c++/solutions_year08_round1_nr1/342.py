#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <functional>
using namespace std;

int main() 
{
	
	int T,n;
	
	cin >> T;
	for (int cas=1; cas<=T;++cas)
	{
	
		cin >> n;
		long long ans = 0;
		int i,t;
		vector<int> a,b;
		for (i=0;i<n;++i) {
			cin >> t;
			a.push_back(t);
		}
		for (i=0;i<n;++i) {
			cin >> t;
			b.push_back(t);
		}
		
		sort(a.begin(),a.end());
		sort(b.begin(),b.end(),greater<int>());
		
		for (i=0; i<n; ++i)
		{
			ans += (long long)a[i] * (long long)b[i];
		}
		
		cout << "Case #" << cas << ": ";
		cout << ans << endl;
	}
	
	return 0;
}