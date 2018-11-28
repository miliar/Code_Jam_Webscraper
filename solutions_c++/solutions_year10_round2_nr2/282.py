#include<iostream>

#define Inf 2147483647

using namespace std;
		
int n, m, t, d;
int p[16];
int v[16];

int main(){
	int csn;

	cin >> csn;

	for(int cs = 1; cs <= csn; ++cs){
		int i;
		int count = 0;
		int k = 0;
		
		cin >> n >> m >> d >> t;

		for(i = 0; i < n; ++i) cin >> p[i];
		for(i = 0; i < n; ++i) cin >> v[i];



		for(i = n-1; i >= 0; --i){
			if(d - p[i] <= t * v[i]){
				count ++;
				k += n - i - count;
				if(count == m) break;
			}
		}

		cout << "Case #" << cs << ": ";
		if(m == 0) cout << 0 << endl;
		else if(i >= 0) cout << k << endl;
		else cout << "IMPOSSIBLE" << endl;
	}

	return 0;
}
