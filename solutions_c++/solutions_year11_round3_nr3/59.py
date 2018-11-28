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

int f[1005];

int main(){
	freopen("C.in", "r", stdin);
	freopen("C.out", "w", stdout);
	cin >> T;
	for (int I=0; I<T; I++){
		cout << "Case #" << I+1 << ": ";
		int N, L, H;
		cin >> N >> L >> H; 
		for (int i=0; i<N; i++){
			cin >> f[i];
		}
		int ans = -1;
		for (int i=L; i<=H && ans == -1; i++){
			ans = i;
			for (int j=0; j<N; j++){
				if (f[j] % i != 0 && i % f[j] != 0){
					ans = -1;
					break;
				}
			}
		}
		if (ans == -1){
			cout << "NO\n";
		} else {
			cout << ans << endl;
		}
	}
	return 0;
}