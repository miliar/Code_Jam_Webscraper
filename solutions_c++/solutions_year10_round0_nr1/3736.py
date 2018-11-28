#include<iostream>
#include<math.h>
using namespace std;
int main()
{
	int no, i, n;
	long long k, pwr, tmp;
	cin>>no;
	for(i=0; i<no; i++)
	{
		cin>>n>>k;
		pwr = pow(2,n) - 1;
		tmp = k & pwr;
		if(tmp == pwr)
			cout<<"Case #"<<i+1<<": ON"<<endl;
		else
			cout<<"Case #"<<i+1<<": OFF"<<endl;
	}
	return 0;
}
