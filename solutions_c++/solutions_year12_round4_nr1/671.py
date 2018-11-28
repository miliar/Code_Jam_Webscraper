#include <iostream>
#include <string>
#include <vector>
#include <list>
#include <map>

using namespace std;

typedef vector<pair<int, int>> Vines;

bool execute(Vines& vines, int D, int cur, int vineLength)
{
	int vinePos = vines[cur].first;

	//cout << " - Holding onto vine " << (cur+1) << " rooted at " << vinePos << endl;

	if (vinePos + vineLength >= D) 
	{
		//cout << " * Swing to true love" << endl;
		return true;
	}

	for (int i = cur + 1; i < vines.size(); i++)
	{
		int dist = vines[i].first - vinePos;

		if (dist > vineLength) 
		{
			//cout << "Can't reach vine" << (i+1) << " from " << (cur+1) << endl;
			break;
		}

		int newLength = min(dist, vines[i].second);

		//cout << "Vine " << (i+1) << " - Freedom: " << newLength << endl;

		if (execute(vines, D, i, newLength)) 
		{
			//cout << " * Swing to vine " << (i+1) << endl;
			return true;
		}
	}

	return false;
}

int main()
{
	int T;
	cin >> T;

	for (int t = 1; t <= T; t++)
	{
		int N;
		cin >> N;

		vector<pair<int, int>> vines(N);

		for (int n = 0; n < N; n++)
		{
			int d, I;
			cin >> d >> I;
			vines[n] = make_pair(d, I);
		}

		int D;
		cin >> D;

		bool result = execute(vines, D, 0, vines[0].first);

		cout << "Case #" << t << ": " << (result ? "YES" : "NO") << endl;
	}
}
