#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <set>
#include <string>
#include <list>
#include <map>
#include <cmath>

using namespace std;


int N;
int X[40], Y[40], R[40];

double dist(int i, int j) {
	double w = X[i]-X[j];
	double h = Y[i]-Y[j];
		return sqrt(w*w+h*h);
}

void solve() {
	cin >> N;

	double result = (1<<29);
	for(int i = 0; i < N; i++) cin >> X[i] >> Y[i] >> R[i];
	if(N == 1) result = R[0];
	if(N == 2) result = max(R[0], R[1]);
	else {	
		for(int i = 0; i < 3; i++) {
			int j = (i+1)%3;
			int k = (i+2)%3;		
			double c = max(double(R[i]), (dist(j, k) + R[j] + R[k])/2);	
			result = min(result, c);		
		}
	}

	printf("%lf\n", result);
	//cout << result << endl;



}


int main() {		
	int C;
	cin >> C;	
	for(int i = 1; i <= C; i++) {
		cout << "Case #" << i << ": ";
		solve();	
	}
}