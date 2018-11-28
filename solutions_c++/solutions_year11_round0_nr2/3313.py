#include <cstdio>
#include <queue>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
using namespace std;


bool combine(vector < char >& list, string comb)
{
	int len = (int)list.size();

	if( (comb[0] == list[len-1] && comb[1] == list[len-2]) || (comb[0] == list[len-2] && comb[1] == list[len-1]) )
	{
		list.pop_back();
		list.pop_back();
		list.push_back(comb[2]);
		return true;
	}
	return false;
}

bool oppose(vector < char >& list, string opp)
{
	int len = (int)list.size();

	bool isclear = false;

	if(list[len-1] == opp[0])
	{
		for(int i = 0; i < len-1; i++)
		{
			if(opp[1] == list[i])
			{
				isclear = true;
				break;
			}
		}
	}
	else if(list[len-1] == opp[1])
	{
		for(int i = 0; i < len-1; i++)
		{
			if(opp[0] == list[i])
			{
				isclear = true;
				break;
			}
		}
	}
	if( isclear ) list.clear();

	return false;
}

int main()
{
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);

	int testCase = 0;
	scanf("%d", &testCase);

	for(int tc = 1; tc <= testCase; tc++)
	{
		int c = 0;
		int d = 0;
		int n = 0;
		
		string invoke;
		vector < char > anslist;

		cin >> c;
		vector < string > basestr(c);
		for(int i = 0; i < c ; i++) cin >> basestr[i];
		
		cin >> d;
		vector < string > oppstr(d);
		for(int i =  0; i < d; i++) cin >> oppstr[i];

		cin >> n;
		if( 0 < n ) cin >> invoke;

		for(int i = 0; i < n; i++)
		{
			anslist.push_back(invoke[i]);

			
			bool iscombine = false;
			for(int j = 0; j < c && 1 < (int)anslist.size(); j++)
			{
				iscombine = combine(anslist, basestr[j]);
				if( true == iscombine ) break;
			}
			
			if( false == iscombine )
			{
				bool isremove = false;
				for(int j = 0; j < d && 1 < (int)anslist.size(); j++)
				{
					isremove = oppose(anslist, oppstr[j]);
					if( true == isremove ) break;
				}
			}

		
		}

		printf("Case #%d: ", tc);
		printf("[");
		int len = (int)anslist.size() -1;
		for(int i = 0; i < len; i++)
		{
			printf("%c, ", anslist[i]);
		}
		if( 0 < anslist.size() ) printf("%c", anslist[len]);

		printf("]\n");
	}
	return 0;
}