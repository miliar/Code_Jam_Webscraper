#include<iostream>
using namespace std;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("Out11.txt","w",stdout);
	
	int ar[32];
	ar[0]=1;
	for ( int i=1;i<31;++i)
		ar[i]=ar[i-1]<<1;
	
	
	
	int i=0,t;
	scanf("%d",&t);
	while(++i,i<=t){
		
		int N,K;
		scanf("%d %d",&N,&K);
		int num=ar[N];
		if ( (K+1)%num==0)
			printf("Case #%d: ON\n",i);
		else
			printf("Case #%d: OFF\n",i);
		
	}
return 0;
}
	
