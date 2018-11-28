#include <iostream>
#include <vector>
#include <set>
using namespace std;

int cas;
int bas[10];

bool eoln( istream &fin = cin )
{ 	return fin.peek()=='\n' || fin.peek()==EOF;  	}

vector<int> getbit(int x, int base)
{
	vector<int> ret;
	ret.clear();
	while (x > 0)
	{
		ret.push_back(x % base);
		x /= base;
	}

	return ret;
}

bool happy(int x, int base)
{
	vector<int> bits = getbit(x, base);
	set<int> vis;
	vis.clear();

	while ((vis.find(x) == vis.end()) && (x != 1))
	{
		vis.insert(x);
		int num = 0;
		for (int i=0; i<bits.size(); ++i)
			num += bits[i] * bits[i];
		x = num;
		bits = getbit(x, base);
	}

	if (x == 1)
		return true;
	else
		return false;
}

int getmin(int start, int base)
{
	while (!happy(start, base))
		++start;
	return start;
}

int main()
{
	cin >> cas;
	cin.get();
	for (int xxx=1; xxx<=cas; ++xxx)
	{
		memset(bas, 0, sizeof(bas));
		int st = 2;
		int bn = 0;
		while (!eoln())
		{
			++bn;
			cin >> bas[bn];
		}
		cin.get();

		bool f = true;
		while (f)
		{
			bool f2 = true;
			for (int i=1; i<=bn; ++i)
			{
				int xx = getmin(st, bas[i]);
				if (xx != st)
				{
					st = xx;
					f2 = false;
					break;
				}
			}
			f = !f2;
		}
		/*for (int i=1; i<=bn; ++i)
		{
			f = true;
			int last = st;
			st = getmin(st, bas[i]);
			if (last != st)
			{
				++last;
				++st;
				i = 1;
			}
		}*/

		cout << "Case #" << xxx << ": " << st << endl;
	}

	return 0;
}