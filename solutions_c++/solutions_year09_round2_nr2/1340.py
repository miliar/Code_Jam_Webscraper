/*#include <iostream>
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

		cout << "Case #" << xxx << ": " << st << endl;
	}

	return 0;
}*/


/*#include <iostream>
#include <cmath>
using namespace std;

int t,c,n;

int main()
{
	cin >> t;
	for (int xxx =1; xxx<=t; ++xxx)
	{
		cin >> c >> n;
		double result = 1;
		for (int i=1; i<=100000; ++i)
			result += 2.0*i/pow(3.0,i*1.0);
		printf("Case #%d: %.7f\n", xxx, result);
	}
}
*/

#include <iostream>
#include <cstring>
using namespace std;

int num[10];

bool check(int t)
{
	int chk[10] = {0};
	while (t)
	{
			++chk[t%10];
			t /= 10;
	}

	for (int i=1; i<=9; ++i)
	{
		if (chk[i] != num[i])
			return false;
	}
	return true;
}

int main()
{
	int n;
	cin >> n;
	for (int xxx=1; xxx<=n; ++xxx)
	{
		memset(num, 0, sizeof(num));
		int last;
		cin >> last;
		int t = last;
		while (t)
		{
			++num[t%10];
			t /= 10;
		}
		t = last + 1;
		while (!check(t))
			++t;

		cout << "Case #" << xxx << ": " << t << endl;
	}
}