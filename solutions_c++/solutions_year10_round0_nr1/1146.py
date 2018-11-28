#include<iostream>
using namespace std;

int main()
{
	freopen("A-large.in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int T,N,K;
	scanf("%d",&T);
	for(int cases=1;cases<=T;cases++){
		scanf("%d %d",&N,&K);
		bool on=true;
		for(int i=0;i<N;i++){
			if( !( K& (1<<i)) )
				on=false;
		}
		if(on )
			printf("Case #%d: ON\n",cases);
		else printf("Case #%d: OFF\n",cases);
	}
	return 0;


}