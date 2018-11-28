#include <iostream>
#include <cstdio>
#include <queue>
#include <list>

struct event_t
{
	int x;
	int t;
};

int main(void)
{
	freopen("bottrust.in","r",stdin);

	int tests;
	std::cin>>tests;
	for (int z=0; z<tests; z++)
	{
		int pos[2]={1,1};

		std::list<event_t> todo[2];

		int nodes;
		std::cin>>nodes;
		for (int i=0; i<nodes; i++)
		{
			event_t ev={0,i};
			char c;
			std::cin>>c>>ev.x;
			c=(c=='B'?0:1);
			todo[c].push_back(ev);
		}

		int moves=0;
		for (moves=0; todo[0].size()+todo[1].size(); moves++){ bool pressed=0;
			for (int q=0; q<2; q++)
				if (!todo[q].empty())
							if (pos[q]<todo[q].front().x) pos[q]++;
					else	if (pos[q]>todo[q].front().x) pos[q]--;
					else	if (pos[q]==todo[q].front().x && (todo[!q].empty() || todo[q].front().t<todo[!q].front().t) && !pressed)
					{
						todo[q].pop_front();
						pressed=1;
					}
		}
		std::cout<<"Case #"<<z+1<<": "<<moves<<std::endl;
	}
}
