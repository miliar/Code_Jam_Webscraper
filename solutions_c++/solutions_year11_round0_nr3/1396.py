#define DBGLEVEL 1

#include "std.h"

char buf[1024*1024];

int main() {
    int T;
    cin >> T; cin.getline(buf, sizeof buf);
    FOR(t, T) {
    nextt:
	int n; cin >> n;
	DBG(2, "CASE " << (t+1)<<V(n));
	cin.getline(buf,sizeof buf);
	int smallest = 9999999;
	int bsum = 0, sum = 0;
	int x;
	FOR(i, n) cin >> x, smallest <?= x, bsum ^= x, sum += x;
	cin.getline(buf,sizeof buf);
	cout << "Case #"<<(t+1)<<": ";
	if (bsum) cout << "NO"<<endl;
	else cout << sum - smallest << endl;
    }
    return 0;
}
