#include <iostream>
#include <stdlib.h>
#include <stdio.h>

#define cyc(i,n) for (i=0; i<n; i++)

using std::cin;
using std::cout;
using std::string;

int main()
{
	int t,T;
	
	cin >> T;
	
	cyc(t,T)
	{
		int c,C;
		int D;
		int h = 0;
		int cur_max = 0;
		int new_max;
		int last_position = -1000001;
		int P;
		int V;

		cin >> C >> D;

		cyc(c,C)
		{
			cin >> P >> V;
			h -= (P - last_position);
			last_position = P;
			if (h < 0)
				h = 0;

			new_max = h + (V-1)*D;
			if (new_max > cur_max)
				cur_max = new_max;

			h += V*D;
		}
		cout << "Case #" << t + 1 << ": " << double(cur_max)/2.0 << "\n";
	}
	return 0;
}
