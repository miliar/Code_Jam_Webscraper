#include<iostream>
#include<stdio.h>
using namespace std;

int p[201];
int np[201];
int n;

int main() {
	int T, D, C, c=1, i, j, pp, npp;
	cin >> T;
	while(T--) {
		cin >> C >> D;
		n=1;
		np[0] = 0;
		double maxdist=0;
		while(C--) {
			cin >> p[n] >> np[n];
			np[n] += np[n-1];
			n++;
		}


		for(i=1; i<n; i++) {
			for(j=i; j<n; j++) {
				double distance;
				cerr << "Checking points " << i <<" and "<<j << " values : "<< p[i] << ' '<< p[j] << " number: " << np[i] << ' '<< np[j] <<endl;
				distance = np[j] - np[i-1];
				distance -= 1;
				distance *= D;
				double curr_distance = p[j] - p[i];
				double diff = distance - curr_distance;
				cerr << "diff = "<<diff << endl;
				if(diff > maxdist) maxdist = diff;
			}

		}
		printf("Case #%d: %.6f\n", c++, maxdist/2);
//		cout << "Case #" << c++ << ": " << maxdist/2 << endl;
	}
}

