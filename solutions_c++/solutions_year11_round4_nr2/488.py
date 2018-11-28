#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <cstdio>

using namespace std;

char buffer[1024];
long long R, C, D;
long long data[520][520];
long long int_data[520][520];
long long int_c_data[520][520];
long long int_r_data[520][520];

void calc_int_data()
{
	for(int r = 0; r < R; r++)
	{
		int_data[r][0] = 0;
		int_c_data[r][0] = 0;
		int_r_data[r][0] = 0;
	}

	for(int c = 0; c < C; c++)
	{
		int_data[0][c] = 0;
		int_c_data[0][c] = 0;
		int_r_data[0][c] = 0;
	}

	for(int r = 1; r <= R; r++)
		for(int c = 1; c <= C; c++)
		{
			int_data[r][c] = int_data[r - 1][c] + int_data[r][c - 1] - int_data[r - 1][c - 1] + data[r-1][c-1];
			int_c_data[r][c] = int_c_data[r - 1][c] + int_c_data[r][c - 1] - int_c_data[r - 1][c - 1] + data[r-1][c-1] * (c-1) * 2;
			int_r_data[r][c] = int_r_data[r - 1][c] + int_r_data[r][c - 1] - int_r_data[r - 1][c - 1] + data[r-1][c-1] * (r-1) * 2;
		}
}

struct cPoint
{
	int r, c;
	bool integer;
};

long long find_int_sum(long long (*int_data)[520], int r, int c, int k)
{
	long long res = 0;

	res += int_data[r + k][c + k];
	res += int_data[r][c];
	res -= int_data[r + k][c];
	res -= int_data[r][c + k];

	return res;
}

cPoint find_c_point(int r, int c, int k)
{
	long long sum = find_int_sum(int_data, r, c, k) - data[r][c] - data[r + k - 1][c] - data[r + k - 1][c + k - 1] - data[r][c + k - 1];
	long long sumC = find_int_sum(int_c_data, r, c, k) - data[r][c] * c * 2 - data[r + k - 1][c] * c * 2 - data[r + k - 1][c + k - 1] * (c + k - 1) * 2 - data[r][c + k - 1] * (c + k - 1) * 2;
	long long sumR = find_int_sum(int_r_data, r, c, k) - data[r][c] * r * 2 - data[r + k - 1][c] * (r + k - 1) * 2 - data[r + k - 1][c + k - 1] * (r + k - 1) * 2 - data[r][c + k - 1] * r * 2;

	cPoint res;

	if (sumC % sum != 0
		|| sumR % sum != 0)
	{
		res.integer = false;
	}
	else
	{
		res.integer = true;
	}

	res.c = int(sumC / sum);
	res.r = int(sumR / sum);

	/*if (res.integer)
	{
		cout << sum << " " << sumC << " " << sumR << endl;
	}*/

	return res;
}

void solve_case(int caseNumber)
{
	cin >> R >> C >> D;

	gets(buffer);

	for(int r = 0; r < R; r++)
	{
		gets(buffer);

		for(int c = 0; c < C; c++)
		{
			data[r][c] = D + buffer[c] - '0';
		}
	}

	calc_int_data();
	
	for(int k = min(R, C); k >= 3; k--)
		for(int r = 0; r < R - k + 1; r++)
			for(int c = 0; c < C - k + 1; c++)
			{
				cPoint cMass = find_c_point(r, c, k);

				if (cMass.integer
					&& r * 2 + k - 1 == cMass.r
					&& c * 2 + k - 1 == cMass.c)
				{
					//cout << r << " " << c << endl;
					cout << "Case #" << caseNumber << ": " << k << endl;

					return;
				}
			}

	cout << "Case #" << caseNumber << ": IMPOSSIBLE" << endl;
}

int main()
{
	int T;

	cin >> T;

	for(int i = 0; i < T; i++)
		solve_case(i + 1);

	return 0;
}