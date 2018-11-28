#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

const int MAX = 1002;

double M[MAX];
double C[MAX][MAX];
double fac[MAX];
double e[MAX];
int num[MAX];

void Init()
{
	M[1] = 0;
	M[2] = 1;
	for(int i=3; i<MAX; i++)
	{
		M[i] = (M[i-1] + M[i-2]) * (i-1);
	}
	
	for(int i=1; i<MAX; i++)
		for(int j=0; j<=i; j++)
			C[i][j] = j == 0 || j == i ? 1.0 : C[i-1][j-1] + C[i-1][j];	
	
	fac[1] = 1;
	for(int i=2; i<MAX; i++)
	{
		fac[i] = fac[i-1] * i;	
	}
	
	e[1] = 0;
	for(int n=2; n<MAX; n++)
	{
		double sum = 1.0;
		for(int i=1; i<n; i++)
		{
			sum += C[n][i] * M[i] / fac[n] * e[i];	
		}	
		e[n] = sum / (1.0 - C[n][n] * M[n] / fac[n]);
//		cout << "sd  " << n << "  " << e[n] << endl;
	}
}

int main()
{
	freopen("in.in", "r", stdin);
	freopen("out.out", "w", stdout);


	
//	Init();
	
	int T;	cin >> T;
	for(int cas=1; cas<=T; cas++)
	{
		int N;	cin >> N;
		for(int i=0; i<N; i++)
		{
			cin >> num[i];	
		}
		
		int cnt = 0;
		for(int i=0; i<N; i++)
		{
			int sum = 0;
			for(int j=0; j<N; j++)
			{
				sum += num[j] < num[i];	
			}
			cnt += sum != i;
		}
		printf("Case #%d: %.6f\n", cas, cnt <= 1 ? 0.0 : cnt*1.0);
	}
	
	
	return 0;	
}
