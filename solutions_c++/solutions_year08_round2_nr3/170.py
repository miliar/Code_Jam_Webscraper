#include <iostream>
#include <fstream>
#include <cmath>
#include <vector>
#include <cstdio>



using namespace std;


int k;
int n;
int d[200];
int a[5010];

int sz;




void Load()
{
	cin >> k;
	cin >> n;
	sz = 1;
	while (sz < k) sz *= 2;

	int i;
	for (i = 0; i < n; i++)
		cin >> d[i];
}



int min(int a, int b)
{
	if (a > b) return b;
	else return a;
}


int max(int a, int b)
{
	if (a < b) return b;
	else return a;
}



void Solve()
{
	int i = 0, l;
	memset(a, 0, sizeof(a));
	for (int j = 0; j < k; j++)
	{
		
		l = j;
		while (l > 0)
		{
			if (a[i] == 0) l--;
			i++;
			if (i == k) i = 0;
		}
		while (a[i] != 0)
		{
			i++;
			if (i == k) i = 0;
		}
		a[i] = j+1;
	}

	cerr << "end\n";

	for (i = 0; i < n; i++)
	{
		cout << " " << a[d[i]-1];
	}
}


int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int nt, tt;

	cin >> nt;

	for (tt = 1; tt <= nt; tt++)
	{
    	Load();
    	cout << "Case #" << tt << ":";
    	Solve();
    	cout << "\n";
    }
	return 0;
}