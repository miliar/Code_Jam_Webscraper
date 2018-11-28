#include<iostream>
#include <cmath>
using namespace std; 

int gcd(int a,int b)
{
	if( a==0 )return b;
	if( b==0 )return a;
	int r;
	if( a< b){int t = a;a=b;b=t;}
	do{
		r=a%b;
		a=b;
		b=r;
	}while(r);
	return a;
}

int main()
{
	
	int t;
	int cas = 0;
	freopen("B-small.in","r",stdin);
	freopen("B-small.out","w",stdout);
	scanf("%d",&t);
	while(t--){
		int n;
		scanf("%d",&n);
		cas++;
		int a,b,c,ans;
		if(n==2)
		{
			scanf("%d %d",&a,&b);
			int x=abs(a-b);
			if( x==1 )ans=0;
			else if( a%x==0)ans=0;
			else ans=x-(a%x);
		}
		else if( n==3 )
		{
			scanf("%d %d %d",&a,&b,&c); 
			int x=gcd( abs(a-b), abs(a-c) );
			x=gcd(x,abs(b-c)); 
			if( x==1 )ans=0;
			else if( a%x==0)ans=0;
			else ans=x-(a%x);
		}
		printf("Case #%d: %d\n",cas,ans );
	}
	return 0;
}
