#define _CRT_SECURE_NO_WARNINGS
#include "stdio.h"
#include <cmath>
#include <cassert>
#include "iostream"
#include "sstream"
#include "string"
#include "algorithm"
#include "vector"
#include "queue"
#include "map"

using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;

#define all(s) s.begin(), s.end()

const int INF = 1000000000;



int main ()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);


	int test_count;
	cin >> test_count;



	for (int test = 0; test < test_count ; test++)
	{
		fprintf(stderr, "%d\n", test);

		string s;
//		getline(cin, s);
//		cin >> s;

		int n;
		cin >> n;
		vvi a(n, vi(n, 0));

		for (int i = 0; i < n ; i++)
		{
			for (int j = 0; j < n ; j++)
			{
				char c;
				cin >> c;
				a[i][j] = c - '0';
			}
		}
		
		int res = 0;
		for (int i = 0; i < n ; i++)
		{
			int c = 0;
			for (int j = i + 1; j < n ; j++)
			{
				c += a[i][j];
			}

			int swap_i;
			if (c)
			{
				for (int j = i + 1; j < n ; j++)
				{
					int c1 = 0;
					for (int k = i + 1; k < n ; k++)
					{
						c1 += a[j][k];
					}

					if (!c1)
					{
						swap_i = j;
						break;
					}
				}

				
				for (int j = swap_i - 1; j >= i ; j--)
				{
					swap(a[j], a[j+1]);
					res++;
				}
					
				
				//res += swap_i - i;
			}
		}

		printf("Case #%d: %d\n", test + 1, res);
	}

}