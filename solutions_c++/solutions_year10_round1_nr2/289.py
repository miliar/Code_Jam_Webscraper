#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <climits>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

#define forall(i,n) for(int i=0; i<(int)(n); i++)

typedef unsigned char uc;
typedef vector<uc> UCharList;
typedef vector<int> IntList;


#define REPLACE(pix1, pix2) (min(D+I, abs((pix1)-(pix2))))
#define MIN(x,y) ((x)<(y)?(x):(y))

int Ans(const IntList& v, int D, int I, int M, int N) {
    if (N <= 1)
	return 0;

    int vScores[N+1][256];
    forall (p, 256)
	vScores[0][p] = I;
    for (int n=1; n<=N; n++) {
	forall (p, 256) {
	    // cost for replace the last one by p
	    int initScore = MIN(D+I, abs(v[n-1]-p));

	    int score1 = vScores[n-1][p]+D; // delete the last one?
	    int score2 = (n-1)*D + initScore; // delete all but the last one?
	    int minScore = MIN(score1, score2);

	    // edit previous pixels, replace the last one
	    forall (pPrev, 256) {
		int delta = abs(p - pPrev);
		int score = initScore + vScores[n-1][pPrev];
		if (M == 0 && delta > 0)
		    continue;
		// add the path
		if (delta > M)
		    score += I * ((delta - 1) / M);
		// improved?
		if (score < minScore)
		    minScore = score;
	    }

	    vScores[n][p] = minScore;
	}
    }

    int minScore = vScores[N][0];
    forall (p, 256)
	if (vScores[N][p] < minScore)
	    minScore = vScores[N][p];
    return minScore;
}


int main() {
    int nTests;
    cin >> nTests;
    forall (iTest, nTests) {
	int D, I, M, N;
	cin >> D >> I >> M >> N;
	IntList v(N);
	forall (i, N) {
	    cin >> v[i];
	}
	int ans = Ans(v, D, I, M, N);
	cout << "Case #" << iTest+1 <<": " << ans << endl;
    }
}
