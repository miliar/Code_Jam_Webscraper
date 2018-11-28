#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <deque>
#include <algorithm>
#include <utility>

using namespace std;

typedef unsigned int ui;
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;

int main(){
	int abc; cin >> abc;
	for (int zzz = 1; zzz <= abc; zzz++){
		int n; cin >> n;
		int x[n+2]; int y[n+2]; int r[n+2];
		for (int i = 0; i < n; i++){
			cin >> x[i] >> y[i] >> r[i];
			//cout << x[i] << " " << y[i] << " " << r[i] << endl;
		}
		if (n == 1){
			double ma = (double) r[0];
			printf("Case #%d: %.7f\n", zzz, ma);
		}
		else if (n == 2){
			//cout << r[0] << " " << r[1] << endl;
			double ma = (double) max(r[0],r[1]);
			printf("Case #%d: %.7f\n", zzz, ma);
		}
		else{
			for (int i = 3; i <= 4; i++){
				x[i] = x[i-3]; y[i] = y[i-3]; r[i] = r[i-3];	
			}
			double ma = 1E20;
			for (int i = 0; i < 3; i++){
				double dist = (sqrt((x[i+1]-x[i+2])*(x[i+1]-x[i+2])+(y[i+1]-y[i+2])*(y[i+1]-y[i+2])) + r[i+1]+r[i+2]) / 2.0;
				dist = max(dist,(double) r[i]);
				//cout << "dist = " << dist << endl;
				if (ma > dist) ma = dist;
			}
			printf("Case #%d: %.7f\n", zzz, ma);
		}
	}
	return 0;
}
