#include <cmath>
using namespace std;
#include <iostream>
#include <cstdio>

//By chyx111
#define two(x) (1<<(x))
#define Rep(i,n) for(int n_ = (n), i = 0; i< n_; ++i)

int main() {
	int ca;cin>>ca;
	Rep(ica,ca){
		int n, k;
		scanf("%d%d", &n, &k);
		printf("Case #%d: %s\n", ica+1, ( ((k & two(n)-1) == two(n)-1 ) ? "ON" : "OFF") );
	}
	return 0;
}

