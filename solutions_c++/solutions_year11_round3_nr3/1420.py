#include<iostream>
using namespace std;
int main()
{
	int TC;cin>>TC;
	for( int k=0; k <TC; k ++ ) {
	int size;cin>>size;
	int lb, ub;
	cin>>lb;cin>>ub;
	int A[size];
	for ( int j=0; j < size; j++ )
	cin>>A[j];
	int out;
	bool flag = false;
	for ( int i=lb; i<=ub; i++ )
	{
		int counter = 0;
		flag = false;
		for ( int j=0; j < size; j++ )
		{
			if ( i % A[j] == 0 || A[j] % i == 0 )
			{
				counter++;
				if ( counter == size )
				{
					out = i;
					flag = true;
				}
			}
			else break;
		}
		if ( flag )
		break;
	}
	if ( flag )
	cout<<"Case #"<<k+1<<": "<<out<<endl;
	else cout<<"Case #"<<k+1<<": "<<"NO"<<endl;
	}
	return 0;
}
