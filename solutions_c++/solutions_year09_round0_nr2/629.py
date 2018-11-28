#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <queue>

using namespace std;

enum{SINK=1,N,W,E,S};

char *direction(int d){
	switch(d){
		case SINK:return "s";
		case N:return "^";
		case W:return "<";
		case E:return ">";
		case S:return "v";
	}
	return "?";
}

struct basin{
	int sink_x,sink_y;
	char name;
};

struct cell{
	int altitude;
	int to;
	int basinID;
};

struct mapT{
	int h,w;
	vector<cell> cells;
	vector<basin> basin_list;

	mapT(int h,int w):h(h),w(w),cells((h+2)*(w+2)),basin_list(){
		cell wall={9999999,SINK,-1};
		for(int i = -1; i <= w; ++i){
			at(i,-1) = wall;
			at(i,h) = wall;
		}
		for(int i = 0; i <= h-1; ++i){
			at(-1,i) = wall;
			at(w,i) = wall;
		}
		basin_list.reserve(26);
	}
	cell &at(int x, int y){return cells[x+1+(y+1)*(w+2)];}
	cell &north(int x, int y){return at(x,y-1);}
	cell &west (int x, int y){return at(x-1,y);}
	cell &east (int x, int y){return at(x+1,y);}
	cell &south(int x, int y){return at(x,y+1);}
	void print(ostream &o);

	void scan_to();

	void scan_basin(basin &b);
	void scan_basin_impl(int x,int y);

	int solve();

};

int T;
vector<mapT> tests;

int input_read(char * filename)
{
	ifstream ifs;
	ifs.open(filename, ios::in);
    
    ifs >> T;

	for(int i=0; i<T; ++i){
		int h=1,w=1;
		ifs >> h >> w;
		mapT testmap(h,w);
		for(int y=0; y<h; ++y){
			for(int x=0; x<w; ++x){
				ifs >> testmap.at(x,y).altitude;
			}
		}
		tests.push_back(testmap);
	}

	return 0;
}

void mapT::scan_to(){
	for(int y=0; y<h; ++y){
		for(int x=0; x<w; ++x){
			cell &here = at(x,y);
			here.to = SINK;
			int min = here.altitude;
			if(north(x,y).altitude < min){
				here.to=N; min=north(x,y).altitude;
			}
			if(west(x,y).altitude < min){
				here.to=W; min=west(x,y).altitude;
			}
			if(east(x,y).altitude < min){
				here.to=E; min=east(x,y).altitude;
			}
			if(south(x,y).altitude < min){
				here.to=S;
			}
			if(here.to==SINK){
				basin b = {x,y,'?'};
				basin_list.push_back(b);
				here.basinID = basin_list.size();
			}
		}
	}
}

void mapT::scan_basin_impl(int x,int y){
	int bID = at(x,y).basinID;
	if(north(x,y).basinID == 0 && north(x,y).to == S){
		north(x,y).basinID = bID;
		scan_basin_impl(x,y-1);
	}
	if(west(x,y).basinID == 0 && west(x,y).to == E){
		west(x,y).basinID = bID;
		scan_basin_impl(x-1,y);
	}
	if(east(x,y).basinID == 0 && east(x,y).to == W){
		east(x,y).basinID = bID;
		scan_basin_impl(x+1,y);
	}
	if(south(x,y).basinID == 0 && south(x,y).to == N){
		south(x,y).basinID = bID;
		scan_basin_impl(x,y+1);
	}
}

/*
struct point{
	int x,y;
	point(int x, int y):x(x),y(y){}
};
void mapT::scan_basin_impl(int x,int y){
	cell &sink = at(x,y);
	queue<point> qu;
	qu.push(point(x,y-1));
	qu.push(point(x-1,y));
	qu.push(point(x+1,y));
	qu.push(point(x,y+1));

	while(!qu.empty()){
		point p = qu.front();
		if(at(p.x,p.y).basinID != 0){
			qu.pop();
			continue;
		}
		at(p.x,p.y).basinID = sink.basinID;
		if(north(p.x,p.y).basinID == 0 && north(p.x,p.y).to == S){
			qu.push(point(p.x,p.y-1));
		}
		if(west(p.x,p.y).basinID == 0 && west(p.x,p.y).to == E){
			qu.push(point(p.x-1,p.y));
		}
		if(east(p.x,p.y).basinID == 0 && east(p.x,p.y).to == W){
			qu.push(point(p.x+1,p.y));
		}
		if(south(p.x,p.y).basinID == 0 && south(p.x,p.y).to == N){
			qu.push(point(p.x,p.y+1));
		}
		qu.pop();
	}
}
*/

void mapT::scan_basin(basin &b){
	scan_basin_impl(b.sink_x,b.sink_y);
}

void mapT::print(ostream &o){
	char *marks = "abcdefghijklmnopqrstuvwxyz";
	char *p = marks;
	for(int y=0; y<h; ++y){
		for(int x=0; x<w; ++x){
			char &basin_name = basin_list[at(x,y).basinID-1].name;
			if(basin_name == '?'){
				basin_name = *p;
				p++;
			}
			o << basin_name;
			if(x != w-1){o << ' ';}
		}
		o << endl;
	}	
}


int mapT::solve(){
	scan_to();

	for(vector<basin>::iterator i = basin_list.begin(), e=basin_list.end(); i != e; ++i){
		scan_basin(*i);
	}

	return 0;
}

int main(){
	input_read("J:\\g\\B-large.in");
	ofstream o("J:\\g\\B-large.out");

	int n = 0;
	for(vector<mapT>::iterator i = tests.begin(), e = tests.end(); i != e; ++i){
		(*i).solve();
		o << "Case #" << ++n << ":" << endl;
		(*i).print(o);
	}
}
