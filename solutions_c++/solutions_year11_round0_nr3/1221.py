#include <iostream>
#include<algorithm>
#include <vector>
using namespace std;
void stuff()
{
	unsigned int min=1000000,sum=0,xsum=0,l;
	int N;
	cin>>N;
	for(int i=0;i<N;i++)
	{
		cin>>l;
		sum+=l;
		xsum^=l;
		if(l<min)
			min=l;
	}
	if(xsum!=0)
		cout<<"NO";
	else
		cout<<sum-min;
}
int main(void)
{
	int T;
	cin>>T;
	for(int i=0;i<T;i++)
	{
		cout<<"Case #"<<i+1<<": ";
		stuff();
		cout<<endl;
	}
	
}
