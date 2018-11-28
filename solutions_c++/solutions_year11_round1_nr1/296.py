#include <iostream>
#include <map>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

long long gcd (long long a, long long b)
{
	if (b>a)
		swap (a, b);
	if (b==0)
		return a;
	else
		return gcd (b, a%b);
}

void solve_case ()
{
	unsigned long long N, Pd, Pg;
	cin >> N >> Pd >> Pg;
	bool flag;

	if (Pg==0)
	{
		if (Pd>0)
			flag = false;
		else
			flag = true;
	}
	else if (Pg==100)
	{
		if (Pd==100)
			flag = true;
		else
			flag = false;
	}
	else
		flag = true;

	if (Pd>0)
	{
		long long k = gcd (Pd, 100);
		int base = 100/k;
	if (base>N)
		flag = false;
	}


	if (flag)
		cout << "Possible";
	else
		cout << "Broken";
	cout << endl;
}

int main ()
{
	int total_cases;

	cin >> total_cases;
	for (int cases=1 ;cases<=total_cases ;cases++)
	{
		cout << "Case #" << cases << ": ";
		solve_case ();
	}

	return 0;
}
