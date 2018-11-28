#include <iostream>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <cmath>
#include <iomanip>

#include <assert.h>

using namespace std;

struct Point
{
	double x, y;

	Point(double x, double y) : x(x), y(y) {}

	Point operator+ (const Point& o) const {return Point(x+o.x, y+o.y);}
	Point operator- (const Point& o) const {return Point(x-o.x, y-o.y);}

	double length() const {return sqrt(x*x + y*y);}
	double distance(Point& o) {return (*this - o).length();}
};

typedef pair<int, Point> Student;

double valid(vector<Student>& points, Student& check)
{
	for (int i = 0; i < points.size(); i++)
	{
		Student& p = points[i];

		double dist = p.second.distance(check.second);
		double threshold = p.first + check.first;

		if (dist < threshold) 
		{
			//cout << "Clash with (" << p.second.x << ", " << p.second.y << ") with reach " << p.first << endl;
			//cout << " trying (" << check.second.x << ", " << check.second.y << ") with reach " << check.first << endl;
			return threshold - dist;
		}
	}
	
	return -1.0;
}

int main()
{
	int T;
	cin >> T;

	for (int t = 1; t <= T; t++)
	{
		int N, W, L;
		cin >> N >> W >> L;

		vector<int> R(N);

		for (int i = 0; i < N; i++)
			cin >> R[i];

		vector<Student> placed;

		int k = 0;

		// Try quick case
		int nextW = 1;
		for (int w = 0; w <= W;)
		{
			int nextL = 1;			
			for (int l = 0; l <= L; )
			{
				Student s = make_pair(R[k], Point(w, l));

				double v = valid(placed, s);
				if (v < 0.0)
				{
					//cout << "Quick placed at (" << w << ", " << l << ") with reach " << R[k] << endl;
					placed.push_back(s);
					k++;
					if (k == N) break;

					int posW = R[k-1] + w;
					if (posW > nextW) nextW = posW;

					int posL = R[k-1] + R[k] + l;
					if (posL > nextL) nextL = posL;
				}
				else
					nextL += v;
				
				l = max(l + 1, nextL);
			}

			if (k == N) break;

			w = max(w + 1, nextW) + R[k];
			//cout << "Next W: " << w << endl;
		}

		if (placed.size() != N)
		{
			cout << "!!!!!!!!! Not everything was placed, only placed " << placed.size() << " of " << N << " students" << endl;
			break;
		}

		cout << "Case #" << t << ": ";

		for (Student& s : placed)
			cout << (int)s.second.x << " " << (int)s.second.y << " ";

		cout << endl;
	}
}
