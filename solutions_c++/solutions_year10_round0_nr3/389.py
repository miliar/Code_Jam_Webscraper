#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

ifstream fin("C-large.in");
ofstream fout("C-large.out");

#define cin fin
#define cout fout

long long ans;
long long R, K;
long long data[1024];
int n;

vector <long long> bonus;
vector <int> pos;

void work()
{
	int cur, next_cur, left;
	int times;
	int m;

	long long now, gain, cycle;

	pos.clear();
	bonus.clear();

	ans = 0;
	cur = 0;
	times = 0;

	while (times < R)
	{
		for (int i = 0; i < pos.size(); i++)
			if (pos[i] == cur)
			{
				cycle = 0;
				for (int j = i; j < pos.size(); j++)
					cycle += bonus[j];

				ans += ((R - times) / (pos.size() - i)) * cycle;
				
				left = (R - times) % (pos.size() - i);
				for (int j = i; j < i + left; j++)
					ans += bonus[j];

				return;
			}

		next_cur = cur;
		now = data[next_cur];
		m = 0;

		while (now <= K && m < n)
		{
			next_cur = (next_cur + 1) % n;
			now += data[next_cur];
			m++;
		}

		gain = now - data[next_cur];

		pos.push_back(cur);
		bonus.push_back(gain);

		cur = next_cur;

		times++;
		ans += gain;
	}
}

int main()
{
	int t;

	cin >> t;
	for (int i = 0; i < t; i++)
	{
		cin >> R >> K >> n;
		for (int j = 0; j < n; j++)
			cin >> data[j];

		work();

		cout << "Case #" << i+1 << ": " << ans << endl;
	}

	return 0;
}