#include <iostream>
#include <string>
using namespace std;

int main(void)
{
	unsigned int num_cases, n, q, min_switches, switches[1001][101];
	string engines[101], queries[1001];

	cin >> num_cases;
	for(unsigned int c = 1; c <= num_cases; c++)
	{
		memset(switches, 0, sizeof(unsigned int) * 1001 * 101);
		cin >> n; cin.get();
		for(unsigned int i = 1; i <= n; i++) getline(cin, engines[i]);

		cin >> q; cin.get();
		for(unsigned int i = 1; i <= q; i++) getline(cin, queries[i]);
		q = distance(queries + 1, unique(queries + 1, queries + q + 1));

		for(unsigned int i = 1; i <= q; i++)
		{
			for(unsigned int j = 1; j <= n; j++)
			{
				unsigned int min = 999999;

				for(unsigned int k = 1; k <= n; k++)
				{
					if(engines[k] == queries[i]) continue;
					if(k == j && switches[i - 1][k] < min) min = switches[i - 1][k];
					else if(k != j && switches[i - 1][k] + 1 < min) min = switches[i - 1][k] + 1;
				}
						
				switches[i][j] = min;
			}
		}

		min_switches = 999999;
		for(unsigned int j = 1; j <= n; j++) if(switches[q][j] < min_switches) min_switches = switches[q][j];
		cout << "Case #" << c << ": " << min_switches << endl;
	}
}
