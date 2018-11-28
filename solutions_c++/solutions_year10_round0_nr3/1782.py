#include <map>
#include <deque>
#include <vector>
#include <fstream>
#include <iostream>
using namespace std;
typedef long long ll;

ll Simulate(deque<ll> & q, ll k)
{
	ll rest = k;
	deque<ll> qNext;
	ll nowYield = 0;
	while(q.size())
	{
		if(q[0] > rest)
			break;
		nowYield += q[0];
		rest -= q[0];
		qNext.push_back(q[0]);
		q.pop_front();
	}
	while(qNext.size())
	{
		q.push_back(qNext.front());
		qNext.pop_front();
	}
	return nowYield;
}

int main()
{
	ifstream in("in.txt");
	ll tests;
	in >> tests;
	ll r, k, n;
	deque<ll> g;
	map<deque<ll>, ll> yield;
	map<deque<ll>, ll> history;
	vector<ll> plain;
	for(ll test = 1; test <= tests; test++)
	{
		in >> r >> k >> n;		
		g.resize((int)n);
		for(ll i = 0; i < n; i++)
			in >> g[(int)i];
		plain.clear();
		yield.clear();
		history.clear();		
		ll nowYield = 0;
		deque<ll> q(g.begin(), g.end());
		yield[q] = 0;
		history[q] = 0;		
		plain.push_back(0);
		ll ans = 0;
		for(ll turn = 1; ; turn++)
		{			
			if(turn - 1 == r)
			{
				ans = nowYield;
				break;
			}
			nowYield += Simulate(q, k);
			if(yield.find(q) != yield.end())
			{		

				ans = yield[q];
				ll yieldPeriod = nowYield - yield[q];
				ll prevTurn = history[q];
				ll turnPeriod = turn - prevTurn;
				ll rest = r - history[q];
				if(q == g)
				{
					ans = nowYield * (r / turn) + plain[(int)(r % turn)];
				}
				else
				{
					ans += (rest / turnPeriod) * yieldPeriod;				
					ll mod = rest % turnPeriod;
					while(mod--)
						ans += Simulate(q, k);
				}				
				break;
			}
			yield[q] = nowYield;
			history[q] = turn;
			plain.push_back(nowYield);
		}
		cout << "Case #" << test << ": " << ans << endl;
	}
	return 0;
}