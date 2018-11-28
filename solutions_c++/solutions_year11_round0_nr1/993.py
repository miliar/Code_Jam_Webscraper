#include <iostream>
#include <vector>
#include <list>
#include <cstdlib>
using namespace std;
int sign(int x)
{
	return (x < 0) ? -1 : (x > 0) ? 1 : 0;
}

int solve()
{
	int n;
	cin >> n;
	vector<int> G[2];
	vector<char> turn;
	char c;
	int v;
	
	for (int i = 0; i < n; i++)
	{
		cin >> c >> v;
		G[c == 'O'].push_back(v);
		turn.push_back(c == 'O');
	}
	G[0].push_back(1000000);
	G[1].push_back(1000000);
	int pos[2] = {1, 1};
	int pt[2] = {0, 0};
	int tpt = 0;
	bool press[2];
	for (int t = 0; ; t++)
	{
		if (tpt == n)
			return t;
		for (int i = 0; i < 2; i++)
			press[i] = (pos[i] == G[i][pt[i]] && turn[tpt] == i);
		for (int i = 0; i < 2; i++)
			if (press[i])
				tpt++, pt[i]++;
			else
				pos[i] += sign(G[i][pt[i]] - pos[i]);
	}
}

int main()
{
	int T;
	cin >> T;
	int A;
	for (int i = 1; i <= T; i++)
		A = solve(),
		cout << "Case #" << i << ": " << A << endl,
		cerr << "Case #" << i << ": " << A << endl;
}
