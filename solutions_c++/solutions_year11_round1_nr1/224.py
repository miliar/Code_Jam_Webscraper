#define DBGLEVEL 1

#include "std.h"

char buf[1024*1024];

int main() {
    int T;
    cin >> T; cin.getline(buf, sizeof buf);
    FOR(t, T) {
    nextt:
	int broken = 0;
	LL n, pd, pg; cin >> n >> pd >> pg;
	cin.getline(buf,sizeof buf);

	cout << "Case #"<<(t+1)<<": ";

	if (pd < 100 && pg == 100) { cout << "Broken"; goto end; }
	if (pd > 0 && pg == 0)  { cout << "Broken"; goto end; }

	if (n >= 100) {
	    cout << "Possible"; goto end;
	}

	for (int d = 1; d <= n; d++) {
	    int d2 = d * pd / 100;
	    if (d2 * 100 != pd * d) goto bad;
	    cout << "Possible";
	    goto end;

	bad: continue;
	}
	cout << "Broken";
    end:
	cout<<endl;
    }
    return 0;
}
