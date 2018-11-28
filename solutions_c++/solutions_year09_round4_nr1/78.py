#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
#include <vector>


using namespace std;

ifstream fin("A-large.in");
ofstream fout("A-large.out");

#define cin fin
#define cout fout

int n;
char map[50][50];
int ans;

void work()
{
	int c[50];

	memset(c, 0, sizeof(c));
	for (int i = 0; i < n; i++)
	{
		for (int j = n-1; j >= 0; j--)
			if (map[i][j] == '1') 
			{
				c[i] = j;		
				break;
			}
	}

	ans = 0;
	for (int i = 0; i < n; i++)
	{
		for (int j = i; j < n; j++)
			if (c[j] <= i)
			{
				int h = c[j];

				for (int k = j; k > i; k--)
					c[k] = c[k-1];
				c[i] = h;

				ans += j-i;
				break;
			}
	}
}

int main()
{
	int cases;
	cin >> cases;

	for (int i = 1; i <= cases; i++)
	{
		cin >> n;
		for (int j = 0; j < n; j++)
			cin >> map[j];

		work();

		cout << "Case #" << i << ": " << ans << endl;


	}

	return 0;
}