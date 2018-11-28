#include<stdio.h>
#include<math.h>
#include<iostream.h>
using namespace std;
int main()
{
long long int test,k,i,j,q,a,b,c,p,t;
freopen("B-large(2).in","r",stdin);
freopen("out.txt","w",stdout);
cin>>test;
k=0;
while(k<test)
{
	p=0;
	cin >>a>>b>>c;
	t=c;
	q=b;
	while(1)
	{
	if(a*c>=q) break;
	p++;
	q=(long long int) ceil(sqrt(a*q));
	
	}
	
	cout <<"Case #"<<k+1<<": "<<p<<"\n";
	k++;
}
return 0;
}
