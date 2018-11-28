#include <iostream>
#include <iomanip>
using namespace std;
#include <math.h>
#include <stdio.h>

int main() {
    int T;
    cin >> T;
    for ( int casei = 0; casei < T; casei++ ) {
	int N;
	cin >> N;
	long double pos[3] = {0};
	long double velocity[3] = {0};
	for ( int i = 0; i < N; i++ ) {
	    for ( int j = 0; j < 3; j++ ) {
		int buf;
		cin >> buf;
		pos[j] += (double)buf / N;
	    }
	    for ( int j = 0; j < 3; j++ ) {
		int buf;
		cin >> buf;
		velocity[j] += (double)buf / N;
	    }
	}
	if ( casei == 30 ) {
	for ( int i = 0; i < 3; i++ ) {
	    cout << pos[i] << " " << velocity[i] << endl;
	}
	}
	long double t = 0;
	for ( int i = 0; i < 3; i++ ) {
	    t -= pos[i] * velocity[i];
	}
	long double ssum = 0;
	for ( int i = 0; i < 3; i++ ) {
	    ssum += velocity[i] * velocity[i];
	}

//	cout << t << endl;
	long double newpos[3];
	long double nearest = 0;
	if ( t < 0 || ssum < 0.000001 ) {
	    t = 0;
	    for ( int i = 0; i < 3; i++ ) {
		nearest += pos[i] * pos[i];
	    }
	    nearest = sqrt( nearest );
	} else {
	    	t = t / ssum;
	for ( int i = 0; i < 3; i++ ) {
	    newpos[i] = pos[i] + velocity[i] * t;
	    nearest += newpos[i] * newpos[i];
	}
	nearest = sqrt( nearest );
	}
	cout << "Case #" << casei+1 << ": " << setprecision(15) << nearest << " " << t << endl;
//	printf("%.10e\n", nearest);
    }
    return 0;
}
