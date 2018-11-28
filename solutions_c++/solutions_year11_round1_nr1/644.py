#include <cmath>
using namespace std;
#include <iostream>
#include <cstdio>

//By chyx111
typedef long long ll;
#define Rep(i,n) for(int n_ = (n), i = 0; i< n_; ++i)
ll n, p, q;

bool solve(){
	if( q == 100 && p != 100 ){
		return false;
	}
	if( q == 0 && p != 0 ){
		return false;
	}
	if( n >= 100 ){
		return true;
	}
	for(int d = 1; d <= n; ++d){
		if( p * d % 100 == 0 ){
			return true;
		}
	}
	return false;
}

int main() {
	int ca;cin>>ca;
	Rep(ica,ca){
		printf("Case #%d: ", ica+1);
		cin>>n>>p>>q;

		if( solve() ){
			puts("Possible");
		}else{
			puts("Broken");
		}
	}
	return 0;
}

