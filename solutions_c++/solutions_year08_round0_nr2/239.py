#include <iostream>
#include <string>
#include <cstdio>
#include <vector>

using namespace std;


int t;
int na, nb;
vector < pair <int, int> > ev;
//0 - new in a
//1 - new in b
//10 - need in a
//11 - need in b


int gettime()
{
	char c1, c2;
	int i, j;
	cin >> c1 >> c2;
	cerr << c1 << c2;
	i = (int)c1 - (int)'0';
	i *= 10;
	i += (int)c2 - (int)'0';
	j = i * 60;
	cin >> c1;
	cerr << c1;
	cin >> c1 >> c2;
	cerr << c1 << c2;
	i = (int)c1 - (int)'0';
	i *= 10;
	i += (int)c2 - (int)'0';
	j += i;
	cerr << " ";
	return j;
}

void Load()
{
	cin >> t;
	cin >> na >> nb;
	int i, x, y;

	ev.clear();

	for (i = 0; i < na; i++)
	{
		x = gettime();
		y = gettime();
		ev.push_back(make_pair(x, 10));
		ev.push_back(make_pair(y+t, 1));
	}
	for (i = 0; i < nb; i++)
	{
		x = gettime();
		y = gettime();
		ev.push_back(make_pair(x, 11));
		ev.push_back(make_pair(y+t, 0));
	}
	sort(ev.begin(), ev.end());
}

void Solve()
{
	int a, b;
	int ca, cb;
	a = b = 0;
	ca = cb = 0;
	unsigned int i;
	int j;
	for (i = 0; i < ev.size(); i++)
	{
		j = ev[i].second;
		if (j == 0)
			ca++;
		else if (j == 1)
			cb++;
	   	else if (j == 10)
	   	{
			if (ca == 0)
			{
				ca++;
				a++;
			}
			ca--;
		}
		else if (j == 11)
		{
			if (cb == 0)
			{
				cb++;
				b++;
			}
			cb--;
		}
	}
	cout << a << " " << b << "\n";
}

int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int nt;
	cin >> nt;
	for (int tt = 1; tt <= nt; tt++)
	{
//		cerr << "testcase " << tt << "\n";
//		cerr << "-------------------\n";
		cout << "Case #" << tt << ": ";
		Load();
		Solve();
	}
	return 0;
	
}