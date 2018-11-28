#include <iostream>
using namespace std;

bool light(int nbSnappers, int snaps) {
	// Il faut que le nombre snaps, sous sa forme binaire, ait tous les bits
	// de 1 à nbSnappers activés

	int mask = 1;
	for(int i=0 ; i<nbSnappers ; i++) {
		if((snaps & mask) == 0)
			return false;
		mask <<= 1;
	}
	return true;
}

int main() {
	int nbTests;
	cin >> nbTests;

	for(int i=1 ; i<=nbTests ; i++) {
		int n, k;
		cin >> n >> k;
		cout << "Case #" << i << ": " << (light(n, k) ? "ON" : "OFF") << endl;
	}
}
