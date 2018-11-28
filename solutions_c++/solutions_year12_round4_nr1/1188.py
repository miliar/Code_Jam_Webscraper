
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	int T;
	cin >>T;
	for (int z = 1; z <= T; ++z)
	{
		int N, D;
		cin>>N;
		vector<pair<int, int> > dl(N);
		for (int i = 0; i < N; ++i)
			cin>>dl[i].first>>dl[i].second;
		cin>>D;
		sort(dl.begin(), dl.end());
		dl.push_back(make_pair(D, 1));
		vector<int> maxStep(N+1, -1);
		maxStep[0] = dl[0].first;
		for (int i = 0; i < N; ++i)
		{
			if (maxStep[i] < 0)
				continue;
			int to = maxStep[i] + dl[i].first;
			for (int j = i+1; j <= N && dl[j].first <= to; ++j)
			{
				int step = min(dl[j].second, dl[j].first - dl[i].first);
				maxStep[j] = max(step, maxStep[j]);
			}
		}

		cout<<"Case #"<<z<<": ";
		if (maxStep[N] > 0)
			cout<<"YES\n";
		else
			cout<<"NO\n";
	}
	cin.get();
	cin.get();
	return 0;
}

