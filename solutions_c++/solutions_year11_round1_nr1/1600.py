#include <iostream>
#include <iomanip> 
#include <string> 
#include <algorithm> 
#include <vector> 
#include <set> 
#include <map> 
#include <math.h> 
#include <cstdlib>
#include <queue>

using namespace std;

int main(void) {
	freopen("/Users/admin/Desktop/[Contests]/informatics/Cpl/be/a.in","r",stdin);
	freopen("/Users/admin/Desktop/[Contests]/informatics/Cpl/be/a.out","w",stdout);
	int t;
	cin >> t;
	for (int i = 0; i < t; i++) {
		int n, d, g;
		bool flap = false;
		cin >> n >> d >> g;
		
		if ((g == 100 && d != 100) || (g == 0 && d != 0)) {
			cout << "Case #" << i+1 << ": Broken"<<endl;
		} else {
			if (n >= 100) {
				cout << "Case #" << i+1 << ": Possible"<<endl;
				flap = true;
			} else {
				for (int j = 1; j <= n; j++) {
					if ((100 % j == 0) && (d %(100 / j)== 0) && (d/(100/j) <=j) ) {
						cout << "Case #" << i+1 << ": Possible"<<endl;
						flap = true;
						break;
					}
				}
			}
			if (! flap) {
				cout << "Case #" << i+1 << ": Broken"<<endl;
			}
		}
	}
		
		
	return 0;
}