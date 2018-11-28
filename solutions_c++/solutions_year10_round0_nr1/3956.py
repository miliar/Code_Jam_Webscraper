#include <iostream>
#include <limits.h>

using namespace std;

int main()
{
	int T;
	scanf("%d",&T);
	for(int it=0;it<T;it++) {
		int N,K;
		scanf("%d %d",&N,&K);
		int diff = 1;
		for(int i=0;i<N;i++) {
			diff = diff*2;
		}
		K++;
		printf("Case #%d: ",it+1);
		if(K%diff==0) {
			printf("ON\n");
		}else {
			printf("OFF\n");
		}
	}
	return 0;
}
