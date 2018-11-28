#include <iostream>
#include <cstdio>
using namespace std;

#define FORi(m) for(int i = 0; i < (m); ++i)
#define FOR(i, M) for( int i = 0; i < (M); ++i )

int main(){
	int T;
	cin >> T;
	
	FOR(t, T){
		
		int N, S, p;
		cin >> N >> S >> p;
		
		int M = 0;
		FORi(N){
			int P;
			cin >> P;
			
			int av = P/3, r = P-av*3;
			
			if ((av >= p) || (r && av == p-1)){
				++M;
				continue;
			}
			if (S){
				if ((r == 0 && av > 0 && av == p-1) || (r == 2 && av == p-2)){
					--S;
					++M;
				}
			}
		}
		
		printf("Case #%d: %d\n", t+1, M);
	}
}
