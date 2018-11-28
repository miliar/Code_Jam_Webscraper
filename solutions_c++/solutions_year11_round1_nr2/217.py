#define DBGLEVEL 0

#include "std.h"

char buf[1024*1024];

int cnt[1<<26];

#define MAXN 10000
#define MAXM 100
#define Z 26

short bits[MAXN][Z];
int len[MAXN];
int contains[MAXN];

VI cand;

int main() {
    int T;
    cin >> T; cin.getline(buf, sizeof buf);
    FOR(t, T) {
    nextt:
	int N, M; cin >> N >> M;
	cin.getline(buf,sizeof buf);
	VS words(N);
	VS lists(M);

	int call = 0;
	FOR(i, N) {
	    string w;
	    cin >> w;
	    words[i] = w;
	    cin.getline(buf,sizeof buf);
	    len[i] = w.size();
	    for(char c = 'a'; c <= 'z'; c++) {
		int b = 0;
		FOR(k, w.size()) if (w[k] == c) b |= 1<<k;
		bits[i][c-'a'] = b;
	    }
	    int bc = 0;
	    FOR(k, w.size()) bc |= 1 << (w[k]-'a');
	    contains[i] = bc;
	    call |= bc;
	}

	string sol;

	FOR(m, M) {
	    string order;
	    cin >> order;
	    cin.getline(buf,sizeof buf);
	    
	    string bestw;
	    int bestpts = -1;

	    DBG(1, V(order));

	    FOR(wi, N) {
		int pc = call;
		string w = words[wi];
		int pts = 0;

		DBG(1, V(w));

		VI cand;
		FOR(k, N) if (len[k] == w.size()) cand.pb(k);

		if (cand.size() == 1) {
		    if (bestpts < 0) bestpts = 0, bestw = w;
		    continue;
		}
		assert(cand.size());

		FOR(k, 26) {
		    char c = order[k] - 'a';
		    if ((pc & (1<<c)) == 0) continue;
		    DBG(1, V(k)<< V(order[k]) << V(cand));
		    if (!bits[wi][c]) pts++;
		    int bw = bits[wi][c];
		    VI cand2;
		    int npc = 0;
		    FOR(t, cand.size()) {
			DBG(1, V(char('a'+c)) << hex << V(bw) << dec<<V(cand[t]) << hex<<V(bits[cand[t]][c])<<dec);
			if (bits[cand[t]][c] == bw) cand2.pb(cand[t]), npc |= contains[cand[t]];
		    }
		    assert(cand2.size());
		    cand.swap(cand2);
		    if (cand.size() == 1) break;
		    pc = npc;
		}
		assert(cand.size() == 1);
		if (pts > bestpts) bestpts = pts, bestw = w;

		DBG(1, V(w)<<V(pts));

	    }

	    DBG(1, V(bestw)<<V(bestpts));
	    if (m) sol += ' ';
	    sol += bestw;
	}


	cout << "Case #"<<(t+1)<<": " << sol;
    end:
	cout<<endl;
    }
    return 0;
}
