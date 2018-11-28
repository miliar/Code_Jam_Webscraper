#include <iostream>
#include <cstdlib>
#include <queue>

using namespace std;
int T;


void work(int cur)
{
	int pO = 1,pB = 1;
	queue<int> qO,qB,qT,qR;
	char ch;
	int n;
	cin >> n;
	int step = 0;
	for (int i=1;i<=n;i++)
	{
		cin >> ch;
		while (ch != 'O' && ch != 'B') cin >> ch;
		int num;
		cin >> num;
		if (ch == 'O')
			qO.push(num);
		else if (ch == 'B')
			qB.push(num);
		qR.push(ch);
		qT.push(ch);
	}
	while (!(qB.empty() && qO.empty()))
	{
		bool pushed = false;
		if (qR.front() == 'O' && pO == qO.front())
		{
			qR.pop();qO.pop();
			pushed = true;
		}
		else
		{
			if (pO != qO.front())
			{
				int t = qO.front() - pO;
				pO += t/abs(t);
			}
		}
		if (qR.front() == 'B' && pB == qB.front() && (!pushed))
		{
			qR.pop();qB.pop();
			pushed=true;
		}
		else
		{
			if (pB != qB.front())
			{
				int t = qB.front() - pB;
				pB += t/abs(t);
			}
		}
		step++;

	}
	cout << "Case #" << cur << ": " << step << endl;
}

int main()
{
	cin >> T;
	for (int i=1;i<=T;i++)
		work(i);
}

