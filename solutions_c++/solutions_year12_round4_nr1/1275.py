#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <cmath>
using namespace std;

int T, N, D; 
int vines_ori[60010];
int vines_length[60010];
double min_height[60010];
bool can[60010];

double get_height(int x, int c, int r) {
	return sqrt(r*r - (x-c)*(x-c)) + c;
}

int main() {
	cin >> T;
	
	for(int caseNo=1;caseNo<=T;caseNo++) {
		cin >> N;
		for(int i=0;i<N;i++) {
			cin >> vines_ori[i] >> vines_length[i];
		}
		cin >> D;
		
		for(int i=0;i<N;i++){
			min_height[i] = 2147483647;
			can[i] = false;
		}
		
		double d = D - vines_ori[N-1];
		if (d <= vines_length[N-1]) {
			min_height[N-1] = d;
			can[N-1] = true;
		}
		
		for(int i=N-2;i>=0;i--) {
			// use vine i to reach vine j in min height
			for(int j=i+1;j<N;j++) {
				if (can[j]) { // j can reach end state
					// j can only useful if i can reach j larger than the min height
					if (vines_ori[j] - vines_ori[i] >= min_height[j]) {
						d = vines_ori[j] - vines_ori[i];
						if (d <= vines_length[i]) {
							min_height[i] = min(min_height[i], d);
							can[i] = true;
						}
					}
				}
			}
			// try if this vine can reach end state directly
			d = D - vines_ori[i];
			if (d <= vines_length[i]) {
				can[i] = true;
				min_height[i] = min(min_height[i], d);
			}
		}
		
		//for(int i=0; i< N;i++) {
		//	cout << min_height[i] << " " << can[i] << endl;
		//}
		
		cout << "Case #" << caseNo << ": " ;
		if(vines_ori[0] >= min_height[0]) {
			cout << "YES";
		} else cout << "NO";
		cout << endl;
	}
	return 0;
}
