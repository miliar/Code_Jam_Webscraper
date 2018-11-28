#include <iostream>
#include <algorithm>

using namespace std;

bool f(unsigned a, unsigned b)
{
    if (a == b)
	return false;
    if (a < b)
	swap(a, b);
    if (a >= 2*b)
	return true;
    return !f(b, a-b);
}

int main()
{
    unsigned T;
    while (cin >> T)
    {
	for (unsigned t = 1; t <= T; ++t)
	{
	    unsigned A1, A2, B1, B2;
	    cin >> A1 >> A2 >> B1 >> B2;
	    unsigned n = 0;
	    for (unsigned a = A1; a <= A2; ++a)
	    {
		for (unsigned b = B1; b <= B2; ++b)
		{
		    if (f(a, b))
			n++;
		}
	    }
	    cout << "Case #" << t << ": " << n << endl;
	}
    }
    return 0;
}
