#include<stdio.h>
#include<string>
#include<cmath>
#include<vector>

using namespace std;

int main()
{
	freopen("In.in","r",stdin);
	freopen("Out.out","w",stdout);
	int t;
	scanf("%d",&t);
	for(int x = 1; x <= t;x++)
	{
		int n;
		scanf("%d",&n);
		vector< pair<int,int> > oseq,bseq;
		for(int i = 0; i < n;i++)
		{
			char r;int m;
			scanf(" %c%d",&r,&m);
			if (r == 'O') oseq.push_back(make_pair(i,m));
			else bseq.push_back(make_pair(i,m));
		}
		int opos = 1;
		int bpos = 1;
		int opointer = 0;
		int bpointer = 0;
		int sec = 0;
		while(opointer < oseq.size() || bpointer < bseq.size())
		{
			if (opointer == oseq.size())
			{
				sec += abs(bseq[bpointer].second - bpos) + 1;
				bpos = bseq[bpointer++].second;
			}
			else if (bpointer == bseq.size())
			{
				sec += abs(oseq[opointer].second - opos) + 1;
				opos = oseq[opointer++].second;
			}
			else
			{
				if (bseq[bpointer].first < oseq[opointer].first)
				{
					int bcost = abs(bseq[bpointer].second - bpos) + 1;
					if (bcost >= abs(oseq[opointer].second - opos)) opos = oseq[opointer].second;
					else
					{
						if (opos > oseq[opointer].second) opos -= bcost;
						else opos += bcost;
					}
					sec += bcost;
					bpos = bseq[bpointer].second;
					bpointer ++;
				}
				else
				{
					int ocost = abs(oseq[opointer].second - opos) + 1;
					if (ocost >= abs(bseq[bpointer].second - bpos)) bpos = bseq[bpointer].second;
					else
					{
						if (bpos > bseq[bpointer].second) bpos -= ocost;
						else bpos += ocost;
					}
					sec += ocost;
					opos = oseq[opointer].second;
					opointer ++;
				}
			}
		}
		printf("Case #%d: %d\n",x,sec);
	}
}