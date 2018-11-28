#include<iostream>
#include<queue>

using namespace std;

struct node { int ans, c; bool done; };

int main()
{
	int t; cin >> t;
	int i, j, m;
	for(i = 1; i <= t; i++)
	{
		queue<node> q;
		int R, k, N; cin >> R >> k >> N;
		int g;
		for(j = 0; j < N; j++)
			{ cin >> g; node n; n.ans = g; n.done = false; q.push(n); }
		long long tot = 0;
		int tans[2000], c = 0; 
		while(!q.front().done)
		{
			q.front().c = c;
			q.front().done = true;
			if(q.front().done == false) cout << "Problem";
			int temp = 0;
			queue<node> temp_q;
			while(!q.empty())
			{
				node f = q.front();
				if(temp + f.ans > k) break;
				temp += f.ans;
				q.pop();
				temp_q.push(f);
			}
			tot += temp;
			while(!temp_q.empty())
			{
				q.push(temp_q.front());
				temp_q.pop();
			}
			
			tans[c++] = temp;
		}
		int cycle_length = c - q.front().c;
		if(R < q.front().c)
		{
			tot = 0;
			for(j = 0; j < R; j++) tot += tans[j];
		}
		else
		{
			tot = 0;
			for(j = 0; j < q.front().c; j++) tot += tans[j];
			R -= q.front().c;
			
			long long cycle_cost = 0;
			for(j = q.front().c; j < c; j++)
				cycle_cost += tans[j];
			long long cycles = R / cycle_length;
			tot += cycles * cycle_cost;
			R %= cycle_length;
			for(j = q.front().c; j < q.front().c + R; j++)
				tot += tans[j];
		}
		cout << "Case #" << i << ": " << tot << endl;
	}
	return 0;
}
