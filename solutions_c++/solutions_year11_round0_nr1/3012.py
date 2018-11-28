#include <iostream>
#include <vector>
#include <string>
#include <map>

using namespace std;

typedef map< char, int > RobotPropertyMap;
typedef vector< pair< char , int > > RobotQueue;

const string botNames = "OB";

class RobotSolve {
	private:
		
		RobotQueue queue;
		int size;
		RobotPropertyMap distToObj;
		RobotPropertyMap objPos;
		int currObjIndex;
		int nbLeft;

	public:
		
		RobotSolve () : currObjIndex (0), nbLeft (botNames.length ())
		{
			cin >> size;
			queue.resize (size);

			for (int i = 0; i < size; ++i) {
				pair< char, int> &p = queue[i];
				cin >> p.first >> p.second;
			}

			for (int i = 0; i < botNames.length (); ++i) {
				char c = botNames[i];
				objPos[c] = 1;
				redefObj (c);
			}
		}

		int solve (void) {
			int time = 0;
			while (nbLeft > 0)
				time += next ();
			return time;
		}

	private:

		void redefObj (char c) {
			int i;
			
			for (i = currObjIndex; i < size && queue[i].first != c; ++i);
			
			if (i < size) {
				int newObjPos = queue[i].second;
				distToObj[c] = dist (objPos[c], newObjPos);
				objPos[c] = newObjPos;
			} else {
				distToObj[c] = -1;
				--nbLeft;
			}
		}

		int next (void) {
			char movingRobot = queue[currObjIndex].first;
			int timeNeeded = 1 + distToObj[movingRobot];
			
			for (RobotPropertyMap::iterator it = distToObj.begin (); it != distToObj.end (); ++it)
				if (it->first != movingRobot && it->second > 0) {
					int a = it->second - timeNeeded;
					it->second = a > 0 ? a : 0;
				}
			
			++currObjIndex;
			redefObj (movingRobot);

			return timeNeeded;
		}

		int dist (int a, int b) {
			int d = a - b;
			return d >= 0 ? d : -d;
		}
};

int main (void) {
	int n;

	cin >> n;
	for (int i = 0; i < n; ++i) {
		RobotSolve problem;
		cout << "Case #" << (i + 1) << ": " << problem.solve () << endl;
	}

	return 0;
}

