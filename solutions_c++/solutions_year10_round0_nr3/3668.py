#include<iostream>
#include<fstream>
using namespace std;

ifstream fin("C-small-attempt0.in");
//ifstream fin("A-large-practice.in");
ofstream fout("1.out");
#define cin fin
#define cout fout

#define N 1010 
int a[N];
int main()
{
	int tcase;
	cin >> tcase;
	int icase = 1;
	int i, j;
	int R, k, n;
	int r;
	int sum_cur, sum;
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
		r = 0;
		i = 0;
		while (r < R)
		{
			sum_cur = 0;
			j = 0;
			while(sum_cur  + a[i] <= k && j < n)
			{
				sum_cur += a[i];
				i ++;
				i %= n;
				j ++;
			}
			sum += sum_cur;
			r ++;
		}
		cout << sum << endl;
		icase ++;
	}
	return 0;
}

