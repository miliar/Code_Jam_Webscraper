#include<cstdio>

using namespace std;

int T,n,k,I;

int main(){
	scanf("%d",&T);
	while (T--){
		scanf("%d%d",&n,&k);
		printf("Case #%d: ",++I);
		puts((k&((1<<n)-1))==(1<<n)-1?"ON":"OFF");
	}
}
