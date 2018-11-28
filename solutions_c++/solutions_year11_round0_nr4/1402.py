#define DBGLEVEL 1

#include "std.h"

char buf[1024*1024];

int main() {

    int T;
    cin >> T; cin.getline(buf, sizeof buf);
    FOR(t, T) {
    nextt:
	cout << "Case #"<<(t+1)<<": ";
	int n; cin >> n;
	DBG(1,"CASE " << (t+1)<<V(n));
	cin.getline(buf,sizeof buf);
	int bad = 0;
	int x;
	FOR(i, n) cin >> x, bad += x != i+1;
	cin.getline(buf,sizeof buf);
	cout << bad << endl;
    }
    return 0;
}
