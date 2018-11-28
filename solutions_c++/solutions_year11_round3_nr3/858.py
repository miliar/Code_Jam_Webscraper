#include<iostream>
#include<cmath>
#include<vector>
#include<algorithm>
#include<cstring>
#include<ctime>
#include<cstdlib>
using namespace std;


int main()
{
	
	//freopen("in.in", "r", stdin);
	//freopen("out.out", "w", stdout);
	int i, j, k, ii, n, m, tt, a[200], l, h;
	bool fl;
	cin>>tt;
	for(ii = 1; ii<=tt; ii++)
	{
		cin>>n>>l>>h;
		for(i = 1; i<=n; i++)
			cin>>a[i];
		
		for(i = l; i<=h; i++)
		{
			fl = 1;
			for(j = 1; j<=n; j++)
				if(!(a[j]%i == 0 || i%a[j] == 0))
				{
					fl = 0;
					break;
				}
			if(fl)
				break;
		}
		cout<<"Case #"<<ii<<": ";
		if(!fl)
			cout<<"NO\n";
		else
			cout<<i<<'\n';
	}
	return 0;
}