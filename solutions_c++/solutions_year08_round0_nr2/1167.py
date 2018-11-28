#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int		N, T, NA, NB;
char		start[10], arrive[10];
vector<pair<int, int> > eventList;

int	trans(char * a)
{
	return (a[0] - '0') * 600 + (a[1] - '0') * 60 + (a[3] - '0') * 10 + (a[4] - '0');  
}

int	main()
{
	int nCase;
	scanf("%d\n", &nCase);

	for (int nowCase = 1; nowCase <= nCase; ++nowCase)
	{
		eventList.clear();
		scanf("%d\n", &T);
		scanf("%d %d\n", &NA, &NB);
		N = NA + NB;
		for (int i = 0; i < NA; ++i)
		{
			scanf("%s %s\n", &start, &arrive);
			eventList.push_back( make_pair(trans(start), 2) );
			eventList.push_back( make_pair(trans(arrive) + T, 0) );
		}
		for (int i = 0; i < NB; ++i)
		{
			scanf("%s %s\n", &start, &arrive);
			eventList.push_back( make_pair(trans(start), 3) );
			eventList.push_back( make_pair(trans(arrive) + T, 1) );
		}

		sort(eventList.begin(), eventList.end());

		int x = 0, y = 0, x_need = 0, y_need = 0;
		for (int i = 0; i < eventList.size(); ++i)
		{
//			cout << eventList[i].first << ' ' << eventList[i].second << endl;
			switch (eventList[i].second)
			{
				case 0 : ++y; break;
				case 1 : ++x; break;
				case 2 : --x; break;
				case 3 : --y; break;
			}
			x_need >?= -x;
			y_need >?= -y;
		}
		printf("Case #%d: %d %d\n", nowCase, x_need, y_need);
	}
	return 0;
}
