#include <iostream>

using namespace std;

int main() {
	int t;
	cin >> t;
	int pow2[31];
	pow2[0]=1;
	for (int i=1;i<=30;i++) pow2[i]=pow2[i-1]*2;
	for (int i=1;i<=t;i++) {
		int n,k;
		cin >> n >> k;
		
		cout << "Case #" << i << ": " << ((k%pow2[n]==pow2[n]-1)?"ON":"OFF") << endl;
	}
	return 0;
}
