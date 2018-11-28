#include <iostream>
#include <cmath>
#include <cstring>

using namespace std;

int testNum = 0;
int n;
char result[1000];
int resSize;
int comb[50][50];
bool gmp[50][50];
char input[1000];
int inputS;

void read()
{
	resSize = 0;
	int count3;
	char c1, c2, c3;
	cin >> count3;
	int i, j;
	for (i = 0; i < 50; ++i)
		for (j = 0; j < 50; ++j)
		{
			comb[i][j] = 0;
			gmp[i][j] = false;
		}
	for (i=0; i < count3; ++i)
	{
		do
		{
			cin >> c1;
		}while (c1 == ' ');
		do
		{
			cin >> c2;
		}while (c2 == ' ');
		do
		{
			cin >> c3;
		}while (c3 == ' ');
		comb[c1-'A' + 1][c2-'A' + 1] = c3-'A' + 1;
		comb[c2-'A' + 1][c1-'A' + 1] = c3-'A' + 1;
	}
	int gmpq;
	cin >> gmpq;
	for (i=0; i < gmpq; ++i)
	{
		do
		{
			cin >> c1;
		}while (c1 == ' ');
		do
		{
			cin >> c2;
		}while (c2 == ' ');
		gmp[c2-'A' + 1][c1-'A' + 1] = true;
		gmp[c1-'A' + 1][c2-'A' + 1] = true;
	}
	cin >> inputS;
	for (i = 1; i <= inputS; ++i)
	{
		do
		{
			cin >> input[i];
		}while(input[i]==' ');
	}
}

void printOut()
{
	cout << "Case #" << testNum << ": [";
	int i;
	for (i = 1; i < resSize; ++i)
		cout << result[i] << ", ";
	if (resSize > 0)
		cout << result[resSize];
	cout << "]\n";
}
void solve()
{
	read();
	int i, j;
	for (i = 1; i <= inputS; ++i)
	{
		++resSize;
		result[resSize] = input[i];
		while ( (resSize != 1) && (comb[result[resSize] - 'A' + 1][result[resSize - 1] - 'A' + 1] != 0))
		{
			result[resSize - 1] = comb[result[resSize] - 'A' + 1][result[resSize - 1] - 'A' + 1] - 1 + 'A';
			--resSize;
		}//Combinations

		for (j = 1; j < resSize; ++j)
			if (gmp[result[j] - 'A' + 1][result[resSize] - 'A' + 1])
			{
				resSize = 0;
				break ;
			}
	}
	printOut();
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	while(t)
	{
		++testNum;
		solve();
		--t;
	}
return 0;
}