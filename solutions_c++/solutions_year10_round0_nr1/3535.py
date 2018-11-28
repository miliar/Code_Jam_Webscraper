#include<cstdio>

int Z,N,K;
bool ok;
int main(){
	scanf("%d",&Z);
	for (int i=1;i<=Z;++i){
		scanf("%d%d",&N,&K);
		ok = false;
		if ((K&((1<<N)-1))==(1<<N)-1) ok = true;
		printf("Case #%d: ",i);
		if (ok) puts("ON");
		else puts("OFF");
	}

	return 0;
}
