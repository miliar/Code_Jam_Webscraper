#include <cstdio>
#include <utility>
#include <algorithm>
#include <memory.h>
#include <set>
using namespace std;
#define MP make_pair
#define X first
#define Y second

int in(int x,int y) {	return x>=0 && y>=0; }

int main()
{
//	freopen("c.in","r",stdin);	
	freopen("C-small-attempt2.in","r",stdin);
	freopen("c.out","w",stdout);
	
	set<pair<int,int> > m[2];

	int t,r,x1,y1,x2,y2;
	scanf("%d",&t);
	for(int ti = 0;ti < t;ti++)
	{
		scanf("%d",&r);
		m[0].clear();
		m[1].clear();
		for(int i=0;i<r;i++)
		{
			scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
			if(x1 > x2) swap(x1,x2);
			if(y1 > y2) swap(y1,y2);			
			for(int x = x1-1;x < x2;x++)
				for(int y = y1-1;y < y2;y++)			
					m[0].insert(MP(x,y));
		}
					
		int res = 0;
		int result = 0;
		while(1)
		{
			m[res^1].clear();
			for(set<pair<int,int> >::iterator it = m[res].begin();it != m[res].end();it++)
			{
				if(m[res].count(MP(it->X+1,it->Y - 1)))
					m[res^1].insert(MP(it->X+1,it->Y));
					
				if(m[res].count(MP(it->X-1,it->Y)) || m[res].count(MP(it->X,it->Y - 1)))
					m[res^1].insert(MP(it->X,it->Y));					
			}
			result++;
			if(m[res^1].size() == 0) break;
			res ^= 1;
		}
		printf("Case #%d: %d\n",ti+1,result);
		
	}
	return 0;
}