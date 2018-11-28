#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <iostream>

using namespace std;

int main(){
	int i,cas,T,n,k;
	cin>>T;
	for (cas=1;cas<=T;cas++){
		cin>>n>>k;
		k=k&((1<<n)-1);
		printf("Case #%d:",cas);
		if (k+1==(1<<n))
			puts(" ON");
		else puts(" OFF");
	}
	return 0;
}
