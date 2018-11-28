#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

#define ORANGE	0
#define BLUE	1

int main(void)
{
	int t;
	cin >> t;
	for(int i=1;i<=t;i++) {
		int n, r[200], p[200];
		int pos[2] = {1, 1}, t[2] = {0, 0};
		int ans = 0;
		
		cin >> n;
		
		for(int j=0;j<n;j++) {
			string str;
			cin >> str >> p[j];
			r[j] = (str=="B") ? BLUE : ORANGE;
		}
		
		for(int j=0;j<n;j++) {
			int dt = abs(p[j]-pos[r[j]]);
			pos[r[j]] = p[j];
			t[r[j]] = max(t[r[j]] + dt, t[1-r[j]]) + 1;
			//cout << pos[0] << " " << t[0] << " " << pos[1] << " " << t[1] << endl;
		}
		
		ans = max(t[0], t[1]);
		cout << "Case #" << i << ": " << ans << endl;
	}
	return 0;
}
