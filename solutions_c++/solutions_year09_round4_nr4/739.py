#include <fstream>
#include <iostream>
#include <cmath>
#include <cstdlib>

using namespace std;
int x[3];
int y[3];
double r[3];
int main()
{
	ifstream fin("small1.in");
	ofstream fout("output.txt");
	int cases;
	fin >> cases;
	for(int cas=0;cas<cases;cas++)
	{
		int n;
		fin >> n;
		fout<< "Case #"<<cas+1<<": ";
		for(int i=0;i<n;i++)
		{
			fin>>x[i]>>y[i];
			fin>>r[i];
		}
		if (n==1)
			fout << r[0] << "\n";
		if (n==2)
			fout << max(r[0],r[1]) << "\n";
		if (n==3)
		{
			double minim=0;
			minim=sqrt(double((x[0]-x[1])*(x[0]-x[1])+(y[0]-y[1])*(y[0]-y[1])));
			minim+=r[0]+r[1];
			minim/=2;
			minim=max(minim,r[2]);
			double temp;
			temp=sqrt(double((x[1]-x[2])*(x[1]-x[2])+(y[1]-y[2])*(y[1]-y[2])));
			temp+=r[1]+r[2];
			temp/=2;
			temp=max(temp,r[0]);
			minim=min(temp,minim);
			temp=sqrt(double((x[0]-x[2])*(x[0]-x[2])+(y[0]-y[2])*(y[0]-y[2])));
			temp+=r[0]+r[2];
			temp/=2;
			temp=max(temp,r[1]);
			minim=min(temp,minim);
			fout << minim << "\n";
		}
	}
}