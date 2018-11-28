#include<iostream>

using namespace std;

int main() {
	int t;
	cin >> t;
	for(int i=0;i<t;i++) {
		int n, s, p, sum = 0;
		cin >> n >> s >> p;
		for(int j=0;j<n;j++) {
			int notes;
			cin >> notes;
			if(p == 0) {
				sum ++;
				continue;
			}
			if(notes == 0) continue;
			notes+=2;
			if(notes / p >= 3) {
				sum++;
			} else if((notes + 2) / p >= 3 && s > 0) {
				s--;
				sum++;
			}		
		}
		cout << "Case #" << i+1 << ": " << sum << "\n";
	}
	return 0;
}
