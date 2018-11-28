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

int gcd(int a, int b)
{
        if(b == 0)
        {
                return a;
        }
        else
        {
                return gcd(b, a % b);
        }
}


void _1C3()
{
	int T;
	int i,j,k;

	cin >> T;
	

	for(i=0;i<T;i++)
	{
		int N,L,H;
		vector<int> vec(100,0);

		cin >> N >> L >> H;

		for(j=0;j<N;j++)
		{
			cin >> vec[j];
		}

		bool found=false;
		bool foundj = false;
		int num=0;
		for(j=L;j<=H;j++)
		{
			foundj = true;
			for(k=0;k<N;k++)
			{
				if ( ( j > vec[k] && j%vec[k] != 0) ||
					( j <= vec[k] && vec[k]%j != 0) )
				{
					foundj = false;
					break;
				}
			}

			if(foundj)
			{
				num=j;
				found=true;
				break;
			}
		}

		// cout << found << endl;

		if(found)
		{
			cout << "Case #" << i+1 << ": " << num << endl;
		}
		else
		{
			cout << "Case #" << i+1 << ": NO" << endl;
		}
	}
}

int main()
{
	// _1A1();
	// _1A2();
	// _1B1();
	// _1B2();
	// _1C1();
	_1C3();
	return 0;
}