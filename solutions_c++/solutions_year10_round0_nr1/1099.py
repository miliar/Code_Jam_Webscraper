
#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;

int main(){
	int nn;scanf("%d",&nn);
	while(nn--){
		int n,k;scanf("%d%d",&n,&k);
		static int npr=1;
		int mask=(1<<n)-1;
		printf("Case #%d: %s\n",npr++,((k&mask)==mask ? "ON": "OFF"));
	}
	return 0;
}
