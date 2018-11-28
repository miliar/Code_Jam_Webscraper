#define  _CRT_SECURE_NO_DEPRECATE
#include<iostream>
#include<string>
#include<sstream>
#include<vector>
#include<algorithm>
#include<queue>
#include<map>
#include<time.h>
#include<numeric>
#include<set>
#include<stack>
#include<deque>
#include<math.h>
#define epsilon 0.000000001
using namespace std;


int main()
{
	freopen("google.in", "r", stdin);
	freopen("google.out", "w", stdout);
	int numtests;
	cin >> numtests;
	
	for(int o = 0; o < numtests; o++)
	{
		printf("Case #%d: ", o + 1);
		int n;
		long long a, b, c, d, x0, y0, m;
		cin >> n;
		cin >> a >> b >> c >> d >> x0 >> y0 >> m;
		vector<pair<int, int> > points(n);
		points[0] = make_pair((int)x0, (int)y0);
		long long x = x0, y = y0;
		for(int i = 1; i < n; i++)
		{
			x = (a * x + b) % m;
			y = (c * y + d) % m;
			points[i] = make_pair((int)x, (int)y);
		}
		int mat[3][3];
		for(int i = 0 ; i < 3; i++)
			for(int j = 0; j < 3; j++)
				mat[i][j] = 0;
		for(int i = 0; i < n ;i++)
		{
			mat[points[i].first % 3][points[i].second % 3]++;
		}
		unsigned long long num = 0;
		int lim, lim2;
		long long coef, coef2;
		for(int i = 0; i < 3; i++)
			for(int j = 0; j < 3; j++)
			{
				if(mat[i][j] == 0)
					continue;
				coef = mat[i][j];
				coef2 = -1;
				for(int k = i; k < 3; k++)
				{
					if(k == i)
						lim = j;
					else
						lim = 0;
					for(int o =  lim; o < 3; o++)
					{
						if(k == i && j == o)
						{
							if(mat[k][o] > 1)
								coef2 = (coef * (coef - (unsigned long long)1)) / (unsigned long long) 2;
							else
								continue;
							//coef2 = coef;
						}
						else
							coef2 = mat[k][o];
						for(int p = k; p < 3; p++)
						{
							if(p == k)
								lim2 = o;
							else
								lim2 = 0;
							for(int q = lim2; q < 3; q++)
							{
								if((i + k + p) % 3 == 0 && (j + o + q) % 3 == 0)
								{
								if(p == i && q == j)
								{
									if(mat[i][j] > 2)
										num += (coef * (coef - (unsigned long long)1) * (coef - (unsigned long long)2)) / (unsigned long long) 6;
									else
										continue;
								}
								else
								{
									if(p == k && q == o)
									{
										if(mat[k][o] > 1)
											num += coef * (coef2 * (coef2 -(unsigned long long)1)) / (unsigned long long) 2;
										else
											continue;
									}
									else
									{
										if(k == i && o == j)
											num += coef2 * mat[p][q];
										else
											num += coef2 * coef * mat[p][q];
									}
								}
								}
								//if((i + k + p) % 3 == 0 && (j + o + q) % 3 == 0)
								//	num += a * b * mat[p][q];

							}
						}
					}
				}
			}
		cout << num << endl;
	}
	return 0;
}
