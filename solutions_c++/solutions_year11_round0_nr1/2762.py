#include <iostream>
#include <list>

using namespace std;

int distance(int a, int b)
{
	return abs(a - b);
}

int main()
{
	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t)
	{
		int N;
		cin >> N;

		list<int> pushqueue;
		list<int> destinations[2];

		while (N--)
		{
			char who;
			int dst;
			cin >> who >> dst;
			int index = (who == 'B') ? 0 : 1;
			pushqueue.push_back(index);
			destinations[index].push_back(dst);
		}

		int time = 0;
		int time_shared[2] = {0};
		int locations[2] = {1, 1};
		for (auto i = pushqueue.begin(); i != pushqueue.end(); ++i)
		{
			int dst = destinations[*i].front();
			destinations[*i].pop_front();

			int dist = distance(locations[*i], dst);
			int used = (dist < time_shared[*i]) ? 0 : dist - time_shared[*i];
			used++;
			time_shared[*i] = 0;
			time_shared[(*i + 1) % 2] += used;
			time += used;

			locations[*i] = dst;
		}

		cout << "Case #" << t << ": " << time << endl;
	}

	return 0;
}
