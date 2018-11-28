#include <iostream>
#include <vector>

using namespace std;
/*
int gcd (int a, int b) {
	int max, min;
	
	if (a>b) { max=a; min=b; }
	else { max=b; min=a; }
	
	if (min == 0) return a;
	else if return gcd(min, max%min);
}
*/
int main() {
	
	int T, N, L, H;
	
	cin >> T;
	
	for (int i=0; i<T; i++) {
		cin >> N >> L >> H;
		
		int oth[N];
		
		for (int j=0; j<N; j++) {
			cin >> oth[j];
		}
		
		/*
		int c = gcd(oth[0], oth[1]);
		for (j=2; j<N; j++) {
			c = gcd(c,oth[j]);
		}
		
		*/
		
		cout << "Case #" << (i+1) << ": ";
		bool isNotFound = true;
		for (int j=L; j<=H; j++) {
			
			bool isFound = true;
			for (int k=0; k<N; k++) {
				if (j>=oth[k] && (j % oth[k]) == 0) continue;
				else if (j<oth[k] && (oth[k] % j) == 0) continue;
				else {
					isFound = false;
					break;
				}
			}
			
			if (isFound) {
				cout << j << "\n";
				isNotFound = false;
				break;
			}
		}
		
		if (isNotFound) cout << "NO\n";
	}
}
