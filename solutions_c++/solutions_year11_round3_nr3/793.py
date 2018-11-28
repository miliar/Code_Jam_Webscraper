#include <cstdio>
#include <set>
using namespace std;

unsigned long long ggd(unsigned long long a, unsigned long long b){
	if(a%b==0){
		return b;
	}else{
		return ggd(b, a%b);
	}
}
unsigned long long kgv(unsigned long a, unsigned long long b){
	return a*b/ggd(a,b);
}

int main(){
	unsigned int t;
	scanf("%d",&t);
	unsigned long long n, l, h;
	unsigned long long tmp;
	bool good, answered;
	for(unsigned int j = 0; j < t; ++j){
		scanf("%llu%llu%llu", &n, &l,&h);
		printf("Case #%d: ", j+1);
		set<unsigned long long> freqs;
		for(unsigned int k = 0; k < n; ++k){
			scanf("%llu", &tmp);
			freqs.insert(tmp);
		}
		answered = false;
		for(unsigned long long k = l; k <= h; ++k){
			good = true;
			for(set<unsigned long long>::iterator it = freqs.begin(); it != freqs.end(); ++it){
				if(!((*it) % k == 0 || k% (*it) == 0)){
					good = false;
					break;
				}
			}
			if(good){
				printf("%llu\n", k);
				answered = true;
				break;
			}
		}
		if(!answered)
			printf("NO\n");
	}
	return 0;
}
