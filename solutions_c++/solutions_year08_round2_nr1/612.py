/*
Language:C++
*/

#include<iostream>
#include<fstream>
#include<string>
#include<vector>
#include<algorithm>

using namespace std;

int main()
{
	ofstream fout("A-small.out");
	ifstream fin("A-small-attempt1.in");

	int t;
	fin>>t;

	for(int i=0;i!=t;i++)
	{
		int n,a,b,c,d,x0,y0,m;
		fin>>n>>a>>b>>c>>d>>x0>>y0>>m;

		vector<long long> xv(n,0);
		vector<long long> yv(n,0);
		xv[0]=x0;
		yv[0]=y0;


		for(int u=1;u!=n;u++)
		{
			long long av=xv[u-1]*a;
			long long cv=yv[u-1]*c;
			xv[u]=(av+b)%m;
			yv[u]=(cv+d)%m;
		}

		int count=0;
		for(int t=0;t!=n;t++)
		{
			for(int j=t+1;j!=n;j++)
			{
				for(int k=j+1;k!=n;k++)
				{
					if((xv[t]+xv[j]+xv[k])%3==0)
					{
						if((yv[t]+yv[j]+yv[k])%3==0)
						{
						count++;
					}
					}
				}
			}
		}
		fout<<"Case #"<<i+1<<": "<<count<<endl;
	}
	return 0;
}