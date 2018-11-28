
#include <iostream>

using namespace std;


struct o
{
	bool mi;
	int picks;
	int v;
	int x;
};

o d[1000];


int main()
{
	int c, n, K, b, t;
	cin >> c;

	for (int i = 1; i <= c; i++)
	{
		cout << "Case #" << i << ": ";

		cin >> n >> K >> b >> t;
		for (int j = 0; j < n; j++)
		{
			d[j].mi = false;
			d[j].picks = 0;
			cin >> d[j].x;
		}

		for (int j = 0; j < n; j++) cin >> d[j].v;

		int picks = 0;
		for (int j = n-1; j >= 0; j--)
		{
			if (b - d[j].x > t * d[j].v) { continue; }

			d[j].mi = true;
			for (int k = j+1; k < n; k++)
			{
				if (d[k].v >= d[j].v) continue;
				if (d[j].x - d[k].x > t * (d[j].v - d[k].v)) continue;

				// potkaji se pred barnem
				if (d[k].mi) { d[j].picks += d[k].picks; break; }
				d[j].picks++;
			}
			
			if (!d[j].mi) continue;

			K--;
			picks += d[j].picks;
			if (K == 0) break;
		}

		if (K != 0) cout << "IMPOSSIBLE";
		else cout << picks;
		cout << endl;
	}

	return 0;
}


