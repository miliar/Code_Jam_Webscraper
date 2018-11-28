#include <iostream>
#include <iomanip>
#include <cmath>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
using namespace std;

int T;

int arr[1000005];
int c[1005];

int main(){
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);
	cin >> T;
	for (int I=0; I<T; I++){
		cout << "Case #" << I+1 << ": ";
		long long l, t, n, C = 0, kol = 0;
		long long ans = 0;
		cin >> l >> t >> n >> C;
		for (int i=0; i<C; i++){
			cin >> c[i];
		}
		for (int i=0; i<n; i++){
			arr[i] = c[i%C];
		}
		for (int i=0; i<n; i++){
			if (2*arr[i] < t){
				t -= 2*arr[i];
				ans += 2*arr[i];
				kol = n;
			} else {
				arr[i] -= t/2;
				kol = i;
				ans += t;
				break;
			}
		}
		sort(arr + kol, arr+n);
		reverse(arr + kol, arr+n);
		for (int i=kol; i<n; i++){
			if (i - kol < l){
				ans += arr[i];
			} else {
				ans += 2*arr[i];
			}
		}
		cout << ans << endl;
	}
	return 0;
}