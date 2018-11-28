#include <iostream>
#include <vector>
#include <set>
using namespace std;

struct point
{
	double x;
	double y;
};

bool GetIntersectPoint(const point& AP1, const point& AP2, const point& BP1, const point& BP2, point* IP) 
{ 
	double t; 
	double s;     
	double under = (BP2.y-BP1.y)*(AP2.x-AP1.x)-(BP2.x-BP1.x)*(AP2.y-AP1.y); 
	if(under==0) return false; 

	double _t = (BP2.x-BP1.x)*(AP1.y-BP1.y) - (BP2.y-BP1.y)*(AP1.x-BP1.x); 
	double _s = (AP2.x-AP1.x)*(AP1.y-BP1.y) - (AP2.y-AP1.y)*(AP1.x-BP1.x);     

	t = _t/under; 
	s = _s/under;     
	if(t<0.0 || t>1.0 || s<0.0 || s>1.0) return false; 
	if(_t==0 && _s==0) return false;     

	IP->x = AP1.x + t * (double)(AP2.x-AP1.x); 
	IP->y = AP1.y + t * (double)(AP2.y-AP1.y); 

	return true; 
} 

int main()
{

	int t_case;
	scanf("%d", &t_case);
	for(int t=1; t <= t_case; ++t)
	{
		int nPoints;
		int y1, y2;
		scanf("%d", &nPoints);

		vector<point> pointsA;
		vector<point> pointsB;

		for(int i=0; i < nPoints; ++i){
			scanf("%d %d", &y1, &y2);
			
			point p; 
			p.x = (double)0; p.y = (double)y1;
			pointsA.push_back(p);

			p.x = (double)1; p.y = (double)y2;
			pointsB.push_back(p);
		}

		set< pair<int, int> > intersect;
		point p;
		for(int i=0; i < nPoints; ++i){
			for(int j=i+1; j < nPoints; ++j){
				if( GetIntersectPoint(pointsA[i], pointsB[i], pointsA[j], pointsB[j], &p)==true ){
					intersect.insert( make_pair((int)p.x, (int)p.y) );
				}
			}
		}

		printf("Case #%d: %d\n", t, intersect.size());
	}

	return 0;
}