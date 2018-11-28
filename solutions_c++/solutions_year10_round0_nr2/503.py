#include <cstdio>
#include <cmath>
#include <vector>
#include<iostream>
using namespace std; 
typedef int LL;


LL gcd(LL a,LL b)
{
	if( a==0 )return b;
	if( b==0 )return a;
	LL r;
	if( a< b) swap(a,b);
	do{
		r=a%b;
		a=b;
		b=r;
	}while(r);
	return a;
}

//LL abs(LL x)
//{
//	if( x>0 )return x;
//	return -x;
//}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("codejam.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for(int cases=1;cases<=T;cases++){
		int n;
		scanf("%d",&n);
		LL a,b,c,ans;
		if(n==2){
			scanf("%d %d",&a,&b);
			LL x=abs(a-b);
			if( x==1 )ans=0;
			else if( a%x==0)ans=0;
			else ans=x-(a%x);
		}
		else if( n==3 ){
			scanf("%d %d %d",&a,&b,&c);	
			LL x=gcd( abs(a-b), abs(a-c) );
		
			x=gcd(x,abs(b-c));	
			if( x==1 )ans=0;
			else if( a%x==0)ans=0;
			else ans=x-(a%x);
		}
		printf("Case #%d: %d\n",cases,ans );
	}
	return 0;
}
