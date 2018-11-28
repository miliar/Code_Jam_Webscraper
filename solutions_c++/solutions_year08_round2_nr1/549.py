#include<fstream>
#include<iostream>
using namespace std;
#include<string>
#include<vector>

//#define MAX 1000000

//int x[MAX],y[MAX];

int main()
{
	ifstream fin;
	ofstream fout;
	fin.open("A-small-attempt0.in");
	fout.open("A-small.out");
	
	long long N,n, A, B, C, D, x0, y0, M;
	long long X,Y;
	long long ctr=0;
	
	vector <long long> x,y;
	
	fin>>N;
	for(int cas=1; cas<=N; cas++)
	{
		x.clear();
		y.clear();
		ctr=0;
		
		fin>>n>>A>>B>>C>>D>>x0>>y0>>M;
		
		X=x0;
		Y=y0;
		x.push_back(X);
		y.push_back(Y);
		
		for(int i=1; i<=n-1; i++)
		{
			X = (A * X + B)%M;
			Y = (C * Y + D)%M;
			x.push_back(X);
			y.push_back(Y);
		}
		
		for(int i=0; i<n; i++)
		{
			for(int j=i+1; j<n; j++)
			{
				for(int k=j+1; k<n; k++)
				{
					float xx = (float)(x[i]+x[j]+x[k])/3;
					float yy = (float)(y[i]+y[j]+y[k])/3;
					if(xx == (x[i]+x[j]+x[k])/3  && yy == (y[i]+y[j]+y[k])/3 )
						ctr++;
					
				}
			}
		}
			
		fout<<"Case #"<<cas<<": "<<ctr<<"\n";
	}
	
	return 0;
}
	
	

