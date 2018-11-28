#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <vector>
#include <map>
#include <cmath>
#include <string>
#include <string.h>

#include <Windows.h>

using namespace std;


int st[9] = {1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000};

vector<int> sdv1(vector<int> mass)
{
	int len = mass.size();
	int rec = mass[len-1];
	for (int i = len-1; i > 0; i--)
		mass[i] = mass[i-1];
	mass[0] = rec;
	return mass;
}

int sdvig (vector<int> mass, int sdv)
{
	for (int i = 0; i < sdv; i++)
	{
		swap(mass[mass.size()-i-1], mass[i]);
	}
	return -1;
}

int main()
{
//#ifndef ONLINE_JUDGE
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
//#endif

	int n, a, b, s, p, i, j, k, z1, z2, t;
	long long ans = 0;
	vector<int> v;

	//t=50;
	cin >> t;
	for (int ti = 0; ti < t; ti++)
	{
		//a=1; b=2e6;
		cin >> a >> b;
		ans = 0;
		
		//int time = GetTickCount();

		/*for (int i =a; i <= b; i++)
		{
			vector<int> num;
			int rnum = i;
			while (rnum / 10 != 0)
			{
				num.push_back( rnum % 10);
				rnum /= 10;
			}
			num.push_back( rnum % 10);
			reverse(num.begin(), num.end());
		}*/
		
				
		for (i = a; i < b; i++)
		{
			map<int, bool> mp;

			//for (j = i+1; j <=b; j++)
			{
				vector<int> num;
				int rnum = i;
				while (rnum / 10 != 0)
				{
					num.push_back( rnum % 10);
					rnum /= 10;
				}
				num.push_back( rnum % 10);
				reverse(num.begin(), num.end());

				n = num.size();
				
				int c = 0;
				bool found = false; 
				while (true)
				{
					num = sdv1(num);

					int val = 0;
					for ( k =0; k < n; k++)
						val += num[k] * st[n-k-1];

					if (val > i && val <= b)
					{
						//ans++;
						//mp[make_pair(i, val)] = true;
						mp[val] = true;
					}

					c++;
					if (c+1 < n)
						;
					else
						break;
				}
				
			}
			ans += mp.size();
		}

		cout << "Case #" << ti+1 <<": " << ans << endl;
		//cout << "Case #" << ti+1 <<": " << ans << " " << GetTickCount() - time << endl;
		//time = GetTickCount();
	}

	return 0;
}