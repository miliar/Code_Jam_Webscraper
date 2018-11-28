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
char mp[60][60];
int main()
{
	ofstream fo("G:\\Ans.txt",ios_base::out);
	fo.setf(ios::fixed);
    fo.setf(ios::showpoint);
    fo.precision(8);
	ifstream fi("G:\\Cin.txt",ios_base::in);

	int t,r,c,i,j;
	//scanf("%d", &t);
	fi>>t;
	for (int k = 1; k<= t; k++)
	{
		fi>>r>>c;
		for (i=0;i<r;i++)
			fi>>mp[i];

		int ok = 0;
		for (i=0;i<r;i++)
		{
			for (j=0;j<c;j++)
			{
				if (mp[i][j] == '#')
				{
					if (j+1<c && mp[i][j+1] =='#' &&
						i+1<r && mp[i+1][j] == '#' &&
						mp[i+1][j+1] == '#')
					{
						mp[i][j] ='/';
						mp[i][j+1] ='\\';
						mp[i+1][j] ='\\';
						mp[i+1][j+1]='/';
					}
				}

				if (mp[i][j] == '#')
				{
					ok = 1;
					break;
				}				
			}

			if (ok == 1)
				break;
		}
		
		fo<<"Case #"<<k<<":"<<endl;
		if (ok == 1)
		{
			fo<<"Impossible"<<endl;
		}
		else
		{
			for (i=0;i<r;i++)
				fo<<mp[i]<<endl;
		}
	}

	return 0;
}