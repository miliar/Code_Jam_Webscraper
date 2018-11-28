#include <iostream>
#include <fstream>
#include <cmath>
#include <vector>
#include <algorithm>
#include <iomanip>
#include <cstdio>
#include <map>
#include <set>
#include <sstream>
#include <strstream>
#include <queue>
#include <stack>
#include <set>

using namespace std;

ifstream in("large.in");
ofstream out("large.out");

long long g[1100],R,n,k;
long long qanak[1100];
long long ham[1100];
long long gumar[1100];

long long solve()
{
	long long i;
	
	long long ans = 0,hamar;
	
	for (i = 0 ; i < n; i++)
	{
		qanak[i] = -1;
		ham[i] = -1;
		gumar[i] = 0;
	}

	deque <pair<long long,int>> d;
	
	for (i = 0 ; i < n ; i++)
		d.push_back(make_pair(g[i],i));

	queue <pair<long long,int>> q;

	long long answer = 0;

	long long t = 0;

	/*for (deque <pair<long long,int>>::iterator it = d.begin(); it != d.end(); ++it)
			cout << (*it).first << " ";
		cout << endl;*/

		/*d.pop_front();

		cout << d.front().first << endl;*/
	
	while (R > 0 && qanak[d.front().second] == -1)
	{
		t++;
		R--;
		ans = 0;
		
		while (!q.empty()) q.pop();
		
		hamar = d.front().second;

		gumar[hamar] = answer;
		
		while (!d.empty() && ans + d.front().first <= k)
		{
			q.push(d.front());
			ans += d.front().first;
			d.pop_front();
		}	
		
		qanak[hamar] = ans;

		ham[hamar] = t;
		
		while (!q.empty())
		{
			d.push_back(q.front());
			q.pop();
		}

		answer += qanak[hamar];

	}

	hamar = d.front().second;

	long long u = t - ham[hamar] + 1;

	answer += (R/u)*(answer - gumar[hamar]);

	R %= u;

	while (R > 0)
	{
		t++;
		R--;
		ans = 0;
		
		while (!q.empty()) q.pop();
		
		hamar = d.front().second;

		gumar[hamar] = answer;
		
		while (!d.empty() && ans + d.front().first <= k)
		{
			q.push(d.front());
			ans += d.front().first;
			d.pop_front();
		}	
		
		qanak[hamar] = ans;

		ham[hamar] = t;
		
		while (!q.empty())
		{
			d.push_back(q.front());
			q.pop();
		}

		answer += qanak[hamar];

	}

	return answer;
}

int main()
{
	int test;
	int i;
	in >> test;
	for (int t = 1; t <= test; t++)
	{
		in >> R >> k >> n;
		for (i = 0 ; i < n ; i++)
			in >> g[i];
		long long answer = solve();
		out << "Case #" << t << ": " << answer << endl;
	}
	return 0;
}