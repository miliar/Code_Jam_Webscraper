
#include <iostream>
#include <string>
#include <vector>
#include <set>

#include <stdio.h>

using namespace std;

struct Score;
struct Planet;

struct Score
{
	int prev;
	int len;
	int thr;
	set<int> thrs;

	bool betterThan(Score &s);
	void extend(Planet *p, int p1, int p2);

	Score()
	{
		prev = -1;
		len = -1;
		thr = 0;
		thrs.clear();
	}

	Score(const Score &o)
	{
		prev = o.prev;
		len = o.prev;
		thr = o.thr;
		thrs.insert(o.thrs.begin(), o.thrs.end());
	}
};


struct Planet
{
	int id;
	Score s;
	vector<int> neigh;
};


bool Score::betterThan(Score &s)
{
	if (len == -1) return false;
	if (s.len == -1) return true;
	if (s.len > len) return true;
	if (s.len == len && s.thr < thr) return true;
	return false;
}

void Score::extend(Planet *p, int p1, int p2)
{
	len = p[p1].s.len + 1;
	prev = p1;
	set<int> path;
	int pr = prev;
	while (pr != -1)
	{
		path.insert(pr);
		pr = p[pr].s.prev;
	}
	for (vector<int>::iterator i = p[p2].neigh.begin(); i != p[p2].neigh.end(); ++i)
	{
		if (path.find(*i) == path.end()) thrs.insert(*i);
	}

	thrs.erase(p2);
	thrs.erase(p1);

	thr = thrs.size();
}


int getMin(set<int> &cons, Planet* p)
{
	Score min;
	int minid = -1;

	for (set<int>::iterator i = cons.begin(); i != cons.end(); ++i)
	{
		if (min.betterThan(p[*i].s)) continue;
		min = p[*i].s;
		minid = *i;
	}

	return minid;
}

int main()
{
	int N;

	cin >> N;

	for (int n = 1; n <= N; n++)
	{
		int P, W;
		Planet p[500];
		set<int> thr, done;

		cin >> P >> W;

		string worm;
		for (int i = 0; i < W; i++)
		{
			int f, t;
			cin >> worm;
			sscanf(worm.c_str(), "%d,%d", &f, &t);
			p[f].neigh.push_back(t);
			p[t].neigh.push_back(f);
		}

		thr.clear();
		done.clear();

		p[0].s.len = 0;
		p[0].s.thr = p[0].neigh.size();
		p[0].s.thrs.insert(p[0].neigh.begin(), p[0].neigh.end());
		thr.insert(0);

		int c = getMin(thr, p);

		while (true)
		{
			for (vector<int>::iterator i = p[c].neigh.begin(); i != p[c].neigh.end(); ++i)
			{
				Score s2 = p[c].s;
				s2.extend(p, c, *i);
				if (s2.betterThan(p[*i].s)) p[*i].s = s2;
				if (done.find(*i) == done.end()) thr.insert(*i);
			}

			thr.erase(c);
			done.insert(c);

			if (c == 1) break;

			c = getMin(thr, p);
		}

		/*
		for (int i = 0; i < P; i++)
		{
			cout << "Planet " << i << ": " << p[i].s.len << " " << p[i].s.thr << " " << p[i].s.prev << endl;
		}
		*/

		cout << "Case #" << n << ": " << p[p[1].s.prev].s.len << " " << p[p[1].s.prev].s.thr << endl;
	}
}

