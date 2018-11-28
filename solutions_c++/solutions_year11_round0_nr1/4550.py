#include <iostream>

using namespace std;


int main()
{
	int T, N;
	int O[100], B[100];
	char seq[100];

	freopen("input.txt", "r+", stdin);

	freopen("o.out", "w+", stdout);

	cin >> T;

	for( int i = 1; i <=T; ++i )
	{
		cin >> N;
		int a = 0,b = 0;
		int result = 0;
		for( int j = 0; j < N; ++j )
		{
			cin >> seq[j];

			if( seq[j] == 'O')  cin >> O[a++];
			else cin >> B[b++];
		}

		int starto = 1, startb = 1;
		int idxo = 0, idxb = 0;

		for( int m = 0; m < N; ++m )
		{
			if( seq[m] == 'O' )
			{
				result += abs(O[idxo] - starto) + 1;

				if( idxb < b )
				{
					if( startb > B[idxb] )
					{
						startb -=  min( abs(O[idxo] - starto) + 1, abs(B[idxb] - startb) );
					}else
					{
						startb += min( abs(O[idxo] - starto) + 1, abs(B[idxb] - startb) );
					}
				}
				
				starto = O[idxo];
				idxo++;
			}else 
			{
				result += abs(B[idxb] - startb) + 1;

				if( idxo < a )
				{
					if( starto > O[idxo] )
					{
						starto -=  min( abs(B[idxb] - startb) + 1, abs(O[idxo] - starto) );
					}else
					{
						starto += min( abs(B[idxb] - startb) + 1, abs(O[idxo] - starto) );
					}
				}
				startb = B[idxb];
				idxb++;
			}
		}

		cout << "Case #" << i << ": " << result << endl;

	}
	return 0;
}
