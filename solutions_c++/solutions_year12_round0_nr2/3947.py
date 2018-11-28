#include <iostream>
#include <algorithm>
using namespace std; 

int bestscore(int x, bool sur) {
	if (x == 0) return 0; 
	if (x == 1) return 1; 
	if (!sur){ // khong bat ngo 
		if (x % 3 == 0) return x / 3;
		else return x / 3 + 1; 
	}
	else { // bat ngo
		if (x % 3 == 2) return x / 3 + 2; 
		else return x / 3 + 1; 
	}
}
int main(){
	freopen("B-large.in","r",stdin); 
	freopen("B-large.out","w",stdout); 
	
	int T, total[200], S, P, N, ans; 
	cin >> T; 

	for(int testid = 1; testid <= T; ++testid) {
		cin >> N >> S >> P; 
		ans = 0; 
		for(int i = 0; i < N; ++i) { cin >> total[i]; }
		sort(total,total+N);
		int numsur = 0;
		bool usedsur = false; 
		for(int i = N-1; i >= 0; --i ){
			if (!usedsur) {
				if (bestscore(total[i],usedsur) >= P) {
					ans ++; 
				}
				else {
					usedsur = true; 
					if (bestscore(total[i],usedsur) >= P && numsur < S) {
						ans ++; 
						numsur ++; 
					}
				}
			}
			else {
					if (bestscore(total[i],usedsur) >= P && numsur < S) {
						ans ++; 
						numsur ++; 
					}
			}
		}
		cout << "Case #" << testid << ": " << ans << endl; 
	}
	return 0; 
}