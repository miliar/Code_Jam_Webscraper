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
	int t, n,j;
	ofstream fo("G:\\CSmallAns.txt",ios_base::out);

	scanf("%d",&t);
	for (j = 1; j<= t; j++)
	{
		cin>>n;
		long ans = 0;
		long cur = 0;
		long m = 10000000;
		long k;
		for (int i = 0; i < n; i++)
		{
			cin>>k;
			if (m > k)
				m = k;
			ans += k;
			cur = cur^k;
		}

		if (cur == 0)
			fo<<"Case #"<<j<<": "<<ans - m<<endl;
		else
			fo<<"Case #"<<j<<": NO"<<endl;

	}

	return 0;
}