#include<iostream>
#include<string>

using namespace std;

struct h
{
	int a[100];
};

h t[2000];

void get(h &x)
{
	for (int i = 0; i < 100; i++) x.a[i] = 0;
	char c;
	while (1 == 1)
	{
		c = getchar();
		if ((c == ' ') || (c == '\n') || (c - '0' > 9) || (c < '0')) break;
		x.a[0]++;
		x.a[x.a[0]] = c - '0';
	}
	for (int i = 1; i <= x.a[0] / 2; i++)
	{
		int t = x.a[i];
		x.a[i] = x.a[x.a[0] + 1 - i];
		x.a[x.a[0] + 1 - i] = t;
	}
}


void print(h x)
{
	for (int i = x.a[0]; i > 0; i--) cout << x.a[i];
}
bool bigger(h x,h y)
{
	if (x.a[0] > y.a[0]) return true;
	if (x.a[0] < y.a[0]) return false;
	for (int i = x.a[0]; i > 0; i--)
	{
		if (x.a[i] > y.a[i]) return true;
		if (x.a[i] < y.a[i]) return false;
	}
	return true;
}

h minu(h x,h y)
{
	h z;
	for (int i = 0; i < 100; i++) z.a[i] = 0;
	z.a[0] = x.a[0];
	for (int i = 1; i <= z.a[0]; i++)
	{
		z.a[i] = x.a[i] - y.a[i];
		if (z.a[i] < 0)
		{
			z.a[i] += 10;
			x.a[i + 1]--;
		}
	}
	while ((z.a[z.a[0]] == 0) && (z.a[0] != 1)) z.a[0]--;
	return z;
}


h mod(h x,h y)
{
	h s;
	for (int i = 0; i < 100; i++) s.a[i] = 0;
	s.a[0] = 1;
	for (int i = x.a[0]; i > 0; i--)
	{
		if ((s.a[0] != 1) || (s.a[1] != 0)) s.a[0]++;
		for (int j = 60; j > 0; j--) s.a[j + 1] = s.a[j];
		s.a[1] = x.a[i];
		while (bigger(s,y)) 
		{
			
		s = minu(s,y);
	}
	}	
	return s;
}

h gcd(h x,h y)
{
	h r;
	r = mod(x,y);
	if ((r.a[0] == 1) && (r.a[1] == 0)) return y; else return gcd(y,r);
}

int main()
{
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	int c;
	cin >> c;
	int tt = 0;
	while (c > 0)
	{
		c--;
		tt++;
		int n;
		cin >> n;
		char cc;
		cc = getchar();
		for (int i = 0; i < n; i++) get(t[i]);
		h s;
	    if (bigger(t[0],t[1])) s = minu(t[0],t[1]); else s = minu(t[1],t[0]);
	    for (int i = 1; i < n - 1; i++)
	    {
			h ss;
			if (bigger(t[i],t[i + 1])) ss = minu(t[i],t[i + 1]); else ss = minu(t[i + 1],t[i]);
			if ((ss.a[1] != 0) || (ss.a[0] != 1)) s = gcd(s,ss);
		}
		h one;
		for (int i = 0; i < 100; i++) one.a[i] = 0;
		one.a[0] = 1;
		one.a[1] = 1;
		t[0] = mod(t[0],s);
		t[0] = minu(s,t[0]);
		t[0] = mod(t[0],s);
		cout << "Case #" << tt << ": ";
		print(t[0]);
		cout << "\n";
	}
}
