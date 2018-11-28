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

int b[512][512];

const double eps = 1e-9;

bool checkBlade (int r, int c, int K) {
    double rc = K/2.0, cc = K/2.0;
    double cmx = 0, cmy = 0;
    for (int i = 0; i<K; ++i) {
	for (int j = 0; j<K; ++j) {
	    if (i == 0 and j == 0 or 
		i == 0 and j == K-1 or
		i == K-1 and j == 0 or
		i == K-1 and j == K-1) continue;
	    
	    cmx += ((i+0.5)-rc) * b[r+i][c+j];
	    cmy += ((j+0.5)-cc) * b[r+i][c+j];
/*   
	    if (K == 5 and r == 1 and c == 1) {
		printf("  Point %.2f, %.2f, m=%d, cmx=%.1f, cmy=%.1f\n",
			(i+0.5 - rc),(j+0.5-cc), b[r+i][c+j], cmx, cmy);
	    }
*/
	}
    }
    
//  cout<<"Blade "<<r<<", "<<c<<" K:"<<K<<" cmx="<<cmx<<" cmy="<<cmy<<endl;

    return (fabs(cmx) < eps and fabs(cmy) < eps);
}

int main (void) {
    int T = 0;
    cin >> T;

    for (int c = 1; c<=T; ++c) {
	int R, C, D;
	cin >> R >> C >> D;
	for (int i = 0; i<R; ++i) {
	    for (int j = 0; j<C; ++j) {
		char w;
		cin >> w;
		b[i][j] = D+(w-'0');
	    }
	}
/*
	for (int i = 0 ; i<R; ++i) {
	    for (int j = 0; j<R; ++j) {
		cout<<b[i][j];
	    }
	    cout<<endl;
	}
*/
	int K = (R<C?R:C);
	bool found = false;
	for (; K >= 3 and !found; --K) {
	    for (int i = 0; i+K<=R and !found; ++i) 
		for (int j = 0; j+K<=C and !found; ++j) {
		    if (checkBlade(i,j,K)) {
			found = true;
			break;
		    }
		}
	}
	
	printf("Case #%d: ",c);
	if (found) printf("%d\n",K+1);
	else printf("IMPOSSIBLE\n");
    }

    return 0;
}
