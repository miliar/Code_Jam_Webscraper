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
	int t, n;
	ofstream fo("G:\\ASmallAns.txt",ios_base::out);
	scanf("%d",&t);
	for (int j = 1; j<= t; j++)
	{
		scanf("%d",&n);
		int x = 0;
		int y = 0;
		int p = 1;
		int q = 1;
		int s = 0;
		char col;
		int pos = 0;
		for (int i=0;i<n;i++)
		{
			cin>>col>>pos;
			if (col == 'O')
			{
				s = abs(pos - p) + 1;
				if (x + s > y)
					x = x + s;
				else
					x = y +1;

				p = pos;
			}
			else
			{
				s = abs(pos - q) + 1;
				if (y + s > x)
					y = y + s;
				else
					y = x + 1;

				q = pos;
			}
		}
		
		if (x < y)
			x = y;

		fo<<"Case #"<<j<<": "<<x<<endl;
	}	

	return 0;
}