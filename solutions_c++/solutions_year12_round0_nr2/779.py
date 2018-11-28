#include <iostream>
#include <algorithm>

using namespace std;

int main(){
	int T; 
	int n, s, p;
	int t[101];
	int ans;

	cin >> T;
	for (int cnt = 0; cnt < T; ++cnt){
		cin >> n >> s >> p;
		for (int i=0; i<n; ++i)
			cin >> t[i];

		sort(t, t+n);

		ans = 0;
		for (int i=n-1; i>=0; --i){
			if (t[i]>=3*p-2)
				ans++;
			else if (t[i]>=3*p-4 && p>=2 && s>0){
				ans++; 
				s--;
			}
		}
		cout << "Case #" << cnt+1 << ": " << ans << endl; 
	}

	return 0;
}
