#include <iostream>
#include <cmath>

using namespace std;

bool prime[1000001];

int solveSmall(int N){
	if(N==1) return 0;
	int cnt[1001];
	memset(cnt, 0, sizeof(cnt));
	for(int i=2;i<=N;i++){
		int t = i;
		for(int j=2;j<=t;j++){
			int c = 0;
			if(!prime[j]) continue;
			while(t%j==0){
				c++;
				t/=j;
			}
			cnt[j] = max(cnt[j], c);
		}
	}
	int res = 1;
	for(int i=2;i<=N;i++)
		if(cnt[i] > 0) res += cnt[i]-1;
	return res;
}

int solveLarge(long long N){
	if(N==1) return 0;
	int res = 1;
	for(int j=2;j<=sqrt((double)N)+1;j++){
		if(!prime[j]) continue;
		long long t = j;
		int c = 1;
		while(t*j <= N){
			c++;
			t *= j;
		}
		res += c-1;
	}
	return res;
}

int main(){
	int TEST; cin >> TEST;
	memset(prime, false, sizeof(prime));
	for(int i=2;i<=1000000;i++) prime[i] = true;
	for(int i=2;i<=1000000;i++){
		if(!prime[i]) continue;
		for(int j=2*i;j<=1000000;j+=i)
			prime[j] = false;
	}
	for(int test=1;test<=TEST;test++){
		long long N; cin >> N;
		printf("Case #%d: %d\n", test, solveLarge(N));
	}
}
