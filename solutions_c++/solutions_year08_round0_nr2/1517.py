#include <algorithm>
#include <vector>
#include <list>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <iterator>
#include <numeric>
#include <utility>
#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <fstream>
#include <string>
using namespace std;

#define sqr(x)		((x)*(x))

int main()
{
	int N=0;
	scanf("%d", &N);

	for(int j=1; j<=N; j++)
	{
		int T=0;
		scanf("%d", &T);

		int NA, NB;
		scanf("%d %d", &NA, &NB);

		vector< pair<int, int> > TA, TB;

		for(int i=0; i<NA; i++)
		{
			char buff[256], buff2[256];
			scanf("%s %s", buff, buff2);

			int h1 =(buff[0]-'0')*10+buff[1]-'0';
			int m1=(buff[3]-'0')*10+buff[4]-'0';
			int h2 =(buff2[0]-'0')*10+buff2[1]-'0';
			int m2=(buff2[3]-'0')*10+buff2[4]-'0';

			TA.push_back( make_pair(h1*60+m1, h2*60+m2) ); 

			//printf("s=%d, e=%d\n", h1*60+m1, h2*60+m2);
		}
		sort(TA.begin(), TA.end());

		for(int i=0; i<NB; i++)
		{
			char buff[256], buff2[256];
			scanf("%s %s", buff, buff2);

			int h1 =(buff[0]-'0')*10+buff[1]-'0';
			int m1=(buff[3]-'0')*10+buff[4]-'0';
			int h2 =(buff2[0]-'0')*10+buff2[1]-'0';
			int m2=(buff2[3]-'0')*10+buff2[4]-'0';

			TB.push_back( make_pair(h1*60+m1, h2*60+m2) ); 

			//printf("s=%d, e=%d\n", h1*60+m1, h2*60+m2);
		}
		sort(TB.begin(), TB.end());

		int n1=0, n2=0;

		vector<int> AFree, BFree;

		int p=0;
		int q=0;

		while(p<TA.size() && q<TB.size())
		{
			if(TA[p].first<TB[q].first)
			{
				if(AFree.size()>0 && AFree[0]<=TA[p].first)
				{
					AFree.erase(AFree.begin());
				}
				else
				{
					n1++;
				}

				BFree.push_back(TA[p].second+T);
				sort(BFree.begin(), BFree.end());
				p++;
			}
			else
			{
				if(BFree.size()>0 && BFree[0]<=TB[q].first)
				{
					BFree.erase(BFree.begin());
				}
				else
				{
					n2++;
				}

				AFree.push_back(TB[q].second+T);
				sort(AFree.begin(), AFree.end());
				q++;
			}
		}

		n1+=TA.size()-p;
		n2+=TB.size()-q;

		printf("Case #%d: %d %d\n", j, n1, n2);
	}

	return 1;
}
