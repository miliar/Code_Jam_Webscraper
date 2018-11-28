#define DBGLEVEL 0

#include "std.h"

char buf[1024*1024];


int mat[400][400];

int d0[400], d1[400];

int nw[400];

int com[400][400];

// max # planets threatened for path going through p1 and p2.
int dp[400][400];


// max# threatened planets 
int go(int p) {


}

int main() {
    int T;
    cin >> T; cin.getline(buf, sizeof buf);
    FOR(tt, T) {
	DBG(1, V(tt));
	ZERO(mat);
	ZERO(nw);
    nextt:
	int P, W;
	cin >> P >> W;
	cin.getline(buf, sizeof buf);

	FOR(w, W) {
	    int p1, p2; char c;
	    cin >> p1 >> c >> p2;
	    mat[p1][p2] = mat[p2][p1] = 1, nw[p1]++, nw[p2]++;
	}
	ZERO(com);
	FOR(p1, P) FOR(p2, p1) if (mat[p1][p2]) FOR(p3, P) if (mat[p1][p3] && mat[p2][p3]) com[p1][p2]++;
	cin.getline(buf, sizeof buf);
	memset(d0, 0x7F, sizeof(d0));
	memset(d1, 0x7F, sizeof(d1));
	FOR(h, 2) {
	    int* d = h ? d1 : d0;
	    d[h] = 0;
	    queue<int> q;
	    q.push(h);
	    while (!q.empty()) {
		int p = q.front(); q.pop();
		FOR(pp, P) if (mat[p][pp]) if (d[pp] > d[p] + 1) d[pp] = d[p] + 1, q.push(pp);
	    }
	}
	//DBG(1, V(d0[1])<<V(d1[0]));
	int r1 = d0[1] - 1;
	int r2 = nw[0];
	if (d0[1] == 1) goto done;
	ZERO(dp);
	FOR(p, P) if (d0[p] == 1) {
	    int r = nw[0] - 1;
	    FOR(p4, P) if (p4 && mat[p][p4] && !mat[0][p4]) r++;
	    dp[0][p] = r;
	    DBG(1, V(p)<<V(dp[0][p]));
	    r2 >?= r;
	}

	for(int d = 2; d < d0[1]; d++) {
	    FOR(p, P) if (d0[p] == d && d0[p] + d1[p] == d0[1]) {
		FOR(pp, P) if (d0[pp] == d-1 && mat[p][pp]) {
		    FOR(ppp, P) if (d0[ppp] == d-2 && mat[ppp][pp]) {
			int r = dp[ppp][pp] - 1;
			FOR(p4, P) if (mat[p][p4] && !mat[pp][p4] && !mat[ppp][p4]) r++;
			dp[pp][p] >?= r;
			r2 >?= r;
		    }
		    DBG(1, V(pp)<<V(p)<<V(dp[pp][p]));	    
		}
	    }
	}

    done:
	int ret = 0;
	cout << "Case #"<<(tt+1)<<": ";
	cout << r1 << ' ' << r2;
    end:
	cout<<endl;
    }
    return 0;
}
