#include<iostream>
#include<string>
#include<vector>
using namespace std;


int main() {
	int t;
	int n, s, p;
	int ans, line1,line2;
	cin >> t;
	for (int count=0; count<t; count++) {
		
		cin >> n >> s >> p;
		ans = 0;
		line1 = 3*p-2;
		line2 = 3*p-4;
		if (p==1) line2=1;
		int temp;
		for (int i=0; i<n; i++) {
			cin >> temp;
			if (temp>=line1) ans++;
			else if (temp>=line2 && s>0) {
				ans++;
				s--;
			}
		}
		cout << "Case #" << count+1 << ": " << ans << endl;
	}
	return 0;
}
