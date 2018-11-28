#include<cstdio>
#include<algorithm>
using namespace std;

int main(){
	int testy;
	scanf("%d", &testy);
	for(int i = 1; i <= testy; i++){
		long long suma = 0;
		int m = 1000123000, n, c, x = 0;
		scanf("%d", &n);
		while(n--){
			scanf("%d", &c);
			x ^= c;
			m = min(m, c);
			suma += c;
		}
		printf("Case #%d: ", i);
		if(x==0)
			printf("%lld\n", suma-m);
		else
			printf("NO\n");
	}
	return 0;
}
