#include <iostream>
#include <algorithm>
#include <cmath>

#define MAXN 101

using namespace std;

int p[MAXN];
int b[MAXN];

int min(int a, int b)
{
	return (a < b ? a : b);
}

int main()
{
	int t, T, N, i, pos[2], time, j;
	char c;
	cin >> T;
	for (t = 0; t < T; ++t)
	{
		cin >> N;
		for (i = 0; i < N; ++i)
		{
			cin >> c >> p[i];
			b[i] = (c == 'O' ? 0 : 1);
		}
		pos[0] = pos[1] = 1;
		time = 0;
		for (i = 0; i < N; ++i)
		{
			int dt = abs(pos[b[i]]-p[i]) + 1;
			time += dt;
			pos[b[i]] = p[i];
			for (j = i+1; j < N; ++j)
				if (b[j] == 1-b[i])
					break;
			if (j == N)
				continue;
			if (p[j] > pos[1-b[i]])
				pos[1-b[i]] += min(dt, p[j]-pos[1-b[i]]); 
			else
				pos[1-b[i]] -= min(dt, pos[1-b[i]]-p[j]);			
		}
		cout << "Case #" << t+1 << ": " << time << endl;
	}
	return 0;
}