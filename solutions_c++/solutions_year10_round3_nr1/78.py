#include <iostream>
#include <map>
#include <set>
#include <vector>

using namespace std;

int main(int argc, char *argv[])
{
	int cases, wires;
	cin >> cases;
	for(int ci = 0; ci < cases; ++ci)
	{
		cin >> wires;
		set<int> end_points;
		map<int, set<int>::iterator> start_points;
		for(int wi = 0; wi < wires; ++wi)
		{
			int start, end;
			cin >> start >> end;
			start_points[start] = end_points.insert(end).first;
		}

		int intersections = 0;
		while(start_points.size())
		{
			map<int, set<int>::iterator>::iterator si = start_points.begin();
			for(set<int>::iterator ei = si->second, eend = end_points.begin(); ei != eend; --ei)
				++intersections;
			end_points.erase(si->second);
			start_points.erase(si);
		}
		cout << "Case #" << (ci + 1) << ": " << intersections << endl;
	}

	return 0;
}
