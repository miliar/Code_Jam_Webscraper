#include <iostream>
#include <map>
#include <queue>

using namespace std;

int go (int pos, queue<int> q)
{
	if (q.front() < pos)
		return pos - 1;
	if (q.front() > pos)
		return pos + 1;
	return pos;
}
int solve()
{
	int t;
	std::cin >> t;
	queue<int> oqueue;
	queue<int> bqueue;
	queue<pair<char, int> > obqueue;
	for (int i = 0; i < t; ++i)
	{
		char a;
		int p;
		std::cin >> std::ws >> a >> p;
		if (a == 'O')
		{
			oqueue.push(p);
		}
		else 
		{
			bqueue.push(p);
		}
		obqueue.push(make_pair(a, p));
	}
	int opos = 1, bpos = 1, time = 0; 
	while(! obqueue.empty())
	{
		++time;
		if (obqueue.front().first  == 'O' &&  obqueue.front().second == opos)
		{
			obqueue.pop();
			oqueue.pop();
			bpos = go(bpos, bqueue);
		}
		else if (obqueue.front().first  == 'B' &&  obqueue.front().second == bpos)
		{
			obqueue.pop();
			bqueue.pop();
			opos = go(opos, oqueue);
		}
		else
		{
			opos = go (opos, oqueue);
			bpos = go (bpos, bqueue);
		}
	}
	return time;
}

int main()
{
	int n;
	std::cin >> n;
	for (int i = 0; i < n; ++i)
	{
		int ans = solve();
		std::cout << "Case #" << i+1 << ": "<< ans << std::endl ;
	}
}
