#include <cstdio>
#include <vector>
#include <utility>
#include <algorithm>
using namespace std;

enum Stacja {
	ST_A = 0, ST_B = 1
};

static void solve(int _nc) {
	/* wczytaj czasy odjazdów */
	/* zmiany: kiedy, stacja, delta */
	vector<pair<int, pair<Stacja,int> > > przejazdy;
	{
		int T; scanf("%d", &T);
		int nAdoB, nBdoA; scanf("%d%d",&nAdoB,&nBdoA);
		for(int i=0;i<nAdoB;i++) {
			int h1,m1,h2,m2;
			scanf("%d:%d%d:%d",&h1,&m1,&h2,&m2);
			int t1 = 60*h1+m1, t2 = 60*h2+m2 + T;
			przejazdy.push_back(make_pair(t1,make_pair(ST_A,-1)));
			przejazdy.push_back(make_pair(t2,make_pair(ST_B,+1)));
		}
		for(int i=0;i<nBdoA;i++) {
			int h1,m1,h2,m2;
			scanf("%d:%d%d:%d",&h1,&m1,&h2,&m2);
			int t1 = 60*h1+m1, t2 = 60*h2+m2 + T;
			przejazdy.push_back(make_pair(t1,make_pair(ST_B,-1)));
			przejazdy.push_back(make_pair(t2,make_pair(ST_A,+1)));
		}
	}
	/* wartownik */
	przejazdy.push_back(make_pair(24*60*100, make_pair(ST_A, 0)));
	/* sortuj */
	sort(przejazdy.begin(), przejazdy.end());
	/* symuluj pracę */
	int nA, nB; /* ile jest na stacji */
	int dA, dB; /* ile zostało dorzucone */

	nA=nB=dA=dB=0;

	int tS = przejazdy[0].first;
	int deltaA, deltaB = 0;
	for(int i=0;i<(int)przejazdy.size();i++) {
		int tP    = przejazdy[i].first;
		Stacja nS = przejazdy[i].second.first;
		int dS    = przejazdy[i].second.second;
		if(tP!=tS) {
			/* przetwórz */
			nA += deltaA;
			if(nA<0) {
				dA += -nA;
				nA = 0;
			}
			nB += deltaB;
			if(nB<0) {
				dB += -nB;
				nB = 0;
			}
			/* zeruj */
			deltaA = deltaB = 0;
			tS = tP;
		}

		{
			/* agreguj */
			if(nS==ST_A) deltaA += dS;
			else deltaB += dS;
		}
	} /* for */

	printf("Case #%d: %d %d\n", _nc, dA, dB);
}

int main() {
	int N; scanf("%d",&N);
	for(int i=1;i<=N;i++)
		solve(i);
	return 0;
}

