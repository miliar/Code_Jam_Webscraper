#include <iostream>
#include <stdio.h>
#include <fstream>
#include <math.h>
using namespace std;

int main()
{
	int T, C, D, N;
	char cStr[100][4];
	char dStr[100][3];
	char str[101];
	char result[101];
	int Nresult;
	bool cFound, dFound;

	cin >> T;
	int i,j,k,p;

	for (i=1; i<=T; i++)
	{
		Nresult = 0;
		cin >> C;
		for (j=0; j<C; j++)
		{
			cin >>cStr[j];
		}
		cin >> D;
		for (j=0; j<D; j++)
		{
			cin >> dStr[j];
		}

		cin >> N;
		cin >> str;

		result[0] = str[0];
		Nresult = 1;

		for (j=1; j<N;j++)
		{
			cFound = false;
			dFound = false;
			if (Nresult > 0 )
			{
				for(k=0;k<C;k++)
				{
					if (((cStr[k][0]==result[Nresult-1])&&(cStr[k][1]==str[j]))|| ((cStr[k][1]==result[Nresult-1])&&(cStr[k][0]==str[j])))
					{
						cFound = true;
						result[Nresult-1] = cStr[k][2];
						break;
					}
				}

				if (!cFound)
				{
					for(k=0;k<D;k++)
					{
						if (dStr[k][0]==str[j])
						{
							for(p=0;p<Nresult;p++)
							{
								if (result[p]==dStr[k][1])
								{
									dFound = true;
									Nresult = 0;
									break;
								}
							}
						}

						if (dFound) break;

						if (dStr[k][1]==str[j])
						{
							for(p=0;p<Nresult;p++)
							{
								if (result[p]==dStr[k][0])
								{
									dFound = true;
									Nresult = 0;
									break;
								}
							}
						}

						if (dFound) break;
					}
				}
				if (!(cFound || dFound))
				{
					Nresult ++;
					result[Nresult-1] = str[j];
				}
			}
			else
			{
				Nresult = 1;
				result[0] = str[j];
			}
		}

		cout << "Case #"<<i<<": [";
		if (Nresult > 0)
		{
			cout << result[0];
			for (j=1;j<Nresult;j++) cout <<", "<< result[j];
		}
		cout << "]" << endl;
	}
	return 0;
}