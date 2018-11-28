#include<iostream>
using namespace std;
int main()
{
	int sun;
	cin>>sun;
	for(int pra=1;pra<=sun;pra++)
	{
	cout<<"Case #"<<pra<<": ";
	int n,m;
	cin>>n>>m;
	int arr[n+1];
	arr[0]=0;
	for(int i=1;i<=n;i++)
		arr[i]=arr[i-1]*2+1;


	if(m<arr[n])
		cout<<"OFF"<<endl;
	else
	{
		if((m+1)%(arr[n]+1)==0)
			cout<<"ON"<<endl;
		else 
			cout<<"OFF"<<endl;
	}	

	}
}
