#include <iostream>
#include <cstdio>
using namespace std;

const int maxn = 111111;

int TEST;
int n, m, x;
int LEFT[maxn], RIGHT[maxn];
double X[maxn], ans;
string name[maxn];
string a[maxn];
string s;

int rec(int k)
{
	char c;
	cin >> c >> ::X[k] >> s;

	if (s != ")")
	{
		::name[k] = s;
		::LEFT[k] = n + 1;
		::RIGHT[k] = n + 2;
		n += 2;
		rec(::LEFT[k]);
		rec(::RIGHT[k]);
		cin >> c;
	} else
	{
		::LEFT[k] = 0;
		::RIGHT[k] = 0;
	}


	return 0;
}

int main()
{
	freopen(".in","r",stdin);
	freopen(".out","w",stdout);
	scanf("%d\n", &TEST);
	for (int test = 0; test < TEST; test++)
	{
		printf("Case #%d:\n", test + 1);

		scanf("%d\n", &n);
		n = 0;
		rec(0);

		cin >> m;
		while (m--)
		{
			ans = 1;
			cin >> s >> n;
			for (int i = 0; i < n; i++) cin >> a[i];

			x = 0;
			while (LEFT[x])
			{
				bool fRIGHT = true;
				for (int i = 0; i < n; i++) if (name[x] == a[i])
				{
					fRIGHT = false;
					break;
				}
				ans *= X[x];
				if (fRIGHT)
					x = RIGHT[x]; else
					x = LEFT[x];
			}
			ans *= X[x];
			printf("%.7lf\n", ans);
		}
	}
	
	return 0;
}
