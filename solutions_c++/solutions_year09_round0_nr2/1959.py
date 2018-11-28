#include <iostream>
#include <sstream>
#include <vector>
#include <map>
using namespace std;

int h, w;

map<string, string> basin_area;

map<string, char> area;
char area_mark;

string getBasinArea(string s)
{
    map<string, string>::iterator it = basin_area.find(s);
    if(it->second == s)
	return s;
    return getBasinArea(it->second);
}

string fill(string s)
{
    int j(3 - s.size());
    for(int i = 0; i < j; ++i)
	s = '0' + s;
    return s;
}

string getStr(int x, int y)
{
    string sx, sy, s;
    stringstream ss(stringstream::in | stringstream::out);
    ss<<x<<" "<<y;
    ss>>sx>>sy;
    s = fill(sx) + fill(sy);
    return s;
}

class Point
{
    public:
	Point(int xx, int yy, int alt) : x(xx), y(yy), altitude(alt) { 
	    pstr = getStr(xx, yy); basin_area[pstr] = pstr;
	}
	void updateBasin();
	void updateTop(Point *p1, Point *p2);
	string getPStr() { return pstr; }
    private:
	int x, y;
	int altitude;
	string pstr;
};

vector< vector<Point> > pts;

void Point::updateTop(Point *p1, Point *p2)
{
    string bp1 = getBasinArea(p1->pstr);
    string bp2 = getBasinArea(p2->pstr);
    if(bp1 < bp2) {
	basin_area[p2->pstr] = bp1;
	basin_area[bp2] = bp1;
    }
    else {
	basin_area[p1->pstr] = bp2;
	basin_area[bp1] = bp2;
    }

}

void Point::updateBasin() {
    int min_dir(0), min_altitude(altitude);
    if((x+1) < h) { // south
	if(pts[x+1][y].altitude <= min_altitude) {
	    min_dir = 0;
	    min_altitude = pts[x+1][y].altitude;
	}
    }
    if((y+1) < w) { // east
	if(pts[x][y+1].altitude <= min_altitude) {
	    min_dir = 1;
	    min_altitude = pts[x][y+1].altitude;
	}
    }
    if((y-1) >= 0) {	//west
	if(pts[x][y-1].altitude <= min_altitude) {
	    min_dir = 2;
	    min_altitude = pts[x][y-1].altitude;
	}
    }
    if((x-1) >= 0) {  //north
	if(pts[x-1][y].altitude <= min_altitude) {
	    min_dir = 3;
	    min_altitude = pts[x-1][y].altitude;
	}
    }

    if(min_altitude < altitude)	{    //  flow out 
	string smb;
	switch(min_dir) {
	    case 0: updateTop(&pts[x+1][y], this); break;
	    case 1: updateTop(&pts[x][y+1], this); break;
	    case 2: updateTop(&pts[x][y-1], this); break;
	    case 3: updateTop(&pts[x-1][y], this); break;
	}
    }
}
void test()
{
    int i, j;

    for(i = 0;i < h; ++i) {
	for(j = 0; j < w; ++j) {
	    pts[i][j].updateBasin();
	}
    }
    string pstr, ba;
    map<string, char>::iterator iter;
    for(i = 0;i < h; ++i) {
	for(j = 0; j < w; ++j) {
	    pstr = pts[i][j].getPStr();
	    ba = getBasinArea(pstr);
	    iter = area.find(ba);
	    if(iter == area.end()) {
		area.insert(make_pair(ba, area_mark));
		cout<<area_mark<<((j<w-1)?" ":"");
		area_mark += 1;
	    } else
		cout<<(iter->second)<<((j<w-1)?" ":"");
	}
	cout<<endl;
    }
}

int main()
{
    int t;
    cin>>t;
    int i, j, n(0), alt;
    while(t--) {
	cin>>h>>w;
	pts.clear();
	basin_area.clear();
	area.clear();
	area_mark = 'a';
	for(i = 0;i < h; ++i) {
	    vector<Point> vp;
	    for(j = 0; j < w; ++j) {
		cin>>alt;
		vp.push_back(Point(i, j, alt));
	    }
	    pts.push_back(vp);
	}
	cout<<"Case #"<<++n<<":"<<endl;
	test();
    }
    return 0;
}
