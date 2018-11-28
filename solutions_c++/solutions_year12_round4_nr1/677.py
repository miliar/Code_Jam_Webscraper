#include <iostream>
#include <map>

using namespace std;

bool swing(map<long, long>::iterator current, long h, map<long, long> &vines, long ld) {
	if (current->first + h >= ld) return true;
	
	map<long, long>::iterator next = current; next++;

    bool found = false;
	while (next != vines.end()) {
		if (current->first + h >= next->first) found = swing(next, min(next->first - current->first, next->second), vines, ld);
		if (found) return true;
		next++;
	}

	return false;
}

void solve(int tc) {
	map<long, long> vines;
  
    int nv; cin >> nv;
    for (int v = 0; v < nv; v++) {
		long d, l;
		cin >> d >> l;
		vines[d] = l;
    }  

    long ld; cin >> ld;

	cout << "Case #" << tc << ": " << (swing(vines.begin(), vines.begin()->first, vines, ld)?"YES":"NO") << endl;
}

int main() {
    int ntc; cin >> ntc;
    for (int tc = 0; tc < ntc; tc++) solve(tc);
	return 0;
}
