#include <fstream>
#include <cstring>
#include <vector>

using namespace std;

ifstream cin("data.in");
ofstream cout("data.out");

typedef struct{int p, q;} time;

int na, nb;
int tt[2];
int t;
vector<time> a, b;
vector<bool> fa, fb;


void init()
{
	cin >> t;
	cin >> na >> nb;
	a.clear();
	b.clear();
	fa.clear();
	fb.clear();
	for (int i = 0; i < na; i++)
	{
		int x, y; char z;
		cin >> x >> z >> y;
		int xx = x*60+y;
		cin >> x >> z >> y;
		int yy = x*60+y;
		time c;
		c.p = xx;
		c.q = yy;
		a.push_back(c);
		fa.push_back(true);
	}
	
	for (int i = 0; i < nb; i++)
	{
		int x, y; char z;
		cin >> x >> z >> y;
		int xx = x*60+y;
		cin >> x >> z >> y;
		int yy = x*60+y;
		time c;
		c.p = xx;
		c.q = yy;
		b.push_back(c);
		fb.push_back(true);
	}

	for (int i = 0; i < na; i++)
		for (int j = i+1; j < na; j++)
		{
			if (a[i].p > a[j].p)
			{
				time tmp;
				tmp = a[i];
				a[i] = a[j];
				a[j] = tmp;
			}
		}

	for (int i = 0; i < nb; i++)
		for (int j = i+1; j < nb; j++)
		{
			if (b[i].p > b[j].p)
			{
				time tmp;
				tmp = b[i];
				b[i] = b[j];
				b[j] = tmp;
			}
		}


}

void run()
{
	int s;
	tt[0] = 0; 
	tt[1] = 0;
	int current = 0;
	if (nb == 0 && na == 0)
	{
		return;
	}
	else if (na > 0 && nb == 0)
	{
		s = 0; 
		fa[0] = false;
	}
	else if (na == 0 && nb > 0)
	{
		s = 1;
		fb[0] = false;
	}
	else
	if (a[0].p < b[0].p)
	{
		s = 0;
		fa[0] = false;
	}
	else
	{
		s = 1;
		fb[0] = false;
	}
	tt[s] = 1;
	tt[1-s] = 0;

	while (true)
	{
		bool ok = false;
		for (int i = 0; i < na; i++)
		{
			if (fa[i])
			{
				ok = true;
				break;
			}
		}
		if (!ok)
		for (int j = 0; j < nb; j++)
		{
			if (fb[j])
			{
				ok = true;
				break;
			}
		}
		if (!ok)
			return;
		int oper = -1;
		if (s == 1)
		{
			for (int i = 0; i < na; i++)
				if (fa[i])
				{
					if (a[i].p >= b[current].q+t)
					{
						oper = i;
						break;
					}
				}
		}
		else
		{
			for (int i = 0; i < nb; i++)
				if (fb[i])
				{
					if (b[i].p >= a[current].q+t)
					{
						oper = i;
						break;
					}
				}
		}

		if (oper == -1)
		{
			int ta1 = -1;
			int tb1 = -1;
			for (int i = 0; i < na; i++)
			{
				if (fa[i])
				{
					ta1 = i;
					break;
				}
			}
			for (int i = 0; i < nb; i++)
			{
				if (fb[i])
				{
					tb1 = i;
					break;
				}
			}

			if (ta1 == -1 && tb1== -1)
				return;
			if (ta1 == -1 && tb1 > -1)
			{
				s = 1;
				current = tb1;
				fb[tb1] = false;
			}
			else if (ta1 > -1 && tb1 == -1)
			{
				s = 0;
				current = ta1;
				fa[ta1] = false;
			}
			else
			if (a[ta1].p < b[tb1].q)
			{
				s = 0;
				fa[ta1] = false;
				current = ta1;
			}
			else
			{
				s = 1;
				fb[tb1] = false;
				current = tb1;
			}
			tt[s]++;
		}
		else
		{
			if (s == 0)
				fb[oper] = false;
			else
				fa[oper] = false;
			current = oper;
			s = 1-s;
		}
	}
}


int main()
{
	int m;
	cin >> m;
	for (int i = 0; i < m ;i++)
	{
		init();
		run();
		cout << "Case #" << i+1 << ": " << tt[0] << " " << tt[1] << endl;
	}
}
