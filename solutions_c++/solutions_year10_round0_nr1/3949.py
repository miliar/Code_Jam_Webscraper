#include<iostream.h>
#include<math.h>
main()
{
long n,k,t,v,c=0;
cin>>t;
while(t--)
{
	c++;
	cin>>n>>k;
	v=pow(2,n);cout<<"Case #"<<c;
	if(k%v==v-1)
	cout<<": ON\n";
	else
	cout<<": OFF\n";
}
}
