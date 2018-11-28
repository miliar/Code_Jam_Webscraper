#include <iostream>
#include <vector>
#include <algorithm>
#include <gmpxx.h>	/* GNU MP, http://gmplib.org/, link with -lgmp -lgmpxx */
#include <string>
#include <cmath>


using namespace std;

int P;
int M[1024];
int covered[1024];
int teams;

int iscovered()
{
	for (int i = 0; i < teams; i++)
	{
		if (covered[i] < M[i])
			return 0;
	}
	return 1;
}

int main (int argc, char *argv[])
{
	int T, t;
	cin >> T;
	for (t = 1; t <= T; t++)
	{
		int P;
		int x;
		int cost = 0;
		cin >> P;
		teams = 1 << P;
		//cout << "P is " << P << " and teams " << teams << endl;
		for (int i = 0; i < teams; i++)
		{
			int y;
			cin >> y;
			M[i] = P - y;
			//cout << "Setting M[i] to " << M[i] << endl;
			covered[i] = 0;
		}
		for (int i = teams/2; i > 0; i=i/2)
			for (int j = 0; j < i; j++)
			{
				cin >> x;
				//cout << "Read in waste: " << x << endl;
			}
		if (iscovered()) goto end;
		for (int bs = teams; bs > 1; bs/=2)
		{
			//cout << "Starting blocksize " << bs << endl;
			for (int b = 0; b < teams/bs; b++)
			{
				bool problem = false;
				for (int z = 0; z < bs; z++)
				{
					int i = b*bs +z;
					if (covered[i] < M[i])
					{
						//cout << "Found a problem at team " << i << endl;
						// do something!
						problem = true;
						break;
					}
				}
				if (problem)
				{
					for (int z = 0; z < bs; z++)
					{
						int i = b*bs +z;
						covered[i]++;
					}
					cost++;
				}
				if (iscovered()) goto end;
			}
		}
		end:
		cout << "Case #" << t << ": " << cost << endl;
	}
	
	return 0;
}


