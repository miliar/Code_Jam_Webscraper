#include <cstdio>
#include <cstring>
#include <cstdlib>
int Sim(int N,int K){
	int s=(1<<N)-1,b;
	while(K--){
		b=s&(-s);
		if(b) s^=((b<<1)-1);
		else s=(1<<N)-1;
	}
	return s;
}
int main(){
	freopen("Ain.txt","r",stdin);
	freopen("Aout.txt","w",stdout);
/*	for(int i=1;i<=10;++i){
		printf("test %d\n",i);
		for(int j=0;j<10000;++j){
			int mask=(1<<i)-1;
			int v=mask^(j&mask);
			if(v!=Sim(i,j)){
				printf("%d %d %d %d\n",i,j,v,Sim(i,j));
				system("pause");
			}
		}
	}
*/
	int TT;
	scanf("%d\n",&TT);
	for(int cas=1;cas<=TT;++cas){
		int N,K;
		scanf("%d %d",&N,&K);
		int mask=(1<<N)-1;
		int v=mask^(K&mask);
		printf("Case #%d: %s\n",cas,v>0?"OFF":"ON");
	}
	return 0;
}

