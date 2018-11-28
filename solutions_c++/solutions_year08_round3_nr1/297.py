#include <stdio.h>
#include <stdlib.h>

#include <string>
#include <vector>
#include <map>
#include <iostream>
#include <algorithm>

#include <math.h>

#define PI 2*acos(0.0)
typedef long long int int64;
typedef unsigned long long int uint64;

using namespace std;
int main()
{
	int64 i,j,k,l,m,n;
	int64 testId, nTests;

	cin >> nTests;
	for(testId=1;testId<=nTests;testId++)
	{
		cout << "Case #" << testId << ": ";
		//XXX  -- Read input --  XXX
		int64 p, k, l;
		cin >> p >> k >> l;
		vector<int64> f;
		for (i=0;i<l;i++)
		{
			int64 tmp;
			cin >> tmp;
			f.push_back(tmp);
		}
		sort(f.begin(), f.end());
		vector<int64>::reverse_iterator iter;
		int64 tot=0;
		int64 cur_k=0;

		for (iter=f.rbegin();iter!=f.rend();iter++)
		{
			tot+=(*iter)*((cur_k/k)+1);
			cur_k++;
		}
		/*
		//scanf("%s %s", p1, p2);
		char str[1024];

        gets(str);
        if (str[0]=='\0')
        	gets(str);
		*/


		//XXX  -- Process input --  XXX







		//XXX  -- Print output --  XXX
		cout<<tot<<endl;



	}

	return 0;
}
