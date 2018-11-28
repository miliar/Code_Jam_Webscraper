#include <iostream>
using namespace std;

pair<char,int> seq[128];
int N,T;

void solve(int test)
{
	cin>>N;

	for(int i=1;i<=N;i++)
	{
		cin>>seq[i].first>>seq[i].second;
	}

	int lastOpos = 1, lastBpos = 1;
	int lastOtime = 0, lastBtime = 0;

	int t = 0;
	for(int i=1;i<=N;i++)
	{
		if(seq[i].first == seq[i-1].first)
		{
			t += abs(seq[i].second - seq[i-1].second) + 1;
		}
		else
		{
			int lastpos = seq[i].first == 'O' ? lastOpos : lastBpos;
			int lasttime = seq[i].first == 'O' ? lastOtime : lastBtime;

			t = max( abs(seq[i].second - lastpos) + lasttime, t) + 1;
		}

		seq[i].first == 'O' ? lastOpos = seq[i].second : lastBpos = seq[i].second;
		seq[i].first == 'O' ? lastOtime = t : lastBtime = t;
	}

	printf("Case #%d: %d\n",test,t);
}

int main()
{
	cin>>T;

	for(int t=1;t<=T;t++)
	{
		solve(t);
	}
}