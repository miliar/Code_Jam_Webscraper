#include <iostream>
#include <string>
#include <vector>
#include <list>

using namespace std;

int main(int argc, char** args)
{
	int T;
	cin >> T;
	
	for (int t = 0; t < T; t++)
	{
		cout << "Case #" << (t+1) << ":" << endl;
	
		int N;
		cin >> N;
		
		char*		grid = new char[N*N];
		double*		WP = new double[N];
		double*		OWP = new double[N];
		double*		OOWP = new double[N];
		
		for (int r = 0; r < N; r++)
			for (int c = 0; c < N; c++)
				cin >> grid[c + r * N];
		
		// Calc WP
		for (int r = 0; r < N; r++)
		{
			int total = 0, won = 0;
			for (int c = 0; c < N; c++)
			{
				if (grid[c + r * N] == '.') continue;
				total++;
				if (grid[c + r * N] == '1') won++;
			}
			
			WP[r] = (double)won / (double)total;
			//cout << "WP: " << WP[r] << endl;
		}
		
		// Calc OWP
		for (int s = 0; s < N; s++)
		{
			double TWP = 0.0;
			int		ops = 0;
		
			for (int r = 0; r < N; r++)
			{
				if (grid[r + s * N] == '.') continue;
				ops++;
			
				int total = 0, won = 0;
				for (int c = 0; c < N; c++)
				{
					if (c == s) continue;
					if (grid[c + r * N] == '.') continue;
					total++;
					if (grid[c + r * N] == '1') won++;
				}
				
				double WP = (double)won / (double)total;
				TWP += WP;
			}
			
			OWP[s] = TWP / (double)ops;
			//cout << "OWP: " << OWP[s] << endl;
		}
		
		// Calc OOWP
		for (int s = 0; s < N; s++)
		{
			double TOWP = 0.0;
			int		ops = 0;
			
			for (int r = 0; r < N; r++)
			{
				if (grid[r + s * N] == '.') continue;
				ops++;
				TOWP += OWP[r];
			}
			
			OOWP[s] = TOWP / (double)ops;
			//cout << "OOWP: " << OOWP[s] << endl;
		}
		
		for (int s = 0; s < N; s++)
			cout << ((WP[s] * 0.25) + (OWP[s] * 0.5) + (OOWP[s] * 0.25)) << endl;
	}
}

