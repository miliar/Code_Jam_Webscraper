#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main()
{
	ifstream in("B.in");
	ofstream out("B.out");

	int T;
	in >> T;
	
	for(int i = 0; i < T; ++i)
	{
		int N, S, p, t;
		int numAns = 0;

		in >> N >> S >> p;
		
		for(int j = 0; j < N; ++j)
		{
			in >> t;

			if(t < p) //dont even have enough points to start with
				continue;

			t -= p;

			if(t < 2*p - 4) //impossible
				continue;
			else if((t < 2*p - 2)) //possible but surprising
			{
				if (S > 0)
				{
					numAns++;
					S--;
				}
			}
			else //we have enough to have had higher.
				numAns++;
		}

		out << "Case #" << i + 1 << ": " << numAns << endl;
	}
	

	/*int a;
	cin >> a;*/
	return 0;
}
