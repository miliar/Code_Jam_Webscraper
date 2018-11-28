#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <set>
#include <map>
using namespace std;

int main() {
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int x,y,t,n;
	cin >> t;
	char s;
	for (int i=0;i<t;i++) {
		int o_pos = 1, b_pos = 1, o_t = 0, b_t=0,t_t = 0;
		cin >> n;
		for (int j=0;j<n;j++) {
			cin >> s >> x;

			if (s=='B') {
				y = abs(b_pos - x)+1 + b_t;

			} else {
				y = abs(o_pos - x)+1 + o_t;
			}

			if (t_t < y) t_t = y; else ++t_t;

			if (s=='B') {
				b_pos = x;
				b_t = t_t;
			} else {
				o_pos = x;
				o_t = t_t;
			}

		}
		cout << "Case #" << i+1 << ": " << t_t << endl;
	}
}
