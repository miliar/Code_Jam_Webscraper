#include <iostream>
#include <string>
#include <sstream>
#include <set>
using namespace std;

bool is_recycled(int a, int b)
{
	stringstream sstr;
	string stra, strb;

	if (a == b)
		return false;

	sstr << a;
	sstr >> stra;
	sstr << b;
	sstr >> strb;

	for (int i = 1; i < stra.size(); i++)
	{
		stringstream nss;
		nss << stra.substr(i, stra.size() - i) << stra.substr(0, i);
		int nb;
		nss >> nb;
		if (b == nb)
			return true;
	}

	return false;
}

void c_small()
{
	int t, i, a, b;

	cin >> t;
	for (int i = 1; i <= t; i++)
	{
		cin >> a >> b;
		int c = 0;

		for (int x = a; x <= b; x++)
		{
			for (int y = x+1; y <= b; y++)
			{
				if (is_recycled(x, y))
				{
//					cout << "\t" << x << ' ' << y << endl;
					c++;
				}
			}
		}

		cout << "Case #" << i << ": " << c << endl;
	}
}

int ndigit(int a)
{
	int c = 0;

	do
	{
		a /= 10;
		c++;
	}while(a);

	return c;
}

set<int> get_them(const int aa, const int bb)
{
	int a = aa;
	set<int> si;
	int cnd = ndigit(a);
	int nd = ndigit(a);

	si.insert(a);

	int ten;
	for (ten = 1; --nd; ten *= 10);
	nd = cnd;

	while(nd--)
	{
		int r = a % 10;
		a /= 10;
		a += r * ten;

		if (ndigit(aa) == cnd && a >= aa && a <= bb)
		{
			si.insert(a);
		}
	}

	return si;
}

class Combination
{
	enum {array_size = 20};
	static long long array[array_size][array_size];

public:
	Combination()
	{
		for (int i = 0; i < array_size; i++)
		{
			array[i][0] = 1;
			array[0][i] = 1;
			array[i][i] = 1;
		}

		for (int i = 1; i < array_size; i++)
		{
			for (int j = 1; j < i; j++)
			{
				array[i][j] = (array[i-1][j] * i) / (i - j);
			}
		}
	}

	long long operator()(int n, int r) const {return array[n][r];}
	int size() const {return array_size;}
};

long long Combination::array[array_size][array_size];

void c_big()
{
	int t, i, a, b;
	Combination comb;

	cin >> t;
	for (int i = 1; i <= t; i++)
	{
		cin >> a >> b;
		set<int> si;
		int c = 0;

		for (int x = a; x <= b; x++)
		{
			if (si.find(x) != si.end())
				continue;

			set<int> new_si = get_them(x, b);

			if (new_si.size() > 1)
			{
				set<int>::iterator iter = new_si.begin();
				while(iter != new_si.end())
				{
					si.insert(*iter);
					iter++;
				}

				c += comb(new_si.size(), 2);
			}
		}

		cout << "Case #" << i << ": " << c << endl;
	}
}

int main()
{
	int x = 0;
	
	do
	{
//		c_small();
		c_big();
	}while(x);

	return 0;
}
