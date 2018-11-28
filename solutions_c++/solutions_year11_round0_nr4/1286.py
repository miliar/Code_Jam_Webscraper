#include<iostream>
using namespace std;

int a[2000];
int ans;
int main()
{
	int TT;
	cin>>TT;
	int n;
	for( int T = 1;T<=TT;T++ )
	{
		cout << "Case #"<<T<<": ";
		cin>>n;
		for( int i = 1;i<=n;i++ ) cin>>a[i];

		ans = 0;
		for( int i = 1;i<=n;i++ ) if( a[i]!=i )
		{
			ans++;
			int j = a[i],k;
			a[i] = i;
			while( j!=i )
			{
				k = j;
				j = a[j];
				a[k] = k;
				ans++;
			}
		}
		cout << ans << ".000000" << endl;
	}
	return 0;
}
