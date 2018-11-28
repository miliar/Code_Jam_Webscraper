#include <iostream>
#include <string.h>
#include <stdio.h>
#include <vector>
#include <set>
#include <map>
#include<math.h>
#include<sstream>
#include<fstream>
#include <algorithm>
using namespace std;

int main()
{
	ofstream fo("G:\\ASAns.txt",ios_base::out);
	fo.setf(ios::fixed);
    fo.setf(ios::showpoint);
    fo.precision(8);
	//ifstream fi("G:\\Cin.txt",ios_base::in);
	long t,i,j;
	long n;

	double x,y;

	double w1[200][2], w2[200], w3[200];
	char a[150][150];

	scanf("%d",&t);
	for (int k = 1; k<= t; k++)
	{
		scanf("%d", &n);
		for (i=0;i<n;i++)
			scanf("%s", &a[i]);

		for (i=0;i<n;i++)
		{
			x=0.0;y=0.0;
			for (j=0;j<n;j++)
			{
				if (a[i][j] != '.')
					x=x+1.0;
				if (a[i][j] =='1')
					y=y+1.0;
			}

			w1[i][0]=y;
			w1[i][1]=x;
		}

		for (i=0;i<n;i++)
		{
			x=0.0;y=0.0;
			for (j=0;j<n;j++)
			{
				if (a[i][j] != '.')
				{
					x=x+1.0;
					if (a[i][j] == '1')
						y = y+ w1[j][0]/(w1[j][1]-1.0);
					else
						y= y+(w1[j][0]-1.0)/(w1[j][1]-1.0);
				}
			}

			w2[i]=y/x;
		}

		for (i=0;i<n;i++)
		{
			x=0.0;y=0.0;
			for (j=0;j<n;j++)
			{
				if (a[i][j] != '.')
				{
					x=x+1.0;
					y=y+w2[j];
				}
			}

			w3[i]=y/x;
		}

		fo<<"Case #"<<k<<":"<<endl;

		for (i=0;i<n;i++)
		{
			double ans = 0.25*w1[i][0]/w1[i][1] + 0.5*w2[i] + 0.25*w3[i];
			fo<<ans<<endl;
		}


	}
	return 0;
}