#include <iostream>
#include <fstream>
#include <cmath>
#include <vector>
#include <cstdio>



using namespace std;

int k;
string s;
string s2;
int bst;

void Load()
{
	cin >> k;
	cin >> s;
	s2.resize(s.size());
}

int p[10];


void Test()
{
	int i, j;

	j = 0;
	for (i = 0; i < s.size(); i++)
	{
		s2[i] = s[k * (i / k) + p[i % k + 1] - 1];
		if (i == 0 || s2[i] != s2[i-1]) j++;
	}
	if (j < bst) bst = j;
}

void Solve()
{
	int i, j, t;
	bst = s.size();
	for (i = 1; i <= k; i++)
		p[i] = i;

	int f = 1;

	do
	{
		Test();
		
		i = k;
		while (i > 1 && p[i] < p[i-1]) i--;
		if (i == 1) f = 0;


		if (f == 0) break;
		j = i;
		for (t = i+1; t <= k; t++)
		{
			if (p[t] > p[i-1] && p[j] > p[t]) j = t;
		}

		t = p[j];
		p[j] = p[i-1];
		p[i-1] = t;

		j = k;
		while (i < j)
		{
			t = p[i]; p[i] = p[j]; p[j] = t;
			i++; j--;
		}
		
		
	}
	while(f);
	cout << bst << "\n";
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
    	cout << "Case #" << tt << ": ";
    	Solve();
    }
	return 0;
}