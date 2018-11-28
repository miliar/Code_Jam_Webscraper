#include <iostream>
#include <map>
#include <string>
#include <vector>

using namespace std;

typedef vector<int> vi;
map<int, vi> o;

int main() {
	int nt, it, x1, y1, x2, y2;
	vi v(4);
/*	
	for (x1 = 0; x1 <= 50; x1++) for (y1 = 0; y1 <= 50; y1++) {
		for (x2 = 0; x2 <= 50; x2++) for (y2 = 0; y2 <= 50; y2++) {
			int aa = abs(0 * y1 - x1 * 0 + x1 * y2 - x2 * y1 + x2 * 0 - 0 * y2);
			
			v[0] = x1, v[1] = y1, v[2] = x2, v[3] = y2;
			o[aa] = v;
		}
	}
*/	
	cin >> nt;
	for (it = 1; it <= nt; it++) {
		int n, m, a;
		
		cin >> n >> m >> a;
		
		for (x1 = 0; x1 <= n; x1++) for (y1 = 0; y1 <= m; y1++) {
			for (x2 = 0; x2 <= n; x2++) for (y2 = 0; y2 <= m; y2++) {
				int aa = abs(0 * y1 - x1 * 0 + x1 * y2 - x2 * y1 + x2 * 0 - 0 * y2);
				
				if (aa == a) {a = 0; goto southpark;}
			}
		}
		
southpark:
		cout << "Case #" << it << ": ";
		if (a) {
			cout << "IMPOSSIBLE\n";
		} else {
			cout << "0 0 " << x1 << ' ' << y1 << ' ' << x2 << ' ' << y2 << '\n';
		}
	}
	
	return 0;
}
