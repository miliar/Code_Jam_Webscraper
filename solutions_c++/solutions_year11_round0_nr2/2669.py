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
char a[40][4];
char b[30][3];
char ans[200];
int main()
{
	int t, n,c,d;
	int i,j,ij,ji;
	ofstream fo("G:\\BSmallAns.txt",ios_base::out);
	scanf("%d",&t);
	for (j = 1; j<= t; j++)
	{
		cin>>c;
		for (i = 0; i< c; i++)
			cin>>a[i][0]>>a[i][1]>>a[i][2];
		cin>>d;
		for (i=0;i<d;i++)
			cin>>b[i][0]>>b[i][1];
		cin>>n;

		int m = 0;
		char ch;
		for (i=0;i<n;i++)
		{
			cin>>ch;
			if (m==0)
			{
				ans[0]=ch;
				m++;
			}
			else
			{
				ans[m] = ch;
				m++;
				for (ij = 0;ij<c;ij++)
				{
					if (a[ij][0] == ans[m-1] && a[ij][1] == ans[m-2])
					{
						ans[m-2] = a[ij][2];
						m--;
						break;
					}
					if (a[ij][0] == ans[m-2] && a[ij][1] == ans[m-1])
					{
						ans[m-2] = a[ij][2];
						m--;
						break;
					}
				}

				for (ij = 0; ij<m-1;ij++)
				{
					for (ji=0;ji<d;ji++)
					{
						if (ans[ij] == b[ji][0] && ans[m-1] == b[ji][1])
						{
							m = 0;
							break;
						}

						if (ans[ij] == b[ji][1] && ans[m-1] == b[ji][0])
						{
							m = 0;
							break;
						}
					}
				}
			}
		}
		


		fo<<"Case #"<<j<<": [";
		if (m > 0)
		{
			fo<<ans[0];
			for (i=1;i<m;i++)
				fo<<", "<<ans[i];
		}
		fo<<"]"<<endl;
	}

	return 0;
}