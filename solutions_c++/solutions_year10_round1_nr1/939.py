#include <iostream>
#include <cstdlib>

using namespace std;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int T;
	cin >> T;

	int N, K;
	for ( int t = 1; t <= T; t++)
	{
		cin >> N >> K;
		char **mas = new char*[N];
		for ( int i = 0; i < N; i++)
		{
			mas[i] = new char[N];
			for ( int j = 0; j < N; j++)
			{
				cin >> mas[i][j];
			}
		}
		int z;
		for ( int i = 0; i < N; i++)
		{
			z = N - 1;
			for ( int j = N - 1; j >= 0; j--)
			{
				if ( mas[i][j] != '.')
				{
					char s = mas[i][j];
					mas[i][j] = mas[i][z];
					mas[i][z] = s;
					z--;
				}
			}
		}

		bool r = 0;
		bool b = 0;
		int count1, count2 = 0;
		for ( int i = 0; i <= N - K; i++)
		{
			for ( int j = 0; j < N; j++)
			{
				count1 = 0;
				count2 = 0;
				int z = i;
				while ( z < i + K)
				{
					if ( mas[z][j] == 'R')
						count1++;
					if (mas[z][j] == 'B')
						count2++;
					z++;
				}
				
				if ( count1 == K)
					r = true;
				if ( count2 == K)
					b = true;
			}
		}
		
		for ( int j = 0; j <= N - K; j++)
		{
			for ( int i = 0; i < N; i++)
			{
				count1 = 0;
				count2 = 0;
				int z = j;
				while ( z < j + K)
				{
					if ( mas[i][z] == 'R')
						count1++;
					if (mas[i][z] == 'B')
						count2++;
					z++;
				}
				
				if ( count1 == K)
					r = true;
				if ( count2 == K)
					b = true;
			}
		}

		for ( int i = 0; i <= N - K; i++)
		{
			for ( int j = 0; j <= N - K; j++)
			{
				count1 = 0;
				count2 = 0;
				int s = 0;
				//int w = j;
				while ( s < K)
				{
					if (mas[i + s][j + s] == 'R')
						count1++;
					if (mas[i + s][j + s] == 'B')
						count2++;
					s++;
				}

				if ( count1 == K)
					r = true;
				if ( count2 == K)
					b = true;
			}
		}

		for ( int i = 0; i <= N - K; i++)
		{
			for ( int j = K - 1; j < N; j++)
			{
				count1 = 0;
				count2 = 0;
				int s = 0;
				//int w = j;
				while ( s < K)
				{
					if (mas[i + s][j - s] == 'R')
						count1++;
					if (mas[i + s][j - s] == 'B')
						count2++;
					s++;
				}

				if ( count1 == K)
					r = true;
				if ( count2 == K)
					b = true;
			}
		}

		/*for ( int i = 0; i < N; i++)
		{
			for ( int j = 0; j < N; j++)
			{
				cout << mas[i][j];
			}
			cout << endl;
		}
		cout << endl << r << " " << b << endl;*/
		cout << "Case #" << t << ": ";
		if ( r == true)
		{
			if ( b == true)
			{
				cout << "Both";
			}
			else
			{
				cout << "Red";
			}
		}
		else
		{
			if ( b == true)
			{
				cout << "Blue";
			}
			else
			{
				cout << "Neither";
			}
		}
		cout << endl;
	}
}