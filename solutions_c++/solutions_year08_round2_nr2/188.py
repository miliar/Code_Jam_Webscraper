#include <iostream>
#include <fstream>
#include <cmath>
#include <vector>
#include <cstdio>



using namespace std;



int pr[80000];
int mp[1010];


int pn;

long long p, a, b;


void CalcP()
{
	pn = 1;
	pr[0] = 2;
	int i, j, f;
	for (i = 3; i < 1000000; i += 2)
	{
		if (i % 10000 == 1) cerr << i << "\n";
		f = 0;
		for (j = 1; j < pn; j++)
		{
			if (i % pr[j] == 0)
			{
				f = 1;
				break;
			}
		}
		if (f == 0)
		{
			pr[pn] = i;
			pn++;
		}
	}
	cerr << "primes : " << pn << "\n";
}



void Load()
{
	cin >> a >> b >> p;
}



int root[80000];

int rt(int i)
{
	if (root[i] != i) root[i] = rt(root[i]);
	return root[i];
}


int gcd(int a, int b)
{
	if (a > b) return gcd(b, a);
	else if (a == 0) return b;
	else return gcd(b % a, a);

}

void Solve()
{
	int i, j, k;
	for (i = a; i <=b; i++)
	{
		root[i] = i;
	}

	for (i = 1; i < 1000; i++)
	{
		k = i;
		j = 2;
		while (j <= k)
		{
		    mp[i] = j;
		    while (k % j == 0)
		    	k /= j;
			j++;
		}
	}

	for (i = a; i <=b; i++)
	{
		for (j = i+1; j <= b; j++)
		{
			if (mp[gcd(i,j)] >= p)
			{
				root[rt(i)] = rt(j);
			}
		}
	}
	int ans = 0;
    
    for (i = a; i <= b; i++)
    {
    	if (root[i] == i) ans++;
    }
    cout << ans;
}


int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int nt, tt;

	cin >> nt;

	//CalcP();

	for (tt = 1; tt <= nt; tt++)
	{
    	Load();
    	cout << "Case #" << tt << ": ";
    	Solve();
    	cout << "\n";
    }
	return 0;
}