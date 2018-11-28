#include<iostream>

using namespace std;

long T[1024];

long gcd(long a,long b); 

int main()
{
	int i,j,C,N;
	long res,tmp;
	scanf("%d",&C);
	for(i=0;i<C;i++){
		scanf("%d",&N);
		for(j=0;j<N;j++){
			scanf("%ld",T+j);
		}
		tmp=abs(T[1]-T[0]); 
		for(j=2;j<N;j++){
			tmp=gcd(tmp,abs(T[j]-T[j-1]));
		}
		res=0;
		if(T[0]%tmp!=0)
			res=tmp-T[0]%tmp;
		printf("Case #%d: %ld\n",i+1,res);
	}
	return 0;
}

long gcd(long a,long b)
{
	long r;
	if(a<b){
		r=a;a=b;b=r;
	}
	if(b==0)
		return a;
	while(a%b!=0){
		r=a%b; a=b; b=r;
	}
	return b;
}