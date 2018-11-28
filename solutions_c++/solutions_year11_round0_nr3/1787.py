#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	int sum,n,j,t,i,ans,min_value,Tcase;
	//freopen("input.in","r",stdin);
	//ofstream fout("output.txt");
	cin>>Tcase;
	for ( i = 1 ; i <= Tcase ; i++)
	{
		cin>>n;
		min_value = 10001000;
		for ( ans = sum = j = 0 ; j < n ; j++)
		{
			cin>>t;
			sum += t ;
			ans ^= t ;
			if( min_value > t )	min_value = t ;
		}
		if( ans != 0 )	fout<<"Case #"<<i<<": NO"<<endl;
		else			cout<<"Case #"<<i<<": "<<sum-min_value<<endl;
	}
	return 0;
}