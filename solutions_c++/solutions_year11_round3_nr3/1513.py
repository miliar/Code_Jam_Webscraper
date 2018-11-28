#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <stack>
#include <iomanip>
#include <list>
#include <string>
#include <sstream>

#define	T1 "C"

#if 0
#define IN	"in.txt"
#define OUT	"out.txt"
#elif 1
#define	T2 "0"
#define IN	T1"-small-attempt"T2".in"
#define OUT	T1"-small-attempt"T2".out"
#elif 0
#define IN	T1"-large.in"
#define OUT	T1"-large.out"
#endif

using namespace std;

typedef vector<int> Vec;

void out(const Vec &v)
{
	for(int i=0; i<v.size(); ++i)
	{
		cout << v[i] << endl;
	}
	cout << endl;
}

void sort(Vec &v)
{
	sort(v.begin(), v.end());
}

int gcd(int a, int b)
{
	return b != 0 ? gcd(b, a % b) : a;
}

int lcm(int a, int b)
{
	return a * b / gcd(a, b);
}

// a x + b y = gcd(a, b)
int extgcd(int a, int b, int &x, int &y)
{
	int g = a; x = 1; y = 0;
	if (b != 0) g = extgcd(b, a % b, y, x), y -= (a / b) * x;
	return g;
}

void solve_a_case(ifstream &in, int &result)
{
	// input
	int n, l, h;
	in >> n >> l >> h;

	Vec v(n);
	for(int i=0; i<n; ++i)
	{
		in >> v[i];
	}
	sort(v);

	// calc
	for(int i=l; i<=h; ++i)
	{
		bool ok = false;
		for(int j=0; j<v.size(); ++j)
		{
			if (v[j]==i)
			{
				ok = true;
				continue;
			}
			else if (v[j]>i)
			{
				if (v[j]%i==0)
				{
					ok = true;
					continue;
				}
				else
				{
					ok = false;
					break;
				}
			}
			else if (v[j]<i)
			{
				if (i%v[j]==0)
				{
					ok = true;
					continue;
				}
				else
				{
					ok = false;
					break;
				}
			}
		}
		if (ok)
		{
			result = i;
			return;
		}
	}
}

void solve_all_cases(ifstream &in, ofstream &out)
{
	int case_num = 0;

	in >> case_num;
	for(int i=0; i<case_num; i++)
	{
		int result = -1;
		solve_a_case(in, result);

		out << "Case #" << i+1 << ": ";
		if (result==-1)
			out << "NO";
		else
			out << result;
		out << endl;
	}
}

int main()
{
	ifstream in(IN);
	ofstream out(OUT);

	solve_all_cases(in, out);

	return 0;
}
