#include <iostream>
#include <cstdlib>

using namespace std;

int main()
{
	int tb, to, lb, lo, t;
	char r;
	int a, b, p, dt;
	cin >> a;
	for(int i = 0; i < a; i++)
	{
		tb = 0;
		to = 0;
		lb = 1;
		lo = 1;
		t = 0;
		cin >> b;
		for(int j = 0; j < b; j++)
		{
			cin >> r;
			cin >> p;
			if(r == 'B')
			{
				dt = abs(p - lb);
				if(tb + dt > t)
				{
					t = tb + dt;
				}
				t++;
				tb = t;
				lb = p;
			}
			else
			{
				dt = abs(p - lo);
				if(to + dt > t)
				{
					t = to + dt;
				}
				t++;
				to = t;
				lo = p;
			}
		}

		cout << "Case #" << i+1 << ": " << t << endl;
	}
}
