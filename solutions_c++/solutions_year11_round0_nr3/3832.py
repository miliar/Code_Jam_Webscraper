#include <iostream>
#include <fstream>
using namespace std;
bool used[16];
int num[16];
int n;
int Max = -1;
void add()
{
	int a = 0;
	int suma = 0;
	int b = 0;
	int sumb = 0;
	int i;
	for (i = 0;i < n;i++)
	{
		if (used[i])
		{
			suma += num[i];
			a = a ^ num[i];
		}
		else
		{
			sumb += num[i];
			b = b ^ num[i];
		}
	}
	if (suma > 0 && sumb > 0 && a == b)
	{
		if (suma > Max)
			Max = suma;
		if (sumb > Max)
			Max = sumb;
	}
}

void enumerate(int k)
{
	if (k == n)
	{
		add();
		return;
	}

	used[k] = true;
	enumerate(k+1);

	used[k] = false;
	enumerate(k+1);
}

int main()
{
	int t;
	cin >> t;
	int k;
	int i;
	ofstream outf;
	outf.open("3.out",ios::out);
	for (k = 1;k <= t;k++)
	{
		Max = -1;
		cin >> n;
		for (i = 0;i < n;i++)
			cin >> num[i];
		enumerate(0);
		outf <<"Case #"<<k<<": ";
		if (Max != -1)
			outf << Max << endl;
		else
			outf << "NO" << endl;
	}
	return 0;
}