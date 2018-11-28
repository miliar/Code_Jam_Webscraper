#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cmath>
#include <string>

using namespace std;

void dostep(int t) {
	int n;
	cin >> n;
	string robot;
	int last_moved[2] = {0, 0};
	int last_pos[2] = {1, 1};
	int pos;
	for (int i=0;i<n;i++) {
		cin >> robot >> pos;
		int r = (robot[0] == 'O') ? 0 : 1;
		int needed = abs(pos - last_pos[r]) + 1;
		last_moved[r] = max(last_moved[r] + needed, last_moved[r^1] + 1);
		last_pos[r] = pos;
	}
	cout << "Case #" << t << ": " << max(last_moved[0], last_moved[1]) << endl;
}

int main() {
        int n;
        cin>>n;
        for (int i=1;i<=n;i++)dostep(i);
        return 0;
}
