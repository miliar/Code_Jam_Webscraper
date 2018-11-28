//#pragma comment(linker, "/STACK:64000000")
#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif
	int n;
	scanf("%d\n",&n);
	vector<int> org;
	vector<int> blu;
	vector<pair<int,char> > psl;
	for(int i = 0; i < n; i++)
	{

		int m;
		scanf("%d ",&m);
		for(int j = 0; j < m; j++)
		{
			char c;
			int d;
			scanf("%c %d ",&c,&d);
			if(c == 'O')
				org.push_back(d);
			else
				blu.push_back(d);
			psl.push_back(make_pair(d,c));
		}
		scanf("\n");
		int pO = 1;
		int pB  = 1;
		int wereO = 1;
		int wereB = 1;
		int time = 0;
		for(int t = 0; t < psl.size(); t++)
		{
			if(psl[t].second == 'O')
			{

				int tarO = psl[t].first;
				int tarB = pB > blu.size() ? wereB : blu[pB - 1];
				while(1)
				{
					time++;
					if(wereO == tarO)
					{
						if(wereB > tarB)
							wereB--;
						else if(wereB < tarB)
							wereB++;
						break;
					}
					if(wereO > tarO)
						wereO--;
					else if(wereO < tarO)
						wereO++;

					if(wereB > tarB)
						wereB--;
					else if(wereB < tarB)
						wereB++;
				}
				pO++;
				//time++;
			}
			else if(psl[t].second == 'B')
			{
				int tarB = psl[t].first;
				int tarO = pO > org.size()  ? wereO : org[pO - 1];
				while(1)
				{
					time++;
					if(wereB == tarB)
					{
						if(wereO > tarO)
							wereO--;
						else if(wereO < tarO)
							wereO++;
						break;
					}
					if(wereO > tarO)
						wereO--;
					else if(wereO < tarO)
						wereO++;

					if(wereB > tarB)
						wereB--;
					else if(wereB < tarB)
						wereB++;


				}
				pB++;
				//time++;
			}
		}
		printf("Case #%d: %d\n",i + 1,time);
		org.clear();
		blu.clear();
		psl.clear();

	}
	return 0;
}
