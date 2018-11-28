#include <iostream>
using namespace std;

int main(int argc, char **args)
{
	int cases;
	unsigned int n, k;
	cin >> cases;
	for(int j=0; j < cases; j++) {
		//Number of snappers
		//K number of 'snaps'
		cin >> n >> k;
		bool isGood=true;
		for(int i=0; i < n; i++) {
			if((k & 1) == 0) {
				isGood = false;
				i = n;
			} else k >>= 1;
		}
		cout << "Case #" << j+1 << ": " << (isGood ? "ON" : "OFF") << endl;
	}
	return 0;
}
