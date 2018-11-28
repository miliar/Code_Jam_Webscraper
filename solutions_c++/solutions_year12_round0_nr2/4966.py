#include <algorithm>
#include <cmath>
#include <iostream>
using namespace std;

//~ int surprising(int n) {	return ((n+1)/3) + 1; }
int not_surprising(int n) {	return ceil((double)n/3); }

int main() {
	ios_base::sync_with_stdio(false);
	
	int T, N, p, S, t, ns;
	int count;
	
	cin >> T;
	for(int test=1; test<=T; test++) {
		cout << "Case #" << test << ": ";
		cin >> N >> S >> p;
		count = 0;
		for(int i=0; i<N; i++) {
			cin >> t;
			ns = not_surprising(t);
			if(ns >= p) count++;
			else if(S && t && t<29 && (t%3)!=1 && ns == p-1) {
				count++;
				S--;
			}
		}	
		cout << count << "\n";	
	}
	
	return 0;
}
