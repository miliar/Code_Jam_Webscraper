#include<iostream>
#include<fstream>  //comment
using namespace std;
int main()
{
	ofstream fout("C:/Codejam/candy.txt"); //comment
	int test,n,arr[1001];
	cin>>test;
	for(int i=0;i<test;i++)
	{
		cin>>n;
		for(int j=0;j<n;j++)
			cin>>arr[j];
		int good=arr[0];
		for(j=1;j<n;j++)
		{
			good=good^arr[j];
		}
		if(good!=0)
		{
			fout<<"Case #"<<i+1<<": "<<"NO"<<"\n"; //comment
			cout<<"Case #"<<i+1<<": "<<"NO"<<"\n";
			continue;
		}
		int sum=0,min=1000001;
		for(j=0;j<n;j++)
		{
			sum+=arr[j];
			if(min>arr[j])
			{
				min=arr[j];
			}
		}
		sum-=min;
		fout<<"Case #"<<i+1<<": "<<sum<<"\n";  //comment
		cout<<"Case #"<<i+1<<": "<<sum<<"\n";


	}
	return 0;
}