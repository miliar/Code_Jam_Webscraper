#include <iostream>

using namespace std;

int main (int argc, char const* argv[])
{
	int T, S, N, p;
	cin >> T;
	for (int i = 0; i < T; i += 1)
	{
		cin >> N >> S >> p;
		int resultat=  0;
		int courant = 0;
		for (int j = 0; j < N; j += 1)
		{
			cin >> courant;
			if (3*p-2 <= courant )
			{
				resultat++;
			}
			else
			{
				if (3*p-4 <= courant && S >0 && p>=2)
				{
					resultat++;
					S = S -1;
				}
			}
		}
		cout << "Case #" << i+1 << ": " << resultat << endl;
		
	}
	return 0;
}
