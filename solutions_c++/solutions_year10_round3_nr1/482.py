#include<iostream>
#include<cstdio>
#include<set>
#include<map>
#include<vector>
#include<list>
#include<cstring>
using namespace std;
int main()
{
	int sun;
	cin>>sun;
	for(int pra=0;pra<sun;pra++)
	{
	int n;
	cin>>n;
	int arr[n],brr[n];
	for(int i=0;i<n;i++)
		cin>>arr[i]>>brr[i];
	int count=0;
	for(int i=0;i<n;i++)
		for(int j=i+1;j<n;j++)
		{
				if((arr[i]<arr[j] && brr[i]>brr[j]) ||(arr[i]>arr[j] && brr[i]<brr[j]))
					count++;
		}
	cout<<"Case #"<<pra+1<<": "<<count<<endl;
	}
	return 0;
}
