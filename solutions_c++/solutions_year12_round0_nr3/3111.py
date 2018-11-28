#include <iostream>
#include <cstdio>
#include <cmath>
#include <set>
using namespace std;

#define FORi(m) for(int i = 0; i < (m); ++i)
#define FOR(i, M) for( int i = 0; i < (M); ++i )


int main(){
	int T;
	cin >> T;
	
	FOR(t, T){
		printf("Case #%d: ", t+1);
		
		int A, B;
		cin >> A >> B;
		int D = 1 + (int)(log10(A)), N = 0;
		if (D == 1) {
			cout << '0' << endl;
			continue;
		}
		
		for( int n = A; n <= B-1; ++n ){
			set<int> already;
			for( int i = 1; i < D; ++i ){
				int left = (int)(n/(int)pow(10,i));
				int right = n-left*(int)pow(10,i);
				int r = right*(int)pow(10,D-i)+left;
				
				if (n < r && r <= B && already.find(r) == already.end()){
					++N;
					already.insert(r);
				}
				/*else {
					cout << "x-->";
				}
				cout << n << ' ' << r << endl;*/
			}
		}
		
		cout << N << endl;
	}
}
