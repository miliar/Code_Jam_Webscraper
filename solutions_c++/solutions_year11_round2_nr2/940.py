#include <iostream>
#include <fstream>
#include <cstring>
using namespace std;

int tmp[201],num[201],pos[201];
int n, d;

bool check(double x) {
	memcpy(tmp, num, sizeof(num));
	double last = pos[0] - x;
	tmp[0]--;
	for (int i = 0; i < n; i++){
		while(tmp[i] > 0){
		if (pos[i] + x - last < d)
			return false;
		else{
			last = pos[i] - x -last >= d ?  pos[i] - x : last + d; 
	        tmp[i]--;
			}
		}
	}
	return true;
}

int main() {
	freopen("GCJ P B.in", "r", stdin);
	freopen("GCJ P B.out", "w", stdout);
	int tt;
	cin >> tt;
	for (int t = 0; t < tt; t++){
		cout << "Case #" << t+1 << ": " ;
		cin >>n >>d;
		for (int i = 0; i < n; i++){
			cin >> pos[i] >> num[i];
		}
		double st = 0, ed = 100000000;
		while (ed - st > 1e-8){
			double mid = (st + ed) / 2.0;
			if (!check(mid))
				st = mid;
			else ed = mid;
		}
		cout << st << endl;
	} 
 	return 0;
 } 
 