#include <iostream>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <iomanip>

using namespace std;

double p[100010];

int main(){
	int a, b, t;
	
	cin >> t;
	for(int tc = 1; tc <= t; tc++){
		cin >> a >> b;
		
		p[0] = 1.0;
		for(int i = 1; i <= a; i++){ cin >> p[i];  p[i] *= p[i-1]; }
		
		double ans = b+2;
		
		for(int k = 0; k <= a; k++){
			int watype = 2*k + 2*b - a + 2;
			int actype = 2*k + b - a + 1;
			ans = min(ans, watype*(1 - p[a-k]) + actype*p[a-k]);
		}
		
		cout << "Case #" << tc << ": ";
		cout << fixed << setprecision(6) << ans << "\n";
	}	
	return 0;
}
