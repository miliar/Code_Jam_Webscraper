#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>

using namespace std;

int main(){
	int casos;
	scanf("%d", &casos);
	for(int i = 1; i <= casos; i++){
		int n, k;
		scanf("%d %d", &n, &k);
		printf("Case #%d: ", i);
		if(k%(1<<n) == (1<<n)-1)printf("ON\n");
		else printf("OFF\n");
	}
	return 0;
}
