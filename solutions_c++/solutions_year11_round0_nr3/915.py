#include <iostream>

using namespace std;

int main (int argc, char const *argv[])
{
	int t;
	cin >> t;
	for(int index = 1; index <= t; index++) {
		int n;
		int min = 10000000;
		int current = 0;
		int total = 0;
		int temp;
		cin >> n;
		for(int i = 0; i < n; i++) {
			cin >> temp;
			current = current ^ temp;
			total += temp;
			min = min<temp?min:temp;
		}
		if (current == 0) {
			cout << "Case #"<<index<<": " << total-min << endl;
		} else {
			cout << "Case #"<<index<<": NO" << endl;
		}
	}
	return 0;
}