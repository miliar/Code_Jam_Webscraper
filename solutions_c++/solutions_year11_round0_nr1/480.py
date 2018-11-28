#include <cmath>
using namespace std;
#include <iostream>
#include <algorithm>
#include <cstdio>

//By chyx111
#define DBG(a) cerr << #a << ": " << (a) << endl
#define Rep(i,n) for(int n_ = (n), i = 0; i< n_; ++i)

int main() {
	int ca;cin>>ca;
	Rep(ica,ca){
		int n; scanf("%d", &n);
		int posO = 1;
		int posB = 1;
		int pos, prevO = 0, prevB = 0, currTime = 0;
		char color;
		Rep(i, n){
			scanf(" %c%d", &color, &pos);
			if( color == 'O' ){
				currTime += max(1L, labs(pos - posO) + 1 - (currTime - prevO));
				prevO = currTime;
				posO = pos;
			}else{
				currTime += max(1L, labs(pos - posB) + 1 - (currTime - prevB));
				prevB = currTime;
				posB = pos;
			}
		}
		printf("Case #%d: %d\n", ica+1, currTime);
	}
	
	return 0;
}

