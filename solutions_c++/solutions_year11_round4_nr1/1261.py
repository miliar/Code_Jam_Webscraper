#include <iostream>
#include <vector>
#include <cstdio>
#include <algorithm>
using namespace std;

struct way
{
	int s;
	int idx;
	int e;
	int speed;
	double cost;
	way(int a, int b, int c, int d):idx(a), s(b), e(c), speed(d) {} 
};

bool cmp1(const way& w1, const way& w2)
{
	return w1.s < w2.s;
}
bool cmp2(const way& w1, const way& w2)
{
	return w1.speed < w2.speed;
}

int main()
{
	int T;
	scanf("%d", &T);
	for(int tcase=1; tcase<=T; ++tcase)
	{
		double ans=0.0;
		double len=0.0;
		int _len, ss, sr, srt, nw;
		scanf("%d %d %d %d %d", &_len, &ss, &sr, &srt, &nw);
		len = _len;
		vector<way> ways;
		for(int i=0; i <nw; ++i)
		{
			int s, e, speed;
			scanf("%d %d %d", &s, &e, &speed);
			ways.push_back( way(i, s, e, speed+ss) );
		}

		int begin=0;
		sort(ways.begin(), ways.end(), cmp1);
		int last=0;
		for(int i=0; i < nw; ++i)
		{
			if( begin < ways[i].s )
			{
				ways.push_back(way(-1, begin, ways[i].s, ss));
				begin = ways[i].e;
			}
			last = max(last, ways[i].e);
			begin = ways[i].e;
		}
		if( last != _len )
			ways.push_back( way(-1, last, _len, ss) );

		sort(ways.begin(), ways.end(), cmp1);
		for(int i=0; i < (int)ways.size(); ++i)
		{
			ways[i].speed -= ss;
			ways[i].idx = i;
		}

		sort(ways.begin(), ways.end(), cmp2);
		double SRT = srt;
		bool run=true;
		for(int i=0; i < (int)ways.size(); ++i)
		{
			way& w = ways[i];
			double far = w.e-w.s;
			if(run==false)
			{
				ways[i].cost = far/((double)ss+w.speed);
			}
			else
			{
				double speed = w.speed + sr;
				double _max = speed * SRT;
				if( _max < far )
				{
					double remain = far - _max;
					w.cost = _max/speed;
					w.cost += ((double)remain/((double)w.speed+ss));
					run=false;

				}
				else
				{
					w.cost = far/speed;
					SRT -= ways[i].cost;
				}
			}
			//printf("%d->%d[%.2f]\n", w.s, w.e, w.cost);
		}	
		for(int i=0; i < (int)ways.size(); ++i)
			ans += ways[i].cost;
		printf("Case #%d: %f\n", tcase, ans);
	}
	return 0;
}
