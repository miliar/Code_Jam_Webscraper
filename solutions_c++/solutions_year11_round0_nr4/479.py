#include <numeric>
#include <cassert>
#include <cmath>
using namespace std;
#include <iostream>
#include <string>
#include <algorithm>
#include <cstring>
#include <stack>
#include <cstdio>
#include <set>
#include <vector>

//By chyx111
#define Rep(i,n) for(int n_ = (n), i = 0; i< n_; ++i)

int main() {
	int ca;cin>>ca;
	Rep(ica,ca){
		int n; 
		scanf("%d", &n);
		int arr[n];
		int xor_sum = 0;
		Rep(i, n){
			scanf("%d", arr+i);
			xor_sum ^= arr[i];
		}
		int sum = accumulate(arr, arr+n, 0);
		printf("Case #%d: ", ica+1);
		if( xor_sum ){
			puts("NO");
		}else{
			printf("%d\n", sum - *min_element(arr, arr+n) );
		}
	}
	return 0;
}

