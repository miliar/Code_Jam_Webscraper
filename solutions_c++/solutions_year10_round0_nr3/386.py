#include <iostream>
using namespace std;

long long price[1002];
long long run[1002];
long long g[1002];

int main(){
	int t;
	freopen("input3.txt", "r", stdin);
	freopen("output3.txt", "w", stdout);
	cin >> t;
	for (int I=0; I<t; I++){
		cout << "Case #" << I+1 << ": ";
		memset(price, -1, sizeof price);
		memset(run, -1, sizeof run);
		int R, k, n;
		long long sum = 0;
		cin >> R >> k >> n;
		for (int i=0; i<n; i++){
			cin >> g[i];
			sum += g[i];
		}
		if (sum <= k){
			cout << sum * R << endl;
		} else {
			int tec = 0, r = 0;
			long long pr = 0, ret = 0, prev = 0;
			while (price[tec] == -1 && R){
				if (!tec){
					price[tec] = 0;
					run[tec] = 0;
				} else {
					price[tec] = prev + pr;
					prev = price[tec];
					run[tec] = r;
				}
				pr = 0;
				while (pr + g[tec] <= k){
					pr += g[tec++];
					if (tec == n)
						tec = 0;
				}
				ret += pr;
				r++;
				R--;
			}
			ret += (pr + prev - price[tec])* (R / (r - run[tec]));
			R %= r - run[tec];
			for (int i=0; i<R; i++){
				pr = 0;
				while (pr + g[tec] <= k){
					pr += g[tec++];
					if (tec == n)
						tec = 0;
				}
				ret += pr;
			}
			cout << ret << endl;
		}
	}
	return 0;
}