#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <functional>

#define all(v) (v).begin(), (v).end()

using namespace std;

typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> pii;
typedef map<string,int> msi;

int main (void) {
    int T = 0;
    cin >> T;

    for (int c = 1; c<=T; ++c) {
	int N;
	cin >> N;
	char games[101][101];
	for (int i = 0; i<N; ++i)
	    for (int j = 0; j<N; ++j)
		cin >> games[i][j];
	double wp[101];
	for (int i = 0; i<N; ++i) {
	    int gp = 0, gw = 0;
	    for (int j = 0; j<N; ++j) {
		if (games[i][j] == '.') continue;
		if (games[i][j] == '1') gw++;
		gp++;
	    }
	    wp[i] = (double)gw/gp;
	}
	double owp[101];
	for (int i = 0; i<N; ++i) {
	    int op = 0;
	    double wps = 0;
	    for (int j = 0; j<N; ++j) {
		if (games[i][j] == '.') continue;
		int gp = 0, gw = 0;
		for (int k = 0; k<N; ++k) {
		    if (k == i or games[j][k] == '.') continue;
		    if (games[j][k] == '1') gw++;
		    gp++;
		}
		wps += (double)gw/gp;
		op++;
	    }
	    owp[i] = wps/op;
	}
	printf("Case #%d:\n",c);
	
	for (int i = 0; i<N; ++i) {
	    double oowp = 0.0;
	    int op = 0;
	    for (int j = 0; j<N; ++j) {
		if (games[i][j] == '.') continue;
		oowp += owp[j];
		op++;
	    }
	    oowp /= op;
	    double RPI = 0.25 * wp[i] + 0.5*owp[i] + 0.25*oowp;
	    printf("%0.12f\n",RPI);
	}
    }

    return 0;
}
