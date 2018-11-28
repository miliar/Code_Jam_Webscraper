#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector <vector <int> > arr;
	int t,n;

bool NeedLower(int k)
{
	for (int i = k+1; i < n; i ++)
		if (arr[k][i] == 1)
			return true;
	return false;
}

int main()
{
	freopen("test2.in", "r", stdin);
	freopen("test.out", "w", stdout);
	cin >> t;
	for (int k = 1; k <=t; k ++)
	{
		cin >> n;
		char c;
		arr.assign(n,vector<int>(n,0));
		for (int i = 0; i < n; i ++)
			for (int j = 0; j < n; j ++)
			{
				cin >> c;
				arr[i][j] = c-'0';
			}	
		vector <int> a;
		a.assign(n,-1);
		for (int i = 0; i < n; i ++)
		{

			for (int j = 0; j < n; j ++)
				if (arr[i][j] == 1)
					a[i] = j;
		}
		int ans = 0;





		for (int i = 0; i < n-1; i ++)
			if (a[i] > i)
			{
				int t = i;
				int range = 1;
				bool ok = false;
				while (t+range  < n && !ok )
				{
					if (a[t+range] <= i)
					{
						for (int j = t+range; j > i; j --)
						{
							swap(a[j],a[j-1]);
							ans ++;
						}
						ok = true;
					}
					else
						range ++;
				}
			}

		cout << "Case #"<<k<<": "<<ans << endl;
	}


	return 0;
}
