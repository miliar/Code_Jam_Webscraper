#include <iostream>
#include <fstream>
#include <string>
#include <queue>
using namespace std;

ifstream fin("B.in");
ofstream fout("B.out");

#define cin fin
#define cout fout
#define int64 long long

int l, n, c;
int64 t, sum, a[1000010];
int64 prev[1000010];
int64 ben[1000010];

int main(){
	int T, test = 0;
	for(cin >> T; T--; ){
		sum = 0;
		cin >> l >> t >> n >> c;
		int64 x;
		for(int i = 0; i < c; i++){
			cin >> x;
			for(int j = i; j < n; j += c){
				a[j] = 2 * x;
				sum += a[j];
			}
		}
		prev[0] = 0;
		for(int i = 1; i < n; i++)
			prev[i] = prev[i - 1] + a[i - 1];
		for(int i = 0; i < n; i++){
			int64 tmp = max(0LL, t - prev[i]);
			ben[i] = max(0LL, (a[i] - tmp) / 2);
		}
		sort(ben, ben + n);
		reverse(ben, ben + n);
		int64 res = sum;
		for(int i = 0; i < l; i++)
			res -= ben[i];
		cout << "Case #" << ++test << ": " << res << endl;
	}
	return 0;
}
