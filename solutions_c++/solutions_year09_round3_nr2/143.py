#include <algorithm>
#include <fstream>
#include <string>
#include <queue>
#include <set>
#include <stack>
#include <map>
#include <sstream>
#include <iostream>
#include <cmath>
using namespace std;

typedef unsigned int uint;
typedef long long int64;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> pI;
typedef pair<string,int> pSI;
typedef pair<int,string> pIS;

#define FOR(i,n) for(int i=0, upTo##i=n; i<upTo##i; ++i)
#define REVFOR(i,n) for(int i=(n)-1; i>=0; --i)
#define FOR2(i,b,n) for(int i=b; i<(n); ++i)
#define REVFOR2(i,b,n) for(int i=(n)-1; i>=b; --i)
#define SC(i) scanf("%d", i)
#define ALL(C) (C).begin(), (C).end()
#define RALL(C) (C).rbegin(), (C).rend()
#define MIN(C) *min_element(ALL(C))
#define MAX(C) *max_element(ALL(C))
#define A first
#define B second

struct Point3d {
	double _x,_y,_z;

	Point3d(double x, double y, double z): _x(x), _y(y), _z(z) {  }

	double Distance(const Point3d &p){
		double distX= _x-p._x;
		double distY= _y-p._y;
		double distZ= _z-p._z;
		return sqrt(distX*distX + distY*distY + distZ*distZ);
	}

	Point3d getMiddle(const Point3d &p1, const Point3d &p2) {
		return Point3d((p1._x + p2._x) / 2, (p1._y + p2._y) / 2, (p1._z + p2._z) / 2);
	}

	double get(int idx) {
		if (idx==0) return _x;
		else if (idx==1) return _y;
		else return _z;
	}

	void set(int idx, double val) {
		if (idx==0) _x = val;
		else if (idx==1) _y = val;
		else _z = val;
	}
};

vector<Point3d> initPos;
vector<Point3d> velocity;

Point3d centerOfMass(double time) {
	Point3d res(0,0,0);
	FOR(j,3) {
		double curr = 0;
		FOR(i,initPos.size()) {
			curr += initPos[i].get(j) + (velocity[i].get(j) * time);
		}
		curr /= initPos.size();
		res.set(j, curr);
	}
	return res;
}

Point3d start(0,0,0);

bool isEqual(double d1, double d2) {
	return fabs(d1-d2)<1e-9;
}

double dist(double time)
{
	Point3d cen = centerOfMass(time);
	return cen.Distance(start);
}

int main(void) {
    int n; cin>>n;
    FOR(_i,n) {
		int t;
		cin>>t;
		initPos.clear();
		velocity.clear();
		FOR(i,t) 
		{
			int x,y,z,vx,vy,vz;
			cin>>x>>y>>z>>vx>>vy>>vz;
			initPos.push_back(Point3d(x,y,z));
			velocity.push_back(Point3d(vx,vy,vz));
		}

        double res=0;
		double time=0;

		if (isEqual(dist(0), dist(1)) && isEqual(dist(1), dist(2)))
		{
			res = dist(0);
			time = 0;
		} 
		else 
		{
			if (dist(0) < dist(0.0000001)) {
				res = dist(0);
				time = 0;
			}
			else
			{
				double t1 = 0;
				double t2 = 1e10;
				double t3 = (t2-t1) / 2 + t1;
				
				while(true) {
					double d1 = dist( (t2-t1) / 2 + t1 );
					double d2 = dist( (t3-t2) / 2 + t2 );

					if (isEqual(t1,t2) && isEqual(t2,t3) && isEqual(d1,d2))
					{
						res = d1;
						time = t1;
						break;
					}

					if (d1 < d2)
					{
						t3 = (t3-t2) / 2 + t2;
						t2 = (t3-t1) / 2 + t1;
					}
					else
					{
						t1 = (t2-t1) / 2 + t1;
						t2 = (t3-t1) / 2 + t1;
					}
				}
			}
		}

        printf("Case #%d: %.8lf %.8lf\n", _i+1, res, time);
    }
    return 0;
}
