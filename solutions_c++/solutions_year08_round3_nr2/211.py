#include <fstream>
#include <string>

using namespace std;

ifstream cin("b.in");
ofstream cout("b.out");

string s;
long long res;
int oper[50];

long long getNum()
{
	long long a = 0;
	long long b = s[0]-'0';
	int f = 1;
	for (int i = 0; i < (int)s.length()-1; i++)
	{
		if (oper[i] == 0)
			b = b*10 + s[i+1]-'0';
		if (oper[i] == -1)
		{
			a = a+f*b;
			b = (s[i+1]-'0');
			f = -1;
		}
		if (oper[i] == 1)
		{
			a = a+f*b;
			b = s[i+1]-'0';
			f = 1;
		}
	}
	a += f*b;
	return a;
}

void calc(const int &dep)
{
	if (dep == (int)s.length()-1)
	{
		long long sss = getNum();
		if (sss == 1 || sss == -1)
			return;
		if (sss < 0)
			sss = -sss;
		if (sss %2 == 0 || sss %3 == 0 || sss %5 == 0 || sss %7 ==0)
			res++;
		return;
	}

	oper[dep] = 0;
	calc(dep+1);
	oper[dep] = 1;
	calc(dep+1);
	oper[dep] = -1;
	calc(dep+1);
}

int main()
{
	int T;
	cin >> T;
	for (int i = 0; i < T; i++)
	{
		
		cin >> s;
		res = 0;
		calc(0);
		cout << "Case #" << i+1 << ": " << res << endl;
	}
}
