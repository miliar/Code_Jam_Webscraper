#include <algorithm>
#include <iostream>
#include <map>
#include <cstdio>
#include <string>
#include <vector>
#include <queue>

using namespace std;

#define MAX_N 100
#define MAX_NA 100
#define MAX_NB 100

int parse_time(const string& s)
{
	int hh,mm;
	sscanf(s.c_str(), "%d:%d",&hh,&mm);
	return hh*60+mm;
}

vector<pair<int,int> > get_schedule(int n)
{
	vector<pair<int,int> > a;
	for(int i=0;i<n;i++)
	{
		string depart,arrive;
		cin >> depart >> arrive;
		a.push_back(make_pair(parse_time(depart),parse_time(arrive)));
	}
	return a;
}

struct event
{
	int station, type, time;
	event(int x,int y,int z) : station(x), type(y), time(z) { }
	bool operator<(const event& x) const { return time > x.time; }
};

pair<int,int> solve(void)
{
	int t;
	cin >> t;

	int na, nb;
	cin >> na >> nb;

	vector<pair<int,int> > a(get_schedule(na));
	vector<pair<int,int> > b(get_schedule(nb));

	priority_queue<event> pq;

	for(int i=0;i<na;i++)
	{
		pq.push(event(0,-1,a[i].first));
		pq.push(event(1, 1,a[i].second+t));
	}
	for(int i=0;i<nb;i++)
	{
		pq.push(event(1,-1,b[i].first));
		pq.push(event(0, 1,b[i].second+t));
	}

	int ret[2];
	int at[2];
	at[0]=at[1]=ret[0]=ret[1]=0;

	while(!pq.empty())
	{
		int cur=pq.top().time;

		while(!pq.empty() && pq.top().time == cur)
		{
			at[pq.top().station] += pq.top().type;
			pq.pop();
		}

		for(int i=0;i<2;i++)
			if(at[i]<0)
			{
				ret[i]-=at[i];
				at[i]=0;
			}
	}

	return make_pair(ret[0],ret[1]);
}

int main(void)
{
	int n;

	cin >> n;

	for(int i=0;i<n;i++)
	{
		cout << "Case #" << i+1 << ": ";
		pair<int,int> temp=solve();
		cout << temp.first << " " << temp.second << endl;
	}

	return 0;
}
