# include <iostream>
using namespace std;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int i,j,k,p,ans;
	int t;
	int n;
	char a[50][50];
	int b[50];

	cin>>t;

	for(i = 1; i <= t; ++i)
	{
		ans = 0;
		cin>>n;
		for(j = 0; j < n; ++j)
		{
			b[j] = 0;
			for(k = 0; k < n; ++k)
			{
				cin>>a[j][k];
				if(a[j][k] == '1')
					b[j] = k+1;
			}
		}
		for(j = 0; j < n; ++j)
		{
			if(b[j] > j + 1)
			{
				for(k = j + 1; k < n; ++k)
				{
					if(b[k] <= j + 1)
					{
						for(p = k; p > j; --p )
						{
							swap(b[p], b[p-1]);
							ans++;
						}
						break;
					}
				}
			}
		}
		cout<<"Case #"<<i<<": "<<ans<<endl;
	}
	return 0;
}