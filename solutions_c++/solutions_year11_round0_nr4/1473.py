/*
 * main.cpp
 *
 *  Created on: 2011/5/7
 *      Author: lauer
 */
#include<iostream>
#include<fstream>
#include<iomanip>
using namespace std;

double d[10000];
double c[100][100];
long long f[12];
double e[100];
int x[15];
bool y[15];
int main()
{
	ofstream fout("ans");
	int t;
	int n,k,s,r,a;

	d[1] = 0;
	d[2] = 1;
	f[0] = f[1] = 1;
	for(int i=2;i<12;i++)
		f[i] = i*f[i-1];
	for(int i=3;i<15;i++)
		d[i] = (i-1)*(d[i-1]+d[i-2]);
	c[0][0] = c[1][0] = c[1][1] = 1;
	for(int i=2;i<15;i++)
	{
		c[i][0] = 1;
		for(int j=1;j<i;j++)
			c[i][j] = c[i-1][j-1]+c[i-1][j];
		c[i][i] = 1;
	}
	e[0] = e[1] = 0.0;
	e[2] = 2.0;

	for(int i=3;i<11;i++)
	{
		e[i] = 1.0;
		for(int j=1;j<i-1;j++)
			e[i] += (double)(c[i][j]*d[i-j]*e[i-j])/(double)f[i];
		e[i] *= ((double)f[i]/((double)f[i]-d[i]));
		cout << e[i] << ' ';
	}
	cout << endl;
	cin >> t;
	for(int i=1;i<=t;i++)
	{
		double ans = 0;
		cin >> n;
		for(int j=1;j<=n;j++)
			cin >> x[j];
		for(int j=0;j<15;j++)
			y[j] = false;
		for(int j=1;j<=n;j++)
		{
			if(!y[j])
			{
				if(x[j]==j)
					y[j] = true;
				else
				{
					s = 1;
					r = j;
					y[j] = true;
					while( !y[x[r]] )
					{
						s++;
						y[r] = true;
						r = x[r];
					}
					//cout << "s is " << s << endl;
					ans += e[s];
				}
			}
		}

		/*if(r!=0)
			fout << "Case #" << i << ": NO" << endl;
		else*/
		fout << "Case #" << i << ": " << fixed << setprecision(6) << ans << endl;
	}
}
