#include <stdio.h>
#include <string>
using namespace std;

int n,k;

int main() {
	int d;scanf("%d\n",&d);
	for(int s=1;s<=d;s++) {
		scanf("%d%d",&n,&k);
		int dl=1<<n;
		int wyn=(k+1)%dl==0;
		printf("Case #%d: %s\n",s,wyn?"ON":"OFF");
	}
	return 0;
}
