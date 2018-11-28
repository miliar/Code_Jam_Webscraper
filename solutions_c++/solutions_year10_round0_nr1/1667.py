#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>
using namespace std;

int t,xx,n,k,bit,tmp;
bool ON;

void open(){
	freopen("alarge.in","r",stdin);
	freopen("alarge.out","w",stdout);
}

int main(){
	open();
	scanf("%d",&t);
	xx=1;
	while (t--){
		scanf("%d%d",&n,&k);
		bit=(1<<(n));
		k-=(bit-1);
		tmp=k%bit;
		if (tmp==0) ON=1;
		else ON=0;
		printf("Case #%d: ",xx++);
		if (ON) printf("ON\n");
		else printf("OFF\n");
	}
	return 0;
}
