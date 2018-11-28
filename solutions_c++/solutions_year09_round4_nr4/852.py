#include <iostream>
#include <cmath>
using namespace std;


int main(){
	//freopen("ip.in", "r", stdin);
	//freopen("op.out", "w", stdout);
	
	int cas, n;
	scanf("%d", &cas);
	for(int cs = 1; cs <= cas; ++cs){
		scanf("%d", &n);
		int x[3], y[3], r[3];
		double R[3];
		for(int i = 0; i < n; ++i){
			scanf("%d%d%d", &x[i], &y[i], &r[i]);
		}
		if(n == 1){
			printf("Case #%d: %.6f\n", cs, (double)r[0]);
			continue;
		}
		for(int i = 0; i < n; ++i){
			int j = (i + 1) % n;
			int dd = (x[i] - x[j]) * (x[i] - x[j]) + (y[i] - y[j]) * (y[i] - y[j]);
			R[i] = (sqrt((double)dd) + r[i] + r[j]) / 2;
			//if(sqrt((double)dd) < r[i] + r[j]) cout << "error" << endl;
		}
		if(n == 2){
			printf("Case #%d: %.6f\n", cs, (double)max(r[0], r[1]));
			continue;
		}
		double res = 10000000;
		for(int i = 0; i < n; ++i){//n == 3
			res = min(res, max(R[i], (double)r[(i + 2) % 3]));
		}
		printf("Case #%d: %.6f\n", cs, res);
	}
	return 0;
}