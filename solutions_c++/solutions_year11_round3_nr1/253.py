#include <iostream>
#include <stdio.h>
#include <fstream>
#include <math.h>
using namespace std;

int main()
{
	char field[52][52];
	int T, R, C;

	int i,j,k;
	bool imp;
	cin >> T;
	for (i=1;i<=T;i++)
	{
		imp = false;
		cin >> R >> C;
		for (j=0;j<R;j++)
			for (k=0;k<C;k++)
				cin >> field[j][k];

		for (j=0;j<R;j++)
		{
			if (imp) break;
			for (k=0;k<C;k++)
			{
				if (imp) break;
				if (field[j][k]=='#')
				{
					if ((k<C-1) && (field[j][k+1]=='#'))
					{
						field[j][k]='/';
						field[j][k+1]='\\';
						if ((j<R-1)&&(field[j+1][k]=='#')&&(field[j+1][k+1]=='#'))
						{
							field[j+1][k]='\\';
							field[j+1][k+1]='/';
						}
						else
						{
							imp = true;
						}

					}
					else
					{
						imp = true;
					}
				}
			}
		}
		cout << "Case #" << i <<":" << endl;
		if (imp) cout << "Impossible" << endl;
		else
		{
			for (j=0;j<R;j++)
			{
			for (k=0;k<C;k++)
				cout << field[j][k];
			cout << endl;
			}
		}
	}

	return 0;
}