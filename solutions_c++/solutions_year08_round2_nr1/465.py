#include<iostream>
#include<sstream>
#include<vector>
#include<string>
#include<algorithm>

using namespace std;

class CropTriangles
{
public:
	long long NumberOfTriangles(long long x[10001], long long y[10001], int n)
	{
		long long count = 0;

		for(int i=0;i<n;i++)
		{
			for(int j=i+1;j<n;j++)
			{
				for(int k=j+1;k<n;k++)
				{
					if((x[i] + x[j] + x[k])%3 == 0)
					{
						if((y[i] + y[j] + y[k])%3 == 0)
						{
							count++;
							//cout<<x[i]<<","<<y[i]<<" "<<x[j]<<","<<y[j]<<" "<<x[k]<<","<<y[k]<<" "<<endl;
						}
					}
				}
			}
		}

		return count;
	}
};

int main()
{
	int N;
	cin>>N;

	for(int i=0;i<N;i++)
	{
		int n, A, B, C, D, x0, y0, M;

		cin>>n>>A>>B>>C>>D>>x0>>y0>>M;

		long long x[10001], y[10001];
		memset(x, 0, sizeof(x));
		memset(y, 0, sizeof(y));
		x[0] = x0;
		y[0] = y0;

		for(int j=1;j<n;j++)
		{
			x[j] = (x[j-1]*A + B) % M;
			y[j] = (y[j-1]*C + D) % M;
		}

		CropTriangles ct;
		cout<<"Case #"<<i+1<<": "<<ct.NumberOfTriangles(x, y, n)<<endl;
	}

	return 0;
}