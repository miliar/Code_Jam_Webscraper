#include <iostream>
#include <cmath>
#include <cstring>

using namespace std;

int testNum = 0;
int n;
int result;
int input[10000];
int noOneInPlace[10000];
int xor;
int minimal;

void read()
{
	result = -1;//MAGIC NUMBER
	int i;
	cin >> n;
	for (i = 1; i <= n; ++i)
		cin >> input[i];
}

void printOut()
{
	cout << "Case #" << testNum << ": ";
	if (result == -1)
	{
		cout << "NO\n";
	}
	else
		cout << result << "\n";
}
void calcRealN()
{
	int i;
	int N = 0;
	for (i=1;i <= n; ++i)
		if (input[i] == i)
			++N;
	n = N;
}
void createNoOneArray()
{
	noOneInPlace[1] = 0;
	noOneInPlace[2] = 1;
	int i,j,k;
//	for (i = 3; i <= 1000; ++i)

}

void solve()
{
	read();
	//calcRealN();
	//createNoOneArray();
	result = 0;
	xor = 0;
	minimal = 100000000;
	int i;
	for (i = 1; i <= n; ++i)
	{
		result += input[i];
		xor ^= input[i];
		if (input[i] < minimal)
			minimal = input[i];
	}
	if (xor != 0)
		result = -1;
	else
		result -= minimal;
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