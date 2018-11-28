#define DBGLEVEL 1

#include "std.h"

char buf[1024*1024];


int main() {
    int T;
    cin >> T; cin.getline(buf, sizeof buf);
    FOR(tt, T) {
    nextt:
	int X, S, R, t, N;
	cin >> X >> S >> R >> t >> N;
	cin.getline(buf, sizeof buf);

	map<int, int> sd; // runway speed -> distance
	int sumd = 0;

	FOR(i, N) {
	    int b, e, w;
	    cin >> b >> e >> w;
	    cin.getline(buf, sizeof buf);

	    sd[w] += e - b;
	    sumd += e - b;
	}

	sd[0] += X - sumd;

	double tott = 0;
	double runt = t;

	FOREACH (it, sd) {
	    double sw = it->first + S, d = it->second;
	    double sr = it->first + R;

	    double tr = (d / sr) <? runt;
	    runt -= tr;
	    tott += tr;
	    d -= tr * sr;

	    double tw = d / sw;
	    tott += tw;
	}

	cout << "Case #"<<(tt+1)<<": " << setprecision(10)<<tott;
    end:
	cout<<endl;
    }
    return 0;
}
