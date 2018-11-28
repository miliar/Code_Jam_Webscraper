#include <iostream>
#include <cmath>

using namespace std;

void _1A1()
{
	int T,N,D,Pd,Pg;
	double currP;
	bool found;
	int tW, tL;
	int i,j;

	cin >> T;

	for(i=0; i<T; i++)
	{
		cin >> N >> Pd >> Pg;
		found = false;

		for(j=1; j<=N;j++)
		{
			currP = (j*Pd)/100.0;

			if (floor(currP) == ceil(currP))
			{
				found = true;
				break;
			}
		}

		tW = j*Pd;
		tL = j*(100-Pd);

		if (tL > 0 && (Pg == 100))
		{
			cout << "Case #" << i+1 << ": Broken" << endl;
 		}
		else if (Pd > 0 && Pg == 0)
		{
			cout << "Case #" << i+1 << ": Broken" << endl;
		}
		else if (found)
		{
			cout << "Case #" << i+1 << ": Possible" << endl;
		}
		else
		{
			cout << "Case #" << i+1 << ": Broken" << endl;
		}
	}
}

int main()
{
	_1A1();
	return 0;
}