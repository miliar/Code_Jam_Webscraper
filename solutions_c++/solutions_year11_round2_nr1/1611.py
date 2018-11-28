#include <iostream>
#include <iomanip>
using namespace std;

#define MAX 200

int T;
int N;
char A[MAX][MAX];

double WP[MAX], OWP[MAX], OOWP[MAX], RPI[MAX];

double wp(int x, int ex)
{
	double s = 0, n = 0;
	for (int i=0; i<N; ++i)
	{
		if ( i==ex )
			continue;

		s += A[x][i] == '1';
		n += A[x][i] != '.';
	}
	return s / n;
}

int main()
{
	cin >> T;
	cout << setprecision(10);
	for (int test=1; test<=T; ++test)
	{
		cin >> N;
		char tmp[2];
		cin.getline(tmp, 2);
		for (int i=0; i<N; ++i)
			cin.getline((char*)(A+i), N+1);

		for (int i=0; i<N; ++i)
		{
			WP[i] = wp(i, -1);

			OWP[i] = 0;
			double nr = 0;
			for (int j=0; j<N; ++j)
			{
				OWP[i] += (i!=j && A[i][j]!='.') * wp(j, i);
				nr += (i!=j && A[i][j]!='.');
			}
			OWP[i] /= nr;
		}
		for (int i=0; i<N; ++i)
		{
			OOWP[i] = 0;
			double nr = 0;
			for (int j=0; j<N; ++j)
			{
				OOWP[i] += (i!=j && A[i][j]!='.') * OWP[j];
				nr += (i!=j && A[i][j]!='.');
			}
			OOWP[i] /= nr;

			RPI[i] = 0.25 * WP[i] + 0.5 * OWP[i] + 0.25 * OOWP[i];
		}

		cout << "Case #" << test << ":" << endl;
		for (int i=0; i<N; ++i)
			cout << RPI[i] << endl;
	}
	return 0;
}
