#include <cstdio>
#include <cstdlib>
#include <iostream>

using namespace std;

#define forall(i,n) for(int i=0; i<(int)(n); i++)

main() {
    int nTests;
    cin >> nTests;
    forall (i, nTests) {
	int n, k;
	cin >> n >> k;
	int period = 1 << n;
	int kMin = period - 1;
	bool bOn = (k % period == kMin);
	cout << "Case #" << i+1 <<": " << (bOn ? "ON" : "OFF") << endl;
    }
}
