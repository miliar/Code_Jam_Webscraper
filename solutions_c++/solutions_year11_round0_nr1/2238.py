//Aleksander "kaalex" Kramarz

#include <cstdio>
#include <deque>
using namespace std;

int main()
{
	int t;
	scanf("%d", &t);
	for(int i = 1; i <= t; i++)
	{
		deque<pair<int,int> > v1, v2;
		int n, res = 0, x = 1, y = 1, u;
		char c[5];
		scanf("%d", &n);
		for(int j = 0; j < n; j++)
		{
			scanf("%s%d", c, &u);
			c[0]=='O' ? v1.push_back(make_pair(u,j)) : v2.push_back(make_pair(u,j));
		}
		u=0;
		while(!v1.empty() || !v2.empty())
		{
			bool q=0;
			if(!v1.empty())
			{
				if(x<v1[0].first)
					x++;
				else if(x>v1[0].first)
					x--;
				else if(u==v1[0].second)
				{
					q=1;
					u++;
					v1.pop_front();
				}
			}
			if(!v2.empty())
			{
				if(y<v2[0].first)
					y++;
				else if(y>v2[0].first)
					y--;
				else if(!q && u==v2[0].second)
				{
					u++;
					v2.pop_front();
				}
			}
			res++;
		}
		printf("Case #%d: %d\n", i, res);
	}
}



