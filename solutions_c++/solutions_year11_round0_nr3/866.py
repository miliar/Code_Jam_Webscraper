#include <iostream>
#include <cmath>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
using namespace std;

int arr[10005];
int main(){
	freopen("C.in", "r", stdin);
	freopen("C.out", "w", stdout);
	int t;
	cin >> t;
	for (int I=0; I<t; I++){
		cout << "Case #" << I+1 << ": ";
		int n, xr = 0, sum = 0, mn = 1<<30;
		cin >> n;
		for (int i=0; i<n; i++){
			cin >> arr[i];
			xr ^= arr[i];
			sum += arr[i];
			mn = min(arr[i], mn);
		}
		if (xr != 0){
			cout << "NO" << endl;
		} else {
			cout << sum - mn << endl;
		}
	}
	return 0;
}