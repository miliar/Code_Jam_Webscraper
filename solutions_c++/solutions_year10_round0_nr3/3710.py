#include <iostream>
#include <vector>

//#define MYDEBUG
#define MAXN 1000
#define MAXGSZ 10 // *** small = 10, large = 10^7

typedef unsigned long long myint;

using namespace std;

int main() {
	myint T, t;
	myint R, r;
	myint k;
	myint N, i;
	
	//myint g[MAXN];
	myint P, j, cur;
	vector<myint> start(MAXN * MAXGSZ), end(MAXN * MAXGSZ);
	myint earned;
	
	cin >> T;
	for(t = 1; t <= T; t++) {
		cin >> R >> k >> N;
		
		myint g[N];
		j = 0;
		for(i = 0; i < N; i++) {
			cin >> g[i];
			j += g[i];
		}
		P = j;
		
		if(P < k) {
			#ifdef MYDEBUG
			cout << "*";
			#endif
			
			cout << "Case #" << t <<": " << (earned = R * P) << endl;
			continue;
		}
		
		j = 0;
		for(i = 0; i < N; i++) {
			fill(&start[j], &start[j + g[i]], j);
			fill(&end[j], &end[j + g[i]], j + g[i] - 1);
			j += g[i];
		}
		
		#ifdef MYDEBUG
		cout << T << endl;
		cout << R << ' ' << k << ' ' << N << endl;
		for(i = 0; i < N; i++) {
			cout << g[i] << ' ';
		}
		cout << endl;
		for(j = 0; j < P; j++) {
			cout << start[j] << ' ';
		}
		cout << endl;
		for(j = 0; j < P; j++) {
			cout << end[j] << ' ';
		}
		cout << endl;
		#endif
		
		cur = 0;
		
		#ifdef MYDEBUG
		//cout << "cur = " << cur << " [START]" << endl;
		#endif
		
		j = 0;
		earned = R * k;
		for(r = 0; r < R; r++) {
			j = (cur + k - 1) % P;
			//earned -= (k - 1) / P;
			#ifdef MYDEBUG
			//cout << "j = " << j << endl;
			#endif
			
			if(j != end[j]) {
				earned -= (j - start[j] + 1);
				cur = start[j];
			}
			else
				cur = (j + 1) % P;
			
			#ifdef MYDEBUG
			//cout << "cur = " << cur << endl;
			#endif
		}
		
		cout << "Case #" << t <<": " << earned << endl;
	}
	
	return 0;
}
