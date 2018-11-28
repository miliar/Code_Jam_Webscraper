#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


bool isprime(int a){
	if (a == 2) return true;
	for(int i = 2; i * i <= a; ++ i)
		if (a % i == 0) return false;
	return true;
}


int main(){
	freopen("C-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	int T;
	cin>>T;


	for(int t = 0; t < T; ++ t){
		int N;
		cin>>N;
		vector<int> prime;
		int minc = 0, maxc = 0;
		for(long i = 2; i <= N; ++ i)
			if (isprime(i)){
				prime.push_back(i);
			}
		if (N == 1) {minc = 1; maxc = 1;}
		else{
			maxc = 1;
			for(int i = 0; i < prime.size(); ++ i){
				int p = prime[i];
				++ maxc;
				while (prime[i] * p <= N) {prime[i] = prime[i] * p; ++ maxc;}
			}
			sort(prime.begin(),prime.end());
			int f[1000];
			memset(f,0,1000 * sizeof(int));
			for(int i = 0; i < prime.size(); ++ i){
				cerr<<i<<endl;
				if (f[i] == 0){
					int ss = prime[i];
					for(int j = prime.size() - 1; j > i; -- j){
						if (f[j] == 0 && ss * prime[j] <= N){
							ss *= prime[j];
							f[j] = 1;
							j = prime.size() - 1;
						}
					}
					++ minc;
				}
			}
		}

		cout<<"Case #"<<t+1<<": "<<maxc - minc<<endl;
	}

	return 0;
}