#include <stdio.h>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <math.h>
using namespace std;

#define debug 0
#define dprintf debug&&printf
char tal[64];

long long puw(long long base, int exp) {
	if(exp == 0) return 1;
	long long ans = base;
	while(--exp){
		ans *= base;
	}
	return ans;
}
void test() {
	scanf("%s",tal);
	int len = strlen(tal);
	map<char, int> g;
	int nextNum = 1;
	long long ans = 0;
	for(int i=0;i<len;i++){
		if(g.find(tal[i]) == g.end()){
			g[tal[i]] = nextNum;
			if(nextNum == 1)
				nextNum = 0;
			else if(nextNum == 0)
				nextNum = 2;
			else
				nextNum++;
		}
	}
	if(g.size() == 1)g['#']=42;
	for(int i=0;i<len;i++){
		dprintf("%c %d %lld\n",tal[i], g[tal[i]], puw(g.size(), len-i-1));
		ans += (long long)g[tal[i]] * puw(g.size(), len-i-1);
	}
	printf("%lld\n",ans);
}

int main(){
	int N;
	scanf("%d", &N);
	for(int fall=0;fall<N;fall++){	
		printf("Case #%d: ", fall+1);
		test();
	}
	return 0;
}
