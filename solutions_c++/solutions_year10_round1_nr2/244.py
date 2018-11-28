#include <iostream>
#include <cstdlib>
#include <algorithm>
using namespace std;

int main(){
	int f[155][267];
	int fi[267];
	int a[267];
	int test, t;
	int dcost,m,icost,n;
	int minvalue, delta;
	int result;
	bool change;
	
	cin >> t;
	test  = 0;
	while (test < t){
		test ++;
		cout << "Case #" << test << ": ";
		
		cin >> dcost >> icost >> m >> n;
		for (int i =1;i<=n;i++) cin >> a[i];
		
		// qhd
		for (int i = 0;i<=255;i++) f[0][i] = 0;
		for (int i = 1;i<=n;i++){
			// deletes
			for (int j =0;j<=255;j++) f[i][j] = f[i-1][j] + dcost;
			// changes
			for (int j =0;j<=255;j++){
				delta = abs(j-a[i]);
				minvalue = f[i][j] - delta;
				for (int k=max(0,j-m);k<=min(255,j+m);k++){
					if (minvalue > f[i-1][k]){
						minvalue = f[i-1][k];
					}
				}
				f[i][j] = minvalue + delta;
			}
			// insert
			do {
				change = false;
				for (int j = 0;j<=255;j++){
					minvalue = f[i][j];
					for (int k=max(0,j-m);k<=min(255,j+m);k++){
						if (minvalue > f[i][k]){
							minvalue  =  f[i][k];
						}
					}
					fi[j] = minvalue +  icost;
				}
				for (int j =0;j<=255;j++)
					if (f[i][j] > fi[j]){
						change = true;
						f[i][j] = fi[j];
					}
			} while (change);
		}
		// find result
		result  = f[n][0];
		for (int i=0;i<=255;i++)
			if (result > f[n][i]) result  = f[n][i];
		cout << result << endl;
	}
}
