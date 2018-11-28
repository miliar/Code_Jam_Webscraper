#include <iostream>

using namespace std;
unsigned long long power(unsigned long long n,unsigned long long k)
{
	unsigned long long cnt=1;
	for(unsigned long long i=0;i<k;i++)
		cnt*=n;
	return cnt;
}
int main()
{
	unsigned long long ie2;
	cin>>ie2;
	for(unsigned long long ie=1;ie<=ie2;ie++)
	{
		unsigned long long n,k;
		cin>>n>>k;
		unsigned long long nz=power(2,n);
		cout<<"Case #"<<ie<<": ";
		if(k%nz==nz-1)
			cout<<"ON\n";
		else 
			cout<<"OFF\n";
	}
	return 0;
}