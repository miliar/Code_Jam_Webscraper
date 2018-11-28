#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <map>

using namespace std;

int main()
{
 	int t, n, i;
 	int _cnt = 1;
 	
 	cin >> t;
 	
 	long long ans;
 	
 	while(t--) {
			 
		cin >> n;	   
	    vector<int> v1(n), v2(n);
		
		for(i = 0; i < n; i++)  cin >> v1[i];
		for(i = 0; i < n; i++)  cin >> v2[i];
		
		sort(v1.begin(), v1.end());
		sort(v2.begin(), v2.end());
		reverse(v2.begin(), v2.end());
		
 		ans = 0ll;
 		for(i = 0; i < n; i++) ans += (long long) v1[i]*v2[i];
 		
 		cout << "Case #" << _cnt++ << ": " << ans << endl;
 		
	}
 	
 	return 0;
}
