#include <iostream>
#include <fstream>
#include <string>
#include <math.h>
#include   <iomanip>
#include <algorithm>
#include <map>
using namespace std;
char table0[120][120];
double map1[120][120];
double table1[120];
double table2[120];
double table3[120];
double calRPI(double WP,double OWP,double OOWP)
{
	double RPI;
	RPI = 0.25 * WP + 0.50 * OWP + 0.25 * OOWP;
	return RPI;
}
int main() {
	ofstream fout ("test.out");
	ifstream fin ("test.in");
	int m,n;
	fin>>m;
	for(int i=0;i<m;i++)
	{
		fin>>n;
		for(int i=0;i<n;i++)
			for(int j=0;j<n;j++)
			{
				fin>>table0[i][j];
			}

			for(int i=0;i<n;i++)
			{
				int win=0;
				int al=0;
				for(int j=0;j<n;j++)
				{
					if(table0[i][j]=='.')
						continue;
					al++;
					if(table0[i][j]=='1')
						win++;
				}
				table1[i]=(double)win/al;
				for(int j=0;j<n;j++)
				{
					if(table0[i][j]=='.')
					{
						map1[i][j]=table1[i];
						continue;
					}
					if(table0[i][j]=='1')
					{
						map1[i][j]=(double)(win-1)/(al-1);
					}
					else
					{
						map1[i][j]=(double)win/(al-1);
					}
				}
			}
			for(int i=0;i<n;i++)
			{
				double sum=0;
				double num=0;
				for(int j=0;j<n;j++)
				{
					if(table0[i][j]=='.')
					{
						continue;
					}
					else
					{
						sum+=map1[j][i];
						num+=1;
					}
				}
				table2[i]=sum/num;
			}
			for(int i=0;i<n;i++)
			{
				double sum=0;
				double num=0;
				for(int j=0;j<n;j++)
				{
					if(table0[i][j]=='.')
					{
						continue;
					}
					else
					{
						sum+=table2[j];
						num+=1;
					}
				}
				table3[i]=sum/num;
			}
			double table4[120];
			fout<<"Case #"<<i+1<<":"<<endl;
			for(int i=0;i<n;i++)
			{
				table4[i]=calRPI(table1[i],table2[i],table3[i]);
				fout<<setprecision(10)<<table4[i]<<endl;
			}
	}
	return 0;
}