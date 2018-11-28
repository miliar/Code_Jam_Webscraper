#include<iostream>
using namespace std;
main()
{
	int t,n,k,num;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		cin>>n>>k;
		num=(1<<n)-1;
		cout<<"Case #"<<i+1<<": "<<(((num&k)==num)?"ON":"OFF")<<endl;
	}
}
