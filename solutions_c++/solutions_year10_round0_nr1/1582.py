#include<cstdio>
using namespace std;

int main() {
	int c=0,cc=0,n,k;
	for (scanf("%d",&c);cc<c;cc++) {
		scanf("%d%d",&n,&k);
		printf("Case #%d: %s\n",cc+1,((k+1)%(1<<n)==0)?("ON"):("OFF"));
	}
}
