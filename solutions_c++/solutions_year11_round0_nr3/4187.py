#include<iostream>
using namespace std;
int main()
{
	int TC;
	cin>>TC;
	int count = 1;
	while ( count <= TC )
	{
		int candy;
		cin>>candy;
		int bag[ candy ];
		int min;
		for ( int i=0; i<candy; i++ )
		{
			cin>>bag[i];
			if ( i == 0 )
			min = bag[0];
			if ( min > bag[i] )
			min = bag[i];
		}
		int temp = 0;
		for ( int i=0; i<candy; i++ )
		{
			temp = temp ^ bag[i];
		}
		if ( temp == 0 )
		{
			int sum = 0;
			for ( int i=0; i < candy; i++ )
			{
				sum = sum + bag[i];
			}sum = sum - min;
			cout<<"Case #"<<count<<": "<<sum<<endl;
		}else cout<<"Case #"<<count<<": "<<"NO"<<endl;
		count++;
	}
	return 0;
}
