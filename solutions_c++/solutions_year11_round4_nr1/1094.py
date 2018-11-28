#include <fstream>
#include <vector>
#include <algorithm>
#include <utility>
#include <iomanip>
using namespace std;

/*
Input

The first line of the input gives the number of test cases, T. T test cases follow. 
Each test case begins with a line containing five integers: 
X (the length of the corridor, in meters), S (your walking speed, in meters per second), 
R (your running speed, in meters per second), t (the maximum time you can run, in seconds) 
and N (the number of walkways).
Each of the next N lines contains three integers:
Bi, Ei and wi - the beginning and end of the walkway (in meters from your starting point) 
and the speed of the walkway (in meters per second).
*/

int main() {

	ifstream in("A-large.in");
	ofstream out("out.txt");

	const double eps = 1E-20;

	int tt, x, n;
	double s, r, t;
	in >> tt;
	for (int tc = 1; tc <= tt; ++tc) {
		in >> x >> s >> r >> t >> n;
		vector<pair <pair<int, int>, int> > v(n);
		for (int i = 0; i < n; ++i) 
			in >> v[i].first.first >> v[i].first.second >> v[i].second;
		
		v.push_back(pair<pair<int, int>, int>(pair<int, int>(x, x), 0));
		v.push_back(pair<pair<int, int>, int>(pair<int, int>(0, 0), 0));

		sort(v.begin(), v.end());

		vector<pair<int, int> > sl;
		for (int k = 1; k < v.size(); ++k)
		{
			int posS = v[k].first.first;
			int posE = v[k].first.second;
			double wS = v[k].second;

			int posPrev = v[k - 1].first.second;


			int dist = (posS - posPrev);
			int sR = r, sS = s;

			sl.push_back(pair<int, int>(sS, dist));

			dist = (posE - posS);

			sS = s + wS;
			sl.push_back(pair<int, int>(sS, dist));
		}

		sort(sl.begin(), sl.end());


		vector<double> tim(sl.size(), 1E50);
		tim[0] = 0;

		for (int k = 1; k < sl.size(); ++k)
		{
			double curTime = tim[k - 1];
			double dist = sl[k].second;
			double sR = sl[k].first+ r - s , sS = sl[k].first;

			if (t >= eps) {
				double durR = dist / sR;
				if (durR <= t)
				{
					curTime += dist / sR;
					t -= durR;
				}
				else {
					curTime += (t + (dist - t*sR) / sS);
					t = 0;
				}
			}
			else {
				curTime += dist / sS;
			}
			tim[k] = curTime;

		}
		out << setprecision(11) << setiosflags(ios::showpoint);
		out << "Case #" << tc <<": " << tim[sl.size() - 1] <<  endl;
	}
	return 0;
}