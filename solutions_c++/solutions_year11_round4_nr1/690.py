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
	
int b[1024], e[1024], w[1024];
int wi[1024];

bool wcmp(int i, int j) {return (w[i] < w[j]);}

int main (void) {
    int T = 0;
    cin >> T;

    for (int c = 1; c<=T; ++c) {
	int X, S, R, N; ld t;
	cin >> X >> S >> R >> t >> N;
	for (int i = 0; i<N; ++i) {
	    cin >> b[i] >> e[i] >> w[i];
	}

	int noWalk = b[0] + X-e[N-1];
	for (int i = 1; i<N; ++i) 
	    noWalk += b[i] - e[i-1];
	
	ld time = 0;
	//Always run when there is no walkway
	if (R * t > noWalk) {
	    time += (ld)noWalk/R;
	    t -= (ld)noWalk/R;
	} else {
	    //t running
	    time += t;
	    noWalk -= R*t;
	    // rest walking
	    time += (ld)noWalk/S;
	    t = 0;
	}

	for (int i = 0; i<N; ++i) wi[i] = i;

	sort (wi, wi+N, wcmp);

	
	for (int i = 0; i<N; ++i) {
	    ld d = e[wi[i]] - b[wi[i]];
	    if ((R+w[wi[i]])*t > d) {
		time += d/(R+w[wi[i]]);
		t -= d/(R+w[wi[i]]);
	    } else {
		//t running;
		time += t;
		d -= (R+w[wi[i]])*t;
		//rest walking
		time += d/(S+w[wi[i]]);
		t = 0;
	    }
	}

	printf("Case #%d: %.9Lf\n",c,time);
    }

    return 0;
}
