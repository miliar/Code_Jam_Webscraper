#include <iostream>
#include <map>

using	namespace	std;

const	int	maxtime = 24 * 60;

char	s1[20], s2[20];
int	t, na, nb;
int	cases;
multimap<pair<int, int>, int>	events;

inline	int	trans(char *s)
{
	int	h = (s[0] - '0') * 10 + (s[1] - '0');
	int	m = (s[3] - '0') * 10 + (s[4] - '0');
	return	h * 60 + m;
}

void	solve()
{
	scanf("%d%d%d", &t, &na, &nb);
	for (int i = 0; i < na; ++i)
	{
		scanf("%s %s", s1, s2);
		events.insert(make_pair(make_pair(trans(s1), 3), trans(s2))); // 3 means train from A to B
	}

	for (int i = 0; i < nb; ++i)
	{
		scanf("%s %s", s1, s2);
		events.insert(make_pair(make_pair(trans(s1), 4), trans(s2))); // 4 means train from B to A
	}

	int	ansa = 0, ansb = 0;
	int	hasa = 0, hasb = 0;
	while (!events.empty())
	{
		map<pair<int, int>, int>::iterator iter = events.begin();

		int	what = iter->first.second;
		int	when = iter->second;
		events.erase(iter);

		switch (what)
		{
		case 3:
			if (hasa == 0)
				++ansa;
			else
				--hasa;
			if (when + t < maxtime)
				events.insert(make_pair(make_pair(when + t, 2), 0));
			// 2 means a train is available at B
			break;
		case 4:
			if (hasb == 0)
				++ansb;
			else
				--hasb;
			if (when + t < maxtime)
				events.insert(make_pair(make_pair(when + t, 1), 0));
			// 1 means a train is available at A
			break;
		case 1:
			++hasa;
			break;
		case 2:
			++hasb;
			break;
		}
	}
	printf("Case #%d: %d %d\n", ++cases, ansa, ansb);
}

int	main()
{
	int	t;
	scanf("%d", &t);
	while (t--)	solve();
	return	0;
}
