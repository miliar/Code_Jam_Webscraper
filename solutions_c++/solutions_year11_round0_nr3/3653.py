#include<iostream>
using namespace std;
int main()
{
	int t;
	cin>>t;
	for(int j = 1 ; j<=t ; j++)
	{
		int n,sum=0,min = 1000000,x = 0,arr;
		cin>>n;
		//int[] arr = new int[n];
		for(int i=0 ; i<n ; i++)
		{
			cin>>arr;
			sum += arr;
			if (arr < min) min = arr;
			x = x^arr;
		}
		if (x != 0) cout<<"Case #"<<j<<": NO\n";
		else cout<<"Case #"<<j<<": "<<(sum-min)<<endl;
	}
	return 0;
}
			
			
