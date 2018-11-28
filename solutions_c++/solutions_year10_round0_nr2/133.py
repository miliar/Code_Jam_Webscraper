#include<iostream>
#include<fstream>
using namespace std;

ifstream fin("1.in");
ofstream fout("1.out");
#define cin fin
#define cout fout

const int  N = 1010;
int a[N];

int gcd(int a, int b)
{
	if (a < b)
	{
		swap(a, b);
	}
	if (b == 0)
	{
		return a;
	}
	else
	{
		return gcd(b, a%b);
	}
}

int main()
{
	int tcase;
	cin >> tcase;
	int icase = 1;
	int n;
	int i;
	while (icase <= tcase)
	{
		cout << "Case #" << icase << ": ";
		cin >> n;	
		i = 0;
		cin >> a[i];
		i ++;
		while (i < n)
		{
			cin >> a[i];
			a[i] -= a[0];
			if (a[i] < 0)
			{
				a[i] = -a[i];
			}
			i ++;
		}

		int cm = a[1];
		for (i = 2; i < n; i ++)
		{
			cm = gcd(cm, a[i]);
		}
		int res = a[0] / cm * cm;

		if (res < a[0])
		{
			res += cm ;
		}
		res = res -= a[0];
		cout << res  << endl;
		icase ++;
	}
	return 0;
}
