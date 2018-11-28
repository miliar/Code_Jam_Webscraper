#include <iostream>
#include <fstream>
#include <string>
using namespace std;

/*
n%3 = 0
	n/3, n/3, n/3 //NOT
	n/3 -1, n/3, n/3 +1 //IS MAX N/3 +1
n%3 = 1
	n/3, n/3, n/3 +1 //NOT MAX N/3 +1
	n/3 -1, n/3 + 1, n/3 +1 //IS MAX N/3 +1
n%3 = 2
	n/3, n/3, n/3 + 2 //IS MAX N/3 + 2
	n/3 + 1, n/3 + 1, n/3 //NOT
*/

int main() {
	freopen("input.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int K;
	cin >> K;
	int t, s, p;
	for (int data = 1; data <= K; data++) {
		int total = 0;
		cin >> t >> s >> p;
		for (int i = 0; i < t; i++) {
			int n;
			cin >> n;
			switch (n%3) {
				case 0:	if ((n/3) >= p)
							total++;
						else if ((n/3) + 1 >= p && s > 0 && n != 0) {
							total++;
							s--;
						}
						break;
				case 1:	if ((n/3)+1 >= p)
							total++;
						break;
				case 2:	if ((n/3)+1 >= p)
							total++;
						else if((n/3)+2 >= p && s > 0) {
							total++;
							s--;
						}
						break;
			}
			
		}
		cout << "Case #" << data << ": " << total << endl;
	}
}
