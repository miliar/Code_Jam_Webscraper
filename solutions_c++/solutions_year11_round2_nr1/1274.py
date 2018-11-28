#include <iostream>
#include <cstdio>
#include <fstream>
#include <string>


using namespace std;

int main (int argc, char const* argv[])
{
	int T;
	double N, played[105], RPI[105], Wp[105], OWp[105], OOWp[105], W[105], tmp;
	int x[105][105];
	string input;
	ifstream in ("A.in");
	ofstream out ("A.out");
	
	in >> T;
	
	for (unsigned int t = 0; t < T; t += 1)
	{
		in >> N;
		
		for (unsigned int i = 0; i < N; i += 1)
		{
			in >> input;
			W[i] = 0;
			played[i] = 0;
			
			
			for (unsigned int j = 0; j < N; j += 1)
			{
				x[i][j] = ( input[j] == '1' ) ? 1 : ( (input[j] == '0') ? 0 : -1 );
				if(x[i][j] != -1)	played[i] ++;
				if (x[i][j] == 1)
				{
					W[i] ++;
				}
			}
			
			Wp[i] = W[i]/played[i];
			
		}
		
		for (unsigned int i = 0; i < N; i += 1)
		{
			tmp = 0;
			for (unsigned int j = 0; j < N; j += 1)
			{
				if(x[j][i] != -1)
				{
					if (x[j][i] == 1)
					{
						tmp += (W[j]-1)/(played[j]-1);
					}
					else	tmp += W[j]/(played[j]-1);
				}
			}
			OWp[i] = tmp/played[i];
			//cout << i << "-> " << OWp[i] << "\n";
		}
		
		
		for (unsigned int i = 0; i < N; i += 1)
		{
			tmp = 0;
			for (unsigned int j = 0; j < N; j += 1)
			{
				if(x[j][i] != -1)	tmp += OWp[j];
			}
			OOWp[i] = tmp/played[i];
		}
		cout << "Case #" << t+1 << ":\n";
		for (unsigned int i = 0; i < N; i += 1)
		{
			RPI[i] = 0.25 * Wp[i] + 0.50 * OWp[i] + 0.25 * OOWp[i];
			printf ( "%0.12lf\n", RPI[i] );
		}
	}
	
	
	return 0;
}

