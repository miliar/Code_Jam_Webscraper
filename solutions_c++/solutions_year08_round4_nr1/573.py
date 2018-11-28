#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

#define SZ(a) (int)(a).size()
#define For(i, a, b) for(int i=(a); i<(b); ++i)

typedef long long ll;

int m, v;
int a[100001], b[100001], c[100001];

void Calc(int nom)
{
	if (nom>(m-1)/2) return;
	Calc(2*nom+1); Calc(2*nom);
	if (b[nom]==1)
		a[nom]=a[2*nom+1]&a[2*nom];
	else a[nom]=a[2*nom+1]|a[2*nom];
}

int Change(int nom, int val)
{
	if (a[nom]==val)
		return 0;
	if (nom>(m-1)/2)
		return 1000000;

	if (val==0 && b[nom]==1)
	{
		return min(Change(2*nom, 0), Change(2*nom+1, 0));
	}
	if (val==1 && b[nom]==0)
	{
		return min(Change(2*nom, 1), Change(2*nom+1, 1));
	}
	if (c[nom]==1)
	{
		c[nom]=0;
		if (val==0)
		{
			b[nom]=1; Calc(nom); int t1=Change(nom, val)+1;
			if (t1>=1000000) { b[nom]=0; c[nom]=0; Calc(nom); } else return t1;
		}
		if (val==1)
		{
			b[nom]=0; Calc(nom); int t1=Change(nom, val)+1;
			if (t1>=1000000) { b[nom]=1; c[nom]=0; Calc(nom); } else return t1;
		}
	}
	if (b[nom]==1)
	{
		return min(Change(2*nom, 1)+Change(2*nom+1, 1), 1000000);
	}
	if (b[nom]==0)
	{
		return min(Change(2*nom, 0)+Change(2*nom+1, 0), 1000000);
	}
}

void main()
{
	int tc;
	cin >> tc;
	For(_case, 1, tc+1)
	{
		cin >> m >> v;
		memset(a, 0, sizeof(a));
		memset(b, 0, sizeof(b));
		memset(c, 0, sizeof(c));
		For(i, 1, (m-1)/2+1)
		{
			cin >> b[i] >> c[i];
		}
		For(i, (m-1)/2+1, m+1)
			cin >> a[i];

		Calc(1);
		int res=Change(1, v);
		cout << "Case #" << _case << ": ";
		if (res<1000000)
			cout << res << endl;
		else
			cout << "IMPOSSIBLE" << endl;
	}
}