#include<iostream>
#include"bigint\bigint.h"
// Used class RossiBigInt from http://sourceforge.net/projects/cpp-bigint/
using namespace std;
char is[1000][60];
RossiBigInt i[1000];
static const RossiBigInt Zero (0);
static const RossiBigInt One  (1);
static const RossiBigInt Two  (2);
RossiBigInt gcd(RossiBigInt x,RossiBigInt y)
{
	while( 1 )
	{
		if( x==Zero ) return y;
		if( y==Zero ) return x;
		if( x>y ) x=x%y;
		else y=y%x;
	}
	return Zero;
}
int main()
{
	int a,n;
	RossiBigInt t,mn;
int _,T;
cin>>T;
for(_=1;_<=T;_++)
{
	cin>>n;
	for(a=0;a<n;a++) cin>>is[a];
	for(a=0;a<n;a++) i[a]=RossiBigInt(is[a],DEC_DIGIT);
	mn=i[0];
	for(a=1;a<n;a++) if( i[a]<mn ) mn=i[a];
	t=Zero;
	for(a=0;a<n;a++) t=gcd(t,i[a]-mn);
//	printf("%d %d\n",mn,t);
//	if( t==0 ){ printf("Case #%d: 0\n",_); continue; }
	cout<<"Case #"<<_<<": "<<(t-mn%t)%t<<"\n";
}
	return 0;
}
