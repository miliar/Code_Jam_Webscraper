#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <string>

using namespace std;

const int MAXN = 50;
int v[MAXN];

int main()
{
	string buffer;
	int casi;
	cin >> casi;
	
	
	for (int caso = 1; caso <= casi; caso++)
	{
		string readed;
		int n;
		cin >> n;

		for (int r = 0; r < n; r++)
		{
			int maxv = -1;
	//		for (int c = 0; c < n; c++)
			{
				cin >> readed;
				for (int j = 0; j < readed.size(); j++)
					if (readed[j] == '1') maxv = j;
			}
			v[r] = maxv;
		}

		#ifdef DEBUG
			cerr << "Lettura <" << readed << ">\n";
			for (int i = 0; i < n ; i++)
				cerr << v[i] << "\n";
			cerr << "Fine lettura \n";
		#endif

		int total_swap = 0;
		for (int i = 0; i < n; i++)
		{
			if (v[i] > i) // Condizione errore
			{
				// Risolve
				int j;
				for (j = i+1; j < n; j++)
					if (v[j] <= i) break;
				for (int y = j; y > i; y--, total_swap++)
				{
					swap(v[y], v[y-1]);
					#ifdef DEBUG
						cerr << "Scambio " << v[y-1] << " con " << v[y] << "\n";
					#endif
				}
			}
		}
		
		cout << "Case #" << caso << ": " << total_swap << endl;
	}
	
	return 0;
}

