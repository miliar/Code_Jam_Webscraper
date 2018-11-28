#include<iostream>
#include<fstream>
using namespace std;

ifstream fin("C-large.in");
ofstream fout("1.out");
#define cin fin
#define cout fout

#define N 1010 
__int64 a[N], b[N];
int c[N];
int main()
{
	int tcase;
	cin >> tcase;
	int icase = 1;
	int i, j;
	int R, k, n;
	int r;
	__int64 sum_cur, sum;
	while (icase <= tcase)
	{
		cout << "Case #" << icase << ": ";
		cin >> R >> k >> n;
		i = 0;
		while (i < n)
		{
			cin >> a[i];
			i ++;
		}
		sum = sum_cur = 0;
		int ii;
		for(i = 0; i < n; i ++)
		{
			if (i == 0)
			{
				sum_cur = 0; 
				j = 0; 
				ii = 0;
			}
			else
			{
				sum_cur = b[i-1] - a[i-1];
				j = c[i - 1] - 1; 
				ii = i + c[i -1] - 1;
				ii %= n;
			}
			while(sum_cur  + a[ii] <= k && j < n)
			{
				sum_cur += a[ii];
				ii ++;
				ii %= n;
				j ++;
			}
			b[i] = sum_cur;
			c[i] = j;
		}

		r = 0;
		i = 0;
		while (r < R)
		{
			sum += b[i];
			i += c[i];
			i %= n;
			r ++;
		}
		cout << sum << endl;
		icase ++;
	}
	return 0;
}

