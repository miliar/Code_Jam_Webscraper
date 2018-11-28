#include <iostream>
#include <cstdio>
using namespace std;

int main(){
	int T;
	cin >> T;
	for( int t = 1; t <= T; ++t ){
		int N;
		cin >> N;
		
		int robots[2][2] = {{1, 0},{1, 0}};
		int p, time = 0;
		char r;
		while(N--){
			cin >> r >> p;
			int i = r == 'O'? 0: 1;
			int eta = abs(robots[i][0]-p);
			
			if (robots[i][1] >= eta){
				time += 1;
				robots[!i][1] += 1;
			}
			else {
				int l = eta - robots[i][1] + 1;
				robots[!i][1] += l;
				time += l;
			}
			robots[i][0] = p;
			robots[i][1] = 0;
		}
		printf("Case #%d: %d\n", t, time);
	}
}
