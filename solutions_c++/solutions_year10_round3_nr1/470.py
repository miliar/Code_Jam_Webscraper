#include <iostream>
#include <fstream>
using namespace std;

#define  N 1010
int a[N][2];

int t, n, x, y;

ifstream fin("A-large.in");
ofstream fout("o.txt");


#define cin  fin
#define cout fout

void input()
{
	int i = 0;
	cin >> n;
	while (i < n)
	{
		cin >> a[i][0] >> a[i][1];
		i ++;
	}
	
}
void t2()
{
	int i;
	for (i = 0; i < n ; i ++)
	{
		cout << a[i][0] << ' ' << a[i][1] << endl;
	}

}
void sort()
{
	int i, j;
	int k;
	for (i = 0; i < n; i ++)
	{
		k = i;
		for (j = i + 1; j < n; j ++)
		{
			if (a[j][0] < a[k][0])
			{
				k = j;
			}
			else if(a[j][0] == a[k][0] && a[j][1] < a[k][1])
			{
				k = j;
			}
		}
		if (k != i)
		{
			swap(a[i][0], a[k][0]);
			swap(a[i][1], a[k][1]);
		}
	}
	//t2();
}
int solove()
{
	int i, j;
	int sum = 0;
	for (i = 0; i < n; i ++)
	{
		for (j = i + 1; j < n; j ++)
		{
			if (a[j][1] < a[i][1])
			{
				sum ++;
			}
		}
	}
	return sum;
}
void out(int icase, int res)
{
	cout << "Case #" << (icase + 1) << ": " << res << endl;
}

int main()
{
	int icase = 0;
	int sum;
	cin >> t;
	while (icase < t)
	{
		input();
		sort();
		sum = solove();
		out(icase, sum);
		icase ++;
	}
	return 0;
}