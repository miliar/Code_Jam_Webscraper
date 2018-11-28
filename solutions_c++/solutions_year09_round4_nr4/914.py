

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <string>
#include <map>
#include <algorithm>
#include <cstdlib>
#include <cstdio>
#include <cmath>
using namespace std;

int x[31];
int y[31];
int r[31];
double dis[3][3];
int main()
{
	ifstream inf("D-small-attempt0.in.txt");
	ofstream outf("out.txt");

	int T;
	double ret=0;
	inf>>T;
	for(int t=0;t<T;t++)
	{
		int n;
		inf>>n;
		for(int i=0;i<n;i++)
		{
			inf>>x[i]>>y[i]>>r[i];
		}
		if(n==1)
			ret=r[0];
		if(n==2)
			ret=max(r[1],r[0]);
		else
		{
		for(int i=0;i<n;i++)
		{
			for(int j=i+1;j<n;j++)
			{
				dis[i][j]=sqrt(pow((x[i]-x[j]),2.0)+pow(y[i]-y[j],2.0))+r[i]+r[j];
			}
		}
		double a[3];
		a[0]=dis[0][1];
		a[1]=dis[1][2];
		a[2]=dis[0][2];
		sort(a,a+3);
		ret=a[0]/2;
		for(int i=0;i<n;i++)
			ret=max(ret,double(r[i]));
		}
		outf<<"Case #"<<t+1<<": "<<ret<<endl;
	}
	return 0;
}
