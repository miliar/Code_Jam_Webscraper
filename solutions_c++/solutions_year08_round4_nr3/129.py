#include <iostream>

using namespace std;

int x[1001];
int y[1001];
int z[1001];
int p[1001];

int N;

int d[14][3] = {{0,0,1},{0,1,0},{1,0,0},{0,0,-1},{0,-1,0},{-1,0,0},
			 {1,1,1},{1,1,-1},{1,-1,1},{-1,1,1},
			{-1,-1,1},{-1,1,-1},{1,-1,-1},{-1,-1,-1}};

double myabs(double a, double b)
{
	if (a > b)
		return a-b;
	else
		return b-a;
}

double gao(double mx, double my, double mz)
{
	double res = 0;
	for (int i = 1; i <= N; i++)
	{
		double temp = ( ( myabs(x[i], mx) + myabs(y[i], my) + myabs(z[i], mz) ) / p[i] );
		if (temp > res)
			res = temp;
	}
	return res;
}

double mysearch(double mx, double my, double mz, double step, double crt)
{
	//cout << "trying: " << "(" << mx << ", " << my << ", " << mz << ")" << ": " << gao(mx, my, mz) << " step: " << step << endl;
	
	if (step < 1e-7)
		return gao(mx, my, mz);
		
	double min = crt;
	int index = -1;
	for (int i = 0; i < 14; i++)
	{
		double temp = gao(mx+d[i][0]*step, my+d[i][1]*step, mz+d[i][2]*step);
		
		//cout << "\tpoint : (" << mx+d[i][0]*step << "," <<  my+d[i][1]*step << "," << mz+d[i][2]*step << ") dist: " << temp << endl; 
	
		if (min - temp > 1e-7 )
		{
			min = temp;
			index = i;
		}
	}
	if (index == -1)
	{
		//if no better solution
		step *= 0.1;
		return mysearch(mx, my, mz, step, crt);
	}
	else
		return mysearch(mx+d[index][0]*step, my+d[index][1]*step, mz+d[index][2]*step, step, min);
}

int main()
{
	int T;
	cin >> T;
	for (int casenum = 1; casenum <= T; casenum++)
	{
		cin >> N;
		for (int i = 1; i <= N; i++)
			cin >> x[i] >> y[i] >> z[i] >> p[i];
		double res = mysearch(500000, 500000, 500000, 10000, 2147483647);
		printf("Case #%d: %.6lf", casenum, res);
		cout << endl;
	}
	return 0;
}
