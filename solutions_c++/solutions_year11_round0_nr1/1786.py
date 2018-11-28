#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <queue>
#include <stdexcept>
using namespace std;
#define sz(a) int(a.size())

struct Task 
{
	int k;
	char b;
	Task(int K, char B) {k = K; b = B;}
	Task(){}
};

void go(int &p, queue<Task> &q)
{
	if (q.empty())
		return;
	if (p > q.front().k)
		--p;
	else if (p < q.front().k)
		++p;
}

int solve(queue<Task> &s, queue<Task> &Bs, queue<Task> &Os)
{
	int t = 0, o = 1, b = 1;
	while (!s.empty()) 
	{
		if (s.front().b == 'O')
		{
			go(b, Bs);
			if (o == s.front().k)
				s.pop(), Os.pop();
			else
				go(o, s);
		}
		else 
		{
			go(o, Os);
			if (b == s.front().k)
				s.pop(), Bs.pop();
			else
				go(b, s);
		}
		++t;
	}
	return t;
}

int main()
{
	int tests;
	cin >> tests;
	for (int t_num = 1; t_num <= tests; ++t_num)
	{
		int n;
		cin >> n;
		queue<Task> s, Os, Bs;
		for (int i = 0; i < n; ++i)
		{
			int k;
			char b;
			cin >> b >> k;
			if (b == 'O')
				Os.push(Task(k, 'O'));
			else
				Bs.push(Task(k, 'B'));
			s.push(Task(k, b));
		}
		cout << "Case #" << t_num << ": " << solve(s, Bs, Os) << endl;
	}
	return 0;
}	
