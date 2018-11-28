/*#include <iostream>
#include <vector>
#include <set>
using namespace std;

long long cas;
long long bas[10];

bool eoln( istream &fin = cin )
{ 	return fin.peek()=='\n' || fin.peek()==EOF;  	}

vector<long long> getbit(long long x, long long base)
{
	vector<long long> ret;
	ret.clear();
	while (x > 0)
	{
		ret.push_back(x % base);
		x /= base;
	}

	return ret;
}

bool happy(long long x, long long base)
{
	vector<long long> bits = getbit(x, base);
	set<long long> vis;
	vis.clear();

	while ((vis.find(x) == vis.end()) && (x != 1))
	{
		vis.insert(x);
		long long num = 0;
		for (long long i=0; i<bits.size(); ++i)
			num += bits[i] * bits[i];
		x = num;
		bits = getbit(x, base);
	}

	if (x == 1)
		return true;
	else
		return false;
}

long long getmin(long long start, long long base)
{
	while (!happy(start, base))
		++start;
	return start;
}

long long main()
{
	cin >> cas;
	cin.get();
	for (long long xxx=1; xxx<=cas; ++xxx)
	{
		memset(bas, 0, sizeof(bas));
		long long st = 2;
		long long bn = 0;
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
			for (long long i=1; i<=bn; ++i)
			{
				long long xx = getmin(st, bas[i]);
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

long long t,c,n;

long long main()
{
	cin >> t;
	for (long long xxx =1; xxx<=t; ++xxx)
	{
		cin >> c >> n;
		double result = 1;
		for (long long i=1; i<=100000; ++i)
			result += 2.0*i/pow(3.0,i*1.0);
		prlong longf("Case #%d: %.7f\n", xxx, result);
	}
}
*/

/*#include <iostream>
#include <cstring>
using namespace std;

long long num[10];

bool check(long long t)
{
	long long chk[10] = {0};
	while (t)
	{
			++chk[t%10];
			t /= 10;
	}

	for (long long i=1; i<=9; ++i)
	{
		if (chk[i] != num[i])
			return false;
	}
	return true;
}

long long getmax()
{
	long long sum = 0;
	for (long long i=9; i>=0; --i)
		for (long long j=1; j<=num[i]; ++j)
			sum = sum * 10 + i;
	return sum;
}

long long getmin()
{
	long long sum = 0;
	bool addzero = false;
	for (long long i=1; i<=9; ++i)
	{
		bool flag = true;
		if (num[i] && (!addzero))
		{
			addzero = true;
			flag = false;
			sum += i;
			for (long long j=1; j<=num[0]; ++j)
				sum *= 10;
		}

		for (long long j=(flag?1:2); j<=num[i]; ++j)
			sum = sum * 10 + i;
	}

	return sum;
}

void rearrange(long long data[30], long long maxp)
{
	long long nn[10] = {0};
	for (long long i=1; i<=maxp; ++i)
		++nn[data[i]];

	long long pp = maxp;
	for (long long i=0; i<=9; ++i)
	{
		for (long long j=1; j<=nn[i]; ++j)
		{
			data[pp] = i;
			--pp;
		}
	}
}

int main()
{
	long long n;
	cin >> n;
	for (long long xxx=1; xxx<=n; ++xxx)
	{
		memset(num, 0, sizeof(num));
		long long last;
		scanf("%lld", &last);
		long long t = last;
		while (t)
		{
			++num[t%10];
			t /= 10;
		}

		if (getmax() == last)
		{
			++num[0];
			cout << "Case #" << xxx << ": " << getmin() << endl;
			continue;
		}

		long long data[30] = {0};
		t = last;
		long long pos = 0;
		while (t)
		{
			++pos;
			data[pos] = t % 10;
			t /= 10;
		}

		long long start = 1;
		long long mymin, mymin2, myminpos, mymin2pos=100;
		for (long long start=1; start<=pos-1; ++start)
		{
			long long tm, tm2, tmpos, tm2pos;
			tm = data[start];
			tmpos = start;
			tm2 = tm;
			tm2pos = 0;
			for (long long i=start+1; i<=pos; ++i)
			{
				if (data[i] < tm2)
				{
					tm2 = data[i];
					tm2pos = i;
					break;
				}
			}

			if (tm2pos > 0 && tm2pos < mymin2pos)
			{
				mymin = tm;
				mymin2 = tm2;
				myminpos = tmpos;
				mymin2pos = tm2pos;
			}
		}

		long long tmp = data[myminpos];
		data[myminpos] = data[mymin2pos];
		data[mymin2pos] = tmp;
		rearrange(data, mymin2pos-1);

		t = 0;
		for (long long i=pos; i>=1; --i)
			t = t * 10 + data[i];

		cout << "Case #" << xxx << ": " << t << endl;
	}
}*/

#include <iostream>
#include <cstring>
#include <string>
#include <set>
using namespace std;

typedef struct _treetype {
	double yes;
	double no;
	_treetype* yesnode;
	_treetype* nonode;
	string name;
	double pro;
	_treetype* father;
	_treetype() {
		yes = no = pro = 0;
		yesnode = nonode = father = NULL;
		name = "";
	}
} treetype;

treetype root;

int getnonspace(string x)
{
	int p = 0;
	while (p < x.size() && x[p] == ' ') ++p;
	return p;
}

int main()
{
	int cas;
	cin >> cas;
	for (int xxx=1; xxx<=cas; ++xxx)
	{
		int line;
		cin >> line;
		cin.get();
		treetype* curnode = &root;
		bool flagyes = true;
		for (int i=1; i<=line; ++i)
		{
			string tmp;
			getline(cin, tmp);
			int st = getnonspace(tmp);
			if (tmp[tmp.size()-1] != ')') // feature
			{
				if (curnode->name == "")
				{
					double pro;
					char fea[20];
					sscanf(tmp.c_str(), "(%lf %s", &pro, fea);
					curnode->name = fea;
					curnode->pro = pro;
				}
				else
				{
					treetype tmpnode;
					if (flagyes)
					{

					}
				}
			}
			else if (tmp[st] == ')') // end node
			{
				if (flagyes)
				{
					flagyes = false;
					treetype* tp = curnode->father;
					curnode = new treetype;
					curnode->father = tp;
				}
				else
				{
					curnode = curnode->father;
					if (curnode->nonode == NULL)
						flagyes = false;
					else
						flagyes = true;
				}
			}
			else
			{
				double pro;
				sscanf(tmp.c_str(), "(%lf)", &pro);
				if (flagyes)
				{
					curnode->yes = pro;
					flagyes = false;
				}
				else
				{
					curnode->no = pro;
				}
			}

			//
		}
	}
}