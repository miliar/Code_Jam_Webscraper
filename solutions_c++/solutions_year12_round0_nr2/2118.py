#include <iostream>
#include <cmath>

using namespace std;

int
main()
{
	int T, n, s, p, x, a, b, c, count, ca=0;
	cin >> T;
	while(T--)
	{
		cin >> n >> s >> p;
		count=0;
		while(n--)
		{
			cin >> x;
			a = x / 3;
			x = x - a;
			b = x / 2;
			c = x - b;

						
			if(c > a) swap(a, c);
			if(b > a) swap(a, b);
			if(c > b) swap(b, c);

			if(a >= p)
			{
				++count;
				continue;
			}
			
			if(!s)
				continue;
				
			if((abs(float(a)-p) == 1) && (b > 0) && (a == b))
			{
				--s;
				++count;
			}
		}
		cout << "Case #" << ++ca << ": " << count << endl;
	}

	return 0;
}

