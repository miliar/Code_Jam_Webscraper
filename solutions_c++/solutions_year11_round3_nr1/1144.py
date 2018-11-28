#include <iostream>
#include <cmath>
#include <vector>
#include <string>
#include <iomanip>
#include <climits>

using namespace std;

void _1C1()
{
	int T;
	int i,j,k;

	cin >> T;

	vector< vector<char> > vec(50, vector<char>(50));

	for(i=0;i<T;i++)
	{
		int R,C;
		cin >> R >> C;

		for(j=0;j<R;j++)
			for(k=0;k<C;k++)
			{
				cin >> vec[j][k];
			}

		bool wrong=false;
		for(j=0;j<R;j++)
		{
			for(k=0;k<C;k++)
			{
				if(vec[j][k]=='#')
				{
					if( (k+1 < C && vec[j][k+1]=='#') && (j+1 < R && vec[j+1][k]=='#') && vec[j+1][k+1]=='#')
					{
						vec[j][k]='/';
						vec[j][k+1] = '\\';
						vec[j+1][k] = '\\';
						vec[j+1][k+1]= '/';
					}
					else
					{
						wrong=true;
						break;
					}
				}
			}
			if(wrong)
			{
				break;
			}
		}

		cout << "Case #" << i+1 << ": " << endl;
		if(wrong)
		{
			cout << "Impossible" << endl;
		}
		else
		{
			for(j=0;j<R;j++)
			{
				for(k=0;k<C;k++)
				{
					cout << vec[j][k];
				}
				cout << endl;
			}
		}

	}

}

int main()
{
	// _1A1();
	// _1A2();
	// _1B1();
	// _1B2();
	_1C1();
	return 0;
}