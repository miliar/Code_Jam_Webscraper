#include <iostream>
#include <queue>
using namespace std;

int main()
{
	int N;
	cin >> N;
	for (int i=1; i<=N; i++)
	{
		queue<int> bj, oj;
		queue<char> j;
		char c;
		int n, p;
		cin >> n;
		while (n--)
		{
			cin >> c >> p;
			if (c == 'O') oj.push(p);
			else bj.push(p);
			j.push(c);
		}

		int bp=1, op=1;
		int c_bj=1, c_oj=1;
		bool bf=false, of=false;
		if (!bj.empty())
		{
			c_bj = bj.front(); bj.pop();
		}
		else
		{
			bf = true;
		}
		if (!oj.empty())
		{
			c_oj = oj.front(); oj.pop();
		}
		else
		{
			of = true;
		}
		int turn = 0;

		while (!j.empty())
		{
			int bd, od;
			bd = (c_bj-bp>0) ? c_bj-bp : bp-c_bj;
			od = (c_oj-op>0) ? c_oj-op : op-c_oj;
			char nj = j.front(); j.pop();
			int cost;
			if (nj == 'O')
			{
				cost = od + 1;
				op = c_oj;
				if (!of)
				{
					if (!oj.empty())
					{
						c_oj = oj.front(); oj.pop();
					}
					else
					{
						of = true;
					}
				}

				if (!bf)
				{
					if (cost >= bd)
					{
						bp = c_bj;
					}
					else
					{
						bp = (bp < c_bj) ? bp+cost : bp-cost;
					}
				}
			}
			else
			{
				cost = bd + 1;
				bp = c_bj;
				if (!bf)
				{
					if (!bj.empty())
					{
						c_bj = bj.front(); bj.pop();
					}
					else
					{
						bf = true;
					}
				}

				if (!of)
				{
					if (cost >= od)
					{
						op = c_oj;
					}
					else
					{
						op = (op < c_oj) ? op+cost : op-cost;
					}
				}
			}
			turn += cost;
		}

		cout << "Case #" << i << ": " << turn << endl;
	}

	return 0;
}