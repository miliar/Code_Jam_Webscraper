#include <cstdio>
#include <cstdlib>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <string>
#include <iostream>
#include <sstream>
#include <fstream>
#include <cmath>


using namespace std;

char moves[101];
deque<int> o,b;
int time;
int m;

template<class T>
inline T max(T& a,T& b)
{
	return a>b ? a :b;
}

inline int sign(int a)
{
	return a>0 ? 1 : (a<0 ? -1 : 0);
}
void solve();

void readdata()
{
	int n;
	cin >> n;
	for(int i=0;i<n;++i)
	{
		if (i)
			cout.put('\n');
		o.clear();
		b.clear();
		cin >> m;
		for(int j=0;j<m;++j)
		{
			int k;
			cin >> moves[j] >> k;
			if (moves[j] == 'O')
				o.push_back(k);
			else
				b.push_back(k);
		}
		moves[m] = '\0';
		solve();
		printf("Case #%d: %d",i+1,time);
	}
}

void solve()
{
	int i=0;
	int timeb,timeo;
	timeb = timeo = 0;
	time = 0;
	int cb,co;
	cb = co = 1;
	while(i<m)
	{
		if(moves[i] == 'O')
		{
			timeb = timeo = 0;
			if (!b.empty() && cb != b.front())
			{
				timeb = abs(b.front() - cb);
			}
			while(moves[i] == 'O')
			{
				timeo += abs(o.front() - co) +1;
				co = o.front();
				o.pop_front();
				++i;
			}
			if (timeb != 0)
			{
				int dif = b.front() - cb;
				int s = sign(dif);
				int d = min(abs(dif),timeo);
				cb += s*d;
			}
			time += timeo;
		}
		else if(moves[i] == 'B')
		{
			timeb = timeo = 0;
			if (!o.empty() && co != o.front())
			{
				timeo = abs(o.front() - co);
			}
			while(moves[i] == 'B')
			{
				timeb += abs(b.front() - cb) +1;
				cb = b.front();
				b.pop_front();
				++i;
			}
			if (timeo != 0)
			{
				int dif = o.front() - co;
				int s = sign(dif);
				int d = min(abs(dif),timeb);
				co += s*d;
			}
			time += timeb;
		}
	}
}

int main()
{
#ifdef ANYKEY
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
#endif
	readdata();
	return (EXIT_SUCCESS);
}