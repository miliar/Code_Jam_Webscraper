#include <iostream>

using namespace std;

int main()
{
	int T, R, C, i, j, k;

	char Tie[51][51];

	bool Impossible;

	cin >> T;

	for (i=0; i < T; i++)
	{
		cin >> R >> C;
		memset(Tie, 0, sizeof(Tie));

		for (j=0; j < R; j++)
			for (k=0; k < C; k++)
				cin >> Tie[j][k];

		Impossible = false;
		for (j=0; j < R; j++)
			for (k=0; k < C; k++)
				if (Tie[j][k] == '#') 
				{
					Tie[j][k]='/';
					if ((Tie[j][k+1] == '#') 
						&& (Tie[j+1][k] == '#') 
						&& (Tie[j+1][k+1] == '#'))
					{
						Tie[j+1][k+1]='/';

						Tie[j][k+1]='\\';

						Tie[j+1][k]='\\';
					} else Impossible = true;
				}

		printf("Case #%d:\n", i+1);
		if (Impossible) cout <<"Impossible" <<endl;
		else 
		for (j=0; j < R; j++)
		{
			for (k=0; k < C; k++)
				cout << Tie[j][k];
			cout << endl;
		}
	}
	return 0;
}