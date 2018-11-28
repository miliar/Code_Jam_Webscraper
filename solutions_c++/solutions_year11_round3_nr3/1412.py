#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
using namespace std;

bool prime(long long n){
	for(long long i=2;i*i<=n;i++){
		if(n%i==0)	return false;
	}
	return n != 1;
}

long long gcd(long long a, long long b){
	if(b==0)	return a;
	return gcd(b, a%b);
}

long long lcm(long long a, long long b){
	return (a>=b)?( a*b/gcd(a,b) ):( a*b/gcd(b,a) );
}

int main(){
	int T; cin >> T;
	for(int t=0;t<T;t++){
		long long  N, L, H; cin >> N >> L >> H;
		vector <long long> P;

		for(long long i=0;i<N;i++){
			int temp; cin >> temp;
			P.push_back(temp);
		}

		bool ok = false;
		for(long long i=L;i<=H;i++){
			bool flag = true;
			for(long long j=0;j<N;j++){
				if(i%P[j]!=0 && P[j]%i!=0){
					flag = false;
					break;
				}
			}
			if(flag){
				printf("Case #%d: %ld\n", t+1, i);
				ok = true;
				break;
			}
		}
		if(!ok){
			printf("Case #%d: NO\n", t+1);
		}

	}
	return 0;
}