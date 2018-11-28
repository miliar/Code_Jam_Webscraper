#include <iostream>
#include <fstream>
#include <cmath>
#include <string>
#include <algorithm>
#include <sstream>


using namespace std;

ifstream in("small.in");
ofstream out("small.out");

bool sub(const string& a, const string& b)
{
	for (int i = 0; i < b.size(); ++i)
	{		
		if (a.substr(i, b.size()) == b)
			return true;
	}
	return false;
}

bool rec(int a, int b)
{	
	ostringstream A;
	A << a << a;

	string strA = A.str();

	ostringstream B;

	B << b;

	string strB = B.str();	

	if (strA.size() != 2*strB.size())
		return false;

	if (sub(strA, strB))
		return true;
	
	return false;
	
}

int main()
{
	int test, t, a, b;

	in >> test;

	for (t = 1; t <= test; ++t)
	{
		in >> a >> b;
		
		int ans = 0;
		
		for (int n = a; n <= b; ++n)
			for (int m = n + 1; m <= b; ++m)
				if (rec(n,m))
					ans ++;

		out << "Case #" << t << ": " << ans << endl;
	}

	return 0;
}