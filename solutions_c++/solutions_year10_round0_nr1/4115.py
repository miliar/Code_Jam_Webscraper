/*
ID: tecnoyo1
PROG: palsquare
LANG: C++
*/
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;


int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int cases;
	cin >> cases;
	for (int c = 1; c <= cases; ++c)
	{
		long long snappers,snaps;
		cin >> snappers >> snaps;
		int needed_number=0;
		for(int i=0;i<snappers;i++)
			needed_number += 1<<i;
		if(snaps > needed_number)
		{
			if(((snaps-needed_number)%(needed_number+1)) == 0)
				printf("Case #%d: ON\n",c);
			else
				printf("Case #%d: OFF\n",c);
		}
		else if (snaps == needed_number)
		{
			printf("Case #%d: ON\n",c);
		}
		else
		{
			printf("Case #%d: OFF\n",c);
		}
	}
	return 0;
}
