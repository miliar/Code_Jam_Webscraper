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
int a[10005];
int main()
{
	ofstream fo("G:\\Ans.txt",ios_base::out);
	fo.setf(ios::fixed);
    fo.setf(ios::showpoint);
    fo.precision(8);
	ifstream fi("G:\\Cin.txt",ios_base::in);

	int t,n,l,h,i;
	//scanf("%d", &t);
	fi>>t;
	for (int k = 1; k<= t; k++)
	{
		fi>>n>>l>>h;
		for (i=0;i<n;i++)
			fi>>a[i];
		while(l<=h)
		{
			int ok = 0;
			for (i=0;i<n;i++)
			{
				if (a[i] % l != 0  && l % a[i] != 0)
				{
					ok = 1;
					break;
				}
			}

			if (ok == 0)
				break;

			l++;
		}

		fo<<"Case #"<<k<<": "<<endl;
		if (l>h)
			fo<<"NO"<<endl;
		else
			fo<<l<<endl;
	}
	return 0;
}