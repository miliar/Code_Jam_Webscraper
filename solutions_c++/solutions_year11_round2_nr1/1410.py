#include<iostream>
#include<vector>
#include <algorithm>
#include <stack>
#include <string>
#include <map>

using namespace std;

unsigned long long gcd(unsigned long long a, unsigned long long b)
{
	unsigned long long t;
    while(b!= 0)
	{
       t = b;
       b = a % b;
       a = t;
    }
	return a;
}
int main()
{
	int tests;
	cin >> tests;
	for(int j = 0; j < tests; j++)
	{
		int N;
		cin >> N;
		int matrix[N][N];
		for(int i = 0; i < N; i++)
		{
			string rec;
			cin >> rec;
			for(int k = 0; k < N; k++)
			{
				char t = rec[k];
				if(t=='1')
					matrix[i][k] = 1;
				else if(t=='0')
					matrix[i][k] = 0;
				else
					matrix[i][k] = 2;
			}
		}
		double WP[N];
		int countT[N];
		double OWP[N];
		double OOWP[N];
		for(int i = 0; i < N; i++)
		{
			int count = 0;
			WP[i] = 0;
			countT[i] = 0;
			for(int k = 0; k < N; k++)
			{
				if(matrix[i][k]!=2)
				{
					WP[i]+=(double)matrix[i][k];
					count++;
					countT[i]++;
				}
			}
			WP[i]/=count;
			//cerr << WP[i] << endl;
		}
		for(int i = 0; i < N; i++)
		{
			int count = 0;
			OWP[i] = 0;
			for(int k = 0; k < N; k++)
			{
				if(matrix[i][k]!=2)
				{
					OWP[i]+=(WP[k]*countT[k]-(double)matrix[k][i])/(countT[k]-1);
					//cerr << k << ": " << countT[k] << ", " << matrix[i][k] << endl;
					count++;
				}
			}
			OWP[i]/=count;
			//cerr << OWP[i] << endl;
		}
		for(int i = 0; i < N; i++)
		{
			int count = 0;
			OOWP[i] = 0;
			for(int k = 0; k < N; k++)
			{
				if(matrix[i][k]!=2)
				{
					OOWP[i]+=OWP[k];
					count++;
				}
			}
			OOWP[i]/=count;
		}
		cout << "Case #" << j+1 << ":" << endl;
		for(int i = 0; i<N; i++)
			printf("%.8lf\n",0.25*WP[i]+0.5*OWP[i]+0.25*OOWP[i]);
	}
}