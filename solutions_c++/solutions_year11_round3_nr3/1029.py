#include <iostream>

using namespace std;

const int maxn = 102;
int n,l,h,f[maxn];

int solve()
{
	int i , j ;
	for ( i = l ; i <= h ; i++)
	{
		for( j = 1 ; j <= n ; j++)
			if(!((f[j]%i==0)||(i%f[j]==0)))
				break;
		if(j>n)	return i;
	}
	return 0;
}

int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	int t , i , j , k ;
	cin>>t;
	for( i = 1 ; i <= t ; i++)
	{
		cin>>n>>l>>h;
		for( j = 1 ; j <= n ; j++)
		{	
			cin>>f[j];
		}
		cout<<"Case #"<<i<<": ";
		j = solve() ;
		if( j > 0 )	cout<<j<<endl;
		else cout<<"NO"<<endl;
	}
	return 0;
}