#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <string>
#include <map>
#include <set>

using namespace std;

long long l,d,n;
char mas[5001][20];
int id[5001];
int last;


int main()
{
	freopen("readme.txt","r",stdin);
	freopen("output.txt","w",stdout);

	cin >> l >> d >> n;

	for (int i = 0; i < d; ++ i)
	{
		cin >> mas[i];
		id[i] = i;
	}


	char c;
	long long mask;
	for (int i = 0; i < n; ++ i)
	{
		last = d;
		for (int k = 0; k < l; ++ k)
		{
			mask = 0;
			cin >> c;
			if (c == '(')
			{
				cin >> c;
				while (c != ')')
				{
					mask |= (1 << (c - 'a'));
					cin >> c;
				}
			}
			else mask |= (1 << (c - 'a'));

			for (int j = 0; j < last; ++ j)
			{
				if (!(mask & (1 << (mas[id[j]][k] - 'a'))))
				{
					swap(id[j], id[-- last]);
					-- j;
				}
			}
		}
		cout << "Case #" << (i+1) << ": " << last << endl;
	}

	return 0;
}