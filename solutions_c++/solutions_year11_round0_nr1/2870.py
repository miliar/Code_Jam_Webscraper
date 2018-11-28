#include <iostream>
using namespace std;

int main () {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int n; cin >> n;
	for (int i = 0; i < n; i ++) {
		int m; cin >> m;
		int orange_but = 1,blue_but = 1,orange_time = 0, blue_time = 0;
		for (int j = 0; j < m; j ++) {
			char a; int but;
			cin >> a >> but;
			if (a == 'O') {
				orange_time += abs(orange_but - but) + 1;
				orange_time = max(orange_time,blue_time + 1);
				orange_but = but;
			}
			else {
				blue_time += abs(blue_but - but) + 1;
				blue_time = max(orange_time + 1,blue_time);
				blue_but = but;
			}
		}
		cout << "Case #" << i + 1 << ": " << max(blue_time,orange_time) << endl;
	}
	return 0;
}