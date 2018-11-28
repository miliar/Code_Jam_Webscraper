#include<iostream.h>
#include<math.h>

int calGCD(int l, int m);

int main(int argc, char** argv)
{

	int C, N;
	int *u, *v, y;
	int gcdVal;

	cin >> C;
	
	for( int caseIndex = 0; caseIndex < C; caseIndex++ )
	{
		//cout << "Input N ";
		cin >> N;
		//cout << "Input K ";

		u = new int[N];
		v = new int[N - 1];

		for(int i = 0; i < N; i++)
		{
			cin >> u[i];
			//cout << u[i] << endl;
		}

		for(i = 0; i < (N - 1); i++)
		{
			v[i] = labs(u[i + 1] - u[i]);
			//cout << v[i] << endl;
		}

		gcdVal = v[0];

		for(i = 0; i < (N - 2); i++)
		{
			gcdVal = calGCD(gcdVal, v[i + 1]);
		}

		y = (gcdVal - (u[0] % gcdVal)) % gcdVal;

		//cout << gcdVal << endl;

		cout << "Case #" << (caseIndex + 1) << ": " << y << endl;


		delete [] u;
		delete [] v;
	}

	
	return 0;
}

int calGCD(int l, int m)
{
	int n; 

	if( (l * m) == 0 )
	{
		return (l + m);
	}

	n = l % m;

	while(n != 0)
	{
		l = m; 
		m = n;
		n = l % m;
	}

	return m;
}