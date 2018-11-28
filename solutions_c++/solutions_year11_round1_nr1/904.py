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
	ofstream fo("G:\\ASmallAns.txt",ios_base::out);
	//ifstream fi("G:\\Cin.txt",ios_base::in);
	long t,p,q;
	__int64 n;
	scanf("%d",&t);
	for (int j = 1; j<= t; j++)
	{
		scanf("%I64d %d %d", &n,&p,&q);

		bool ans = true;

		if (p != 0 && q == 0)
			ans = false;

		int y = 100;
		int x = 100;
		for (int i=2;i<=100;i++)
		{
			while(y%i==0 && p%i==0)
			{
				y = y/i;
				p = p/i;
			}

			while(x%i==0 && q%i==0)
			{
				x = x/i;
				q = q/i;
			}
		}

		

		if (y > n)
			ans = false;

		if (y-p != 0 && x-q == 0)
			ans = false;
		if (ans == true)
			fo<<"Case #"<<j<<": Possible"<<endl;
		else
			fo<<"Case #"<<j<<": Broken"<<endl;
	}

	return 0;

}