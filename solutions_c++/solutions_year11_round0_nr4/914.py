#include <iostream>

using namespace std;

int main (int argc, char const *argv[])
{
	int t;
	cin >> t;
	for(int ii = 1; ii <=t; ii++) {
		int n;
		int data[1000];
		cin >> n;
		int ans = 0;
		for(int i = 0; i < n; i++) {
			cin >> data[i];
			if (data[i] != i+1) ans++;
		}
		
		cout << "Case #" << ii << ": " << ans << endl;
	}
	return 0;
}