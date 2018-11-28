#include <stdio.h>
#include <fstream>
#include <iostream>
#include <vector>
#include <string>
#include <list>
#include <set>
#include <map>
#include <algorithm>
#include <math.h>
#include <iomanip>

using namespace std;

typedef long long ll;



//bool myf(mark a, mark b)
//{
//	return ((a.z > b.z)||((a.z == b.z)&&(a.pos < b.pos)));
//}

ll n, i, j, t, p, bp, m, k, a[55][55];
char c;
bool can;

int main()
{
	#ifndef ONLINE_JUDGE
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
	#endif
	cin >> t;
	for(j = 1; j <= t; j++)
	{
		can = 1;
		cin >> n >> m;
		for(i = 0; i < 55; i++)
			for(p = 0; p < 55; p++)
				a[i][p] = 0;
		for(i = 1; i <= n; i++)
			for(p = 1; p <= m; p++)
			{
				cin >> c;
				if(c == '#')
					a[i][p] = -1;
			}

		for(i = 1; i <= n; i++)
			for(p = 1; p <= m; p++)
				if(a[i][p] == -1)
				{
					if((a[i][p+1] == -1)
					&&(a[i+1][p+1] == -1)
					&&(a[i+1][p] == -1))
					{
						a[i][p] = 1;
						a[i+1][p+1] = 1;
						a[i][p+1] = 2;
						a[i+1][p] = 2;
					}
					else
						can = 0;

				}


		cout << "Case #" << j << ":" << endl;
		if(can == 0)
			cout << "Impossible"<<endl;
		else
		{
			for(i = 1; i <= n; i++)
			{
				for(p = 1; p <= m; p++)
					if(a[i][p] == 1)
						cout << '/';
					else
						if(a[i][p] == 2)
							cout << '\\';
						else
						cout << '.';
				cout << endl;

			}
						
		}
	}
		
	return 0;
}