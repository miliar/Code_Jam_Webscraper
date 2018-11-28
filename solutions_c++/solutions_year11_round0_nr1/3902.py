#include <iostream>
#include <string>
#include <stdlib.h>
#include <stdio.h>
#include <vector>
#include <queue>

using namespace std;

int absol(int a)
{
	return (a>0)? a: -a;
}

int minim(int a, int b)
{
	return (a < b)? a: b;
}


int main()
{
	int T;
	cin >> T;
	for(int iter = 0; iter < T; iter++)
	{
		int N;
		vector<char> robots;
		queue<int> q[2];

		cin >> N;
		for(int oper = 0; oper < N; oper++)
		{
			char r;
			int p;
			cin >> r >> p;

			if(r == 'O')
			{
				q[0].push(robots.size());
				robots.push_back(p);
			}else{
				q[1].push(robots.size());
				robots.push_back(p);
			}
		}
		int t = 0;
		int p[] = {1, 1};
		for(int i = 0; i < N; i++)
		{
			int r;
			//get robot
			while(1)
			{
				if(q[0].empty())
				{
					r = 1;
					break;
				}
				if(q[1].empty())
				{
					r = 0;
					break;
				}
				r = q[0].front() < q[1].front()? 0: 1;
				break;
			}

			int process_time = absol(p[r] - robots[q[r].front()]) + 1;
			p[r] = robots[q[r].front()];

			if(!q[1-r].empty())
			{
				int dir = (p[1-r] > robots[q[1-r].front()])? +1: -1;
				int walk = minim(absol(p[1-r] - robots[q[1-r].front()]), process_time);
				p[1-r] -= dir*walk;
			}
			t += process_time;
			q[r].pop();
		}
		fprintf(stdout, "Case #%d: %d\n", iter+1, t);
	}
	return 0;
}

