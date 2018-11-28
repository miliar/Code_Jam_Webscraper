// Output should be passed through grep Case to clean debug outputs

#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

#define forall(i,n) for(int i=0; i<(int)(n); i++)

bool Line(const vector<vector<char> >& a, int n, char c, int k) {
    assert(c=='R' || c=='B');
    forall (iDir, 2) {
	forall (i, n) {
	    int line=0;
	    forall (j, n) {
		char cCur;
		cCur = (iDir == 1 ? a[i][j] : a[j][i]);
		if (cCur==c) {
		    line++;
		    if (line == k) {
			// DEBUG!!!
			cout <<
			    "Line at " << i << " " << j << " k=" << k << endl;

			return true;
		    }
		} else
		    line=0;
	    }
	}
    }

    int aLine[n][n];
    forall (iDir, 2) {
	forall (i, n) {
	    forall (j, n) {
		int jPrev = (iDir == 1 ? j - 1 : j + 1);
		int line;
		if (a[i][j] != c)
		    line = 0;
		else if (i == 0 || jPrev < 0 || jPrev >= n)
		    line = 1;
		else
		    line = aLine[i-1][jPrev] + 1;
		if (line == k) {
		    // DEBUG!!!
		    cout << "Line at " << i << " " << j << " k=" << k << endl;
		    return true;
		}
		aLine[i][j] = line;
	    }
	}
    }

    // DEBUG!!!
    forall (i, n) {
	forall (j, n)
	    cout << aLine[i][j];
	cout << endl;
    }
    cout << endl;

    return false;
}

const char* Ans(const vector<string>& vs, int n, int k) {
    char a[n][n];
    forall (i, n)
	forall (j, n)
	    a[i][j] = vs[n-1-j][i];

    // DEBUG!!!
    forall (i, n) {
	forall (j, n)
	    cout << a[i][j];
	cout << endl;
    }
    cout << endl;

    forall (j, n) {
	int dst = n;
	for (int src=n-1; src>=0; src--) {
	    if (a[src][j] != '.')
		a[--dst][j] = a[src][j];
	}
	forall (i, dst)
	    a[i][j] = '.';
    }

    // DEBUG!!!
    forall (i, n) {
	forall (j, n)
	    cout << a[i][j];
	cout << endl;
    }
    cout << endl;

    vector<vector<char> > vv(n);
    forall (i, n) {
	vv[i].resize(n);
	forall (j, n)
	    vv[i][j] = a[i][j];
    }
    bool bRed = Line(vv, n, 'R', k);
    bool bBlue = Line(vv, n, 'B', k);
    if (bRed && bBlue)
	return "Both";
    if (bRed && !bBlue)
	return "Red";
    if (!bRed && bBlue)
	return "Blue";
    if (!bRed && !bBlue)
	return "Neither";
    return "Impossible";
	
    /*
    // DEBUG
    forall (i, n) {
	forall (j, n)
	    cout << a[i][j];
	cout << endl;
    }
    */
}


int main() {
    int nTests;
    cin >> nTests;
    forall (iTest, nTests) {
	int n, k;
	cin >> n >> k;
	vector<string> vs(n);
	forall (i, n)
	    cin >> vs[i];
	const char* sAns = Ans(vs, n, k);
	cout << "Case #" << iTest+1 <<": " << sAns << endl;
    }
}
