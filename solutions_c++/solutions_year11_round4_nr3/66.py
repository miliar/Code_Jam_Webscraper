#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <set>

using namespace std;

vector<long long> primos;
char ehPrimo[1000100];

int main(){
	int caso = 1;
	int casos;
	
	scanf("%d", &casos);
	long long N;
	
	memset(ehPrimo,1,sizeof(ehPrimo));
	primos.push_back(2);
	for(int i = 4; i <= 1000000; i+=2){
		ehPrimo[i] = 0;
	}
	
	for(int j = 3; j <= 1000000; j += 2){
		if(ehPrimo[j]){
			primos.push_back(j);
			
			for(int i = 2*j; i <= 1000000; i += j){
				ehPrimo[i] = 0;
			}
		}
	}
	
	for(int i = 1; i <= casos; i++){
		scanf("%lld", &N);
		long long res = N == 1 ? 0 : 1;
		for(int j = 0; j < primos.size() && primos[j]*primos[j] <= N; j++){
			int exp = 0;
			long long prod = 1;
			while(prod <= N/primos[j]){
				prod *= primos[j];
				exp++;
			}
			res += exp-1;
		}
		printf("Case #%d: %lld\n", caso++, res);
	}
	
	return 0;
}