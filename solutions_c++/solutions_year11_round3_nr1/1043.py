#include <iostream>
#include <vector>
#include <string>

using namespace std;

int
main()
{
	freopen("A-large.IN", "r", stdin);
	freopen("1234567.txt", "w", stdout);
	int t;
	cin >> t;
	for(int p = 0; p < t; ++p)
	{
		int n, m;
		cin >> n >> m;
		bool f = true;
		vector <vector <char> > a(n, vector <char>(m));
		
		vector <vector <char> > ans(n, vector <char>(m,'.'));

		vector <vector <int> >b(n, vector<int>(m, -1));

		for(int i = 0; i < n; ++i)
		{
			for(int j = 0; j < m; ++j)
			{
				cin >> a[i][j];
			}
		}
		for(int i = 0; i < n; ++i)
		{
			int sum = 0;
			for(int j = 0; j < m; ++j)
			{
				if(a[i][j] == '#')
				{
					++sum;
				}
			}
			if(sum % 2 != 0)
			{
				f = false;
				break;
			}
		}
		if(f == false)
		{
			cout << "Case #" << p + 1 << ':' << endl;
			cout << "Impossible" << endl;
			continue;
		}
		for(int j = 0; j < m; ++j)
		{
			int sum = 0;
			for(int i = 0; i < n; ++i)
			{
				if(a[i][j] == '#')
				{
					++sum;
				}
			}
			if(sum % 2 != 0)
			{
				f = false;
				break;
			}
		}
		if(f == false)
		{
			cout << "Case #" << p + 1 << ':' << endl;
			cout << "Impossible" << endl;
			continue;
		}
		for(int i = 0; i < n; ++i)
		{
			bool q = true;
			for(int j = 0; j < m; ++j)
			{
				if(a[i][j] =='#')
				{
					if(b[i][j] == -1 )
					{
						if(q == true)
						{
							ans[i][j] = '/';
							q = false;
							if(i == n - 1)
							{
								f = false;
								break;
							}
							b[i + 1][j] = 1;
						}
						else
						{
							ans[i][j] = '\\';
							q = true;
							if(i == n - 1)
							{
								f = false;
								break;
							}
							b[i + 1][j] = 2;
						}
					}
					else
					{
						if(b[i][j] == 1)
						{
							ans[i][j] = '\\';
						}
						if(b[i][j] == 2)
						{
							ans[i][j] = '/';
						}
					}
				}
			}
					
		}
		if(f == false)
		{
			cout << "Case #" << p + 1 << ':' << endl;
			cout << "Impossible" << endl;
			continue;
		}
		cout << "Case #" << p + 1 << ':' << endl;
		for(int i = 0; i < n; ++i)
		{
			for(int j = 0; j < m; ++j)
			{
				cout << ans[i][j];
			}
			cout << endl;
		}

	}

}
