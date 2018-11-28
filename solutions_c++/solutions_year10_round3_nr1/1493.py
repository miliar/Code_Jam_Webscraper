#include <fstream>
#include <cmath>
#include <set>
#include <iostream>
using namespace std;

struct point{
	long double x;
	long double y;
	bool operator<(const point& rhs)const{
		if(abs(x - rhs.x)< 1e-7)
			return abs(y - rhs.y) < 1e-10;
		return abs(x - rhs.x) < 1e-10;
	}
};

long double	x1 = 0;
long double	x2 = 5000;
long double	x3 = 0;
long double	x4 = 5000;
point p;
void linecorss(const long double  &y1,const  long double &y2,const  long double &y3,const  long double &y4){
	long double k;
	k = ((x4 - x3) * (y1 - y3) - (y4 - y3) * (x1 - x3))/((y4 - y3) * (x2 - x1) - (x4 - x3) * (y2 - y1));
	p.x = x1 + k * (x2 - x1);
	p.y = y1 + k * (y2 - y1);
}
int main()
{
	ifstream ifs("in.txt");
	ofstream ofs("out.txt");
	int n,i,j;
	long double y1[100],y2[100],jx,jy;
	
	int t;
	ifs>>t;
	int cas = 1;
	
	while(cas <= t)	{
		set<point> s;
		ifs>>n;
		for(i=0;i<n;++i){
			ifs>>y1[i]>>y2[i];
		}
		for(i=0;i<n;++i){
			for(j=i+1;j<n;++j){
				if(y1[i] > y1[j] && y2[i] < y2[j] || y1[i] < y1[j] && y2[i] > y2[j]){
					linecorss(y1[i], y2[i], y1[j], y2[j]);
					s.insert(p);
					//cout<<p.x<<" "<<p.y<<endl;
				}

			}
		}
		ofs<<"Case #"<<cas++<<": "<<s.size()<<endl;
		
	}
	ofs.close();
	ifs.close();
	return 0;
} 