#define DBGLEVEL 1

#include "std.h"

char buf[1024*1024];

int main() {
    int T;
    cin >> T; cin.getline(buf, sizeof buf);
    FOR(t, T) {
    nextt:
	int n; cin >> n;
	//	DBG(1,"CASE " << (t+1)<<V(n));
	char col;
	int c[100];
	int b[100];
	FOR(i, n) cin >> col >> b[i], c[i] = col == 'B';
	cin.getline(buf,sizeof buf);
	int pos[2] = {1, 1};
	int dest[2];
	FOR(o, 2) FOR(i, n) if (c[i] == o) { dest[o] = b[i]; break; }
	int curi = 0;
	int tm = 0;
	while (curi < n) {
	    int done = 0;
	    FOR(o, 2) {
		if (pos[o] < dest[o]) pos[o]++;
		else if (pos[o] > dest[o]) pos[o]--;
		else if (c[curi] == o) {
		    for(int j = curi+1; j<n; j++) if (c[j] == o) { dest[o] = b[j]; break; }
		    done = 1;
		}
	    }
	    tm++;
	    if (done) curi++;
	}
	cout << "Case #"<<(t+1)<<": ";
	cout << tm << endl;
    }
    return 0;
}
