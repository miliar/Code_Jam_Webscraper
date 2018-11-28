#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <iomanip>
#include <string.h>
#include <set>

using namespace std;

#define NORTH (1<<3)
#define WEST (1<<2)
#define EAST (1<<1)
#define SOUTH (1)
#define ALL NORTH|WEST|EAST|SOUTH

class Point {
public:
    Point(){};
    Point(int a,int b) {
        x=a;
        y=b;
    }
    int x;
    int y;

    bool operator<(const Point &a) const {
        if (this->x==a.x) return (this->y)<a.y;
        else return  (this->x)<a.x;
    }
    bool operator== (const Point &a) const {
        return (a.x==this->x)&&(a.y==this->y);
    }

};


class Map {
public:
    int table[100][100];
    int table_tmp[100][100];
    int W,H;
    vector<Point> sinks;
    void clear() {
        for (int x=0;x<100;x++)
            for (int y=0;y<100;y++)
                table_tmp[y][x]=0;
    }

    void print_table() {
        for (int y=0;y<H;y++) {
            for (int x=0;x<W;x++) cout<<setw(4)<<table[y][x];
            cout<<endl;
        }
    }

    void print_table_tmp() {
        for (int y=0;y<H;y++) {
            for (int x=0;x<W;x++) cout<<setw(4)<<table_tmp[y][x];
            cout<<endl;
        }
    }
	
	void print_table_out() {
		char p=97;
		char map[30];
		for(int x=0;x<30;x++) map[x]=0;
		int z;
        for (int y=0;y<H;y++) {
            for (int x=0;x<W;x++) {
			  z=table_tmp[y][x];
			  if (!map[z]) {map[z]=p;p++;}
			  cout<<map[z];
			  if (x<W-1) cout<<" ";
			}
            cout<<endl;
        }
    }

    bool is_sink(int x,int y) {
        int z=table[y][x];
        //check for left to sink
        if (x>0) if (table[y][x-1]<z) return false;
        if (x<W-1) if (table[y][x+1]<z) return false;
        if (y>0) if (table[y-1][x]<z) return false;
        if (y<H-1) if (table[y+1][x]<z) return false;
		//if (x==9) cout<<"tt"<<endl;
        return true;
    }

    void find_sinks() {
        sinks.clear();
        int i=1;
        for (int y=0;y<H;y++)
            for (int x=0;x<W;x++) {
                if (is_sink(x,y)) {
                    Point P;
                    P.x=x;
                    P.y=y;
                    sinks.push_back(P);
                    table_tmp[y][x]=i;
					//cout<<"cos duzo, x "<<x<<" y "<<y<<" "<<i<<endl;
                    i++;
                }
            }
    }
    //where flow from a to
	void flow(Point a,int id){
	  Point P(a.x,a.y);
	  Point z;
	  P.x++;
	  z=flow(P);
	  //cout<<"z "<<P.x<<" "<<P.y<<" do "<<z.x<<" "<<z.y<<" bool "<<(a==z)<<"|"<<a.x<<" "<<a.y<<endl;
	  if (a==z) {table_tmp[P.y][P.x]=id;flow(P,id);}
	  //print_table_tmp();
	  P.x-=2;
	  z=flow(P);
	  //cout<<"z "<<P.x<<" "<<P.y<<" do "<<z.x<<" "<<z.y<<" bool "<<(a==z)<<"|"<<a.x<<" "<<a.y<<endl;
	  if (a==z) {table_tmp[P.y][P.x]=id;flow(P,id);}
	  P.y--;P.x++;
	  z=flow(P);
	  //cout<<"z "<<P.x<<" "<<P.y<<" do "<<z.x<<" "<<z.y<<" bool "<<(a==z)<<"|"<<a.x<<" "<<a.y<<endl;
	  if (a==z) {table_tmp[P.y][P.x]=id;flow(P,id);}
	  P.y++;P.y++;
	  z=flow(P);
	  //cout<<"z "<<P.x<<" "<<P.y<<" do "<<z.x<<" "<<z.y<<" bool "<<(a==z)<<"|"<<a.x<<" "<<a.y<<endl;
	  if (a==z) {table_tmp[P.y][P.x]=id;flow(P,id);}
	}
    Point flow(Point a) {
		//cout<<"check for "<<a.x<<" "<<a.y<<endl;
		if ( (a.x<0)||(a.y<0)||(a.x>=W)||(a.y>=H) ) return a;
		if (table_tmp[a.y][a.x]>0) return a;
        if (is_sink(a.x,a.y)) return a;
		
        //left up
        int z=table[a.y][a.x];
        int flow;//1=S 2=E 3=W 4=N 0=None
        int s=ALL;
        //left up
        if (a.x==0) s&=~WEST;
        if (a.x==W-1) s&=~EAST;
        if (a.y==0) s&=~NORTH;
        if (a.y==H-1) s&=~SOUTH;
	
        int x,y;
        int z2=z-1;
        int z3;
        flow=0;
		
		
        if (s&SOUTH) {
            z3=table[a.y+1][a.x];
            if (z3<=z2) {
                z2=z3;
                flow=1;
                x=a.x;
                y=a.y+1;
            }
        }

        if (s&EAST) {
            z3=table[a.y][a.x+1];
            if (z3<=z2) {
                z2=z3;
                flow=1;
                x=a.x+1;
                y=a.y;
            }
        }
        if (s&WEST) {
            z3=table[a.y][a.x-1];
            if (z3<=z2) {
                z2=z3;
                flow=1;
                x=a.x-1;
                y=a.y;
            }
        }
        if (s&NORTH) {
            z3=table[a.y-1][a.x];
            if (z3<=z2) {
                z2=z3;
                flow=1;
                x=a.x;
                y=a.y-1;
            }
        }
		//if ((a.y==1)&&(a.x==1) )cout<<"tt"<<z2<<endl;
        if (flow) return Point(x,y);
        return a;
    }
    void parse(istream& inn) {
        int L;
        inn>>L;
        //for (int x=0;x<L;x++) {
		for (int x=0;x<L;x++) {
			clear();
            //for(int x=0;x<l;x++){
            inn>>H>>W;
            
            for (int y=0;y<H;y++)
                for (int x=0;x<W;x++)
                    inn>>table[y][x];
			//if (x!=1) continue;
			//cout<<W<<" "<<H<<endl;
            //print_table();
            find_sinks();
			//print_table_tmp();
            for (vector< Point >::iterator it=sinks.begin();it!=sinks.end();it++) {
                Point P=(*it);
                int id=table_tmp[P.y][P.x];
		//		cout<<"-------- "<<(*it).x<<" "<<(*it).y<<" "<<id<<endl;
				flow(P,id);
			//	print_table_tmp();
                /*set<Point> groupset;
                groupset.insert(*it);
                while (groupset.size()){
                  vector< Point >::iterator=groupset.begin();

                }*/
                //cout<<(*it).x<<" "<<(*it).y<<" "<<endl;
            }
			  cout<<"Case #"<<x+1<<":"<<endl;
			  print_table_out();
        };
    };
};

int main(int argc,char** argv) {
	Map map;
    //ifstream myfile("data.txt");
    //map.parse(myfile);
	map.parse(cin);
    /*Point a;
    Point b;
    a.x=10;
    a.y=20;
    b.x=10;
    b.y=21;
    cout<<(a==b)<<endl;
    cout<<(a<b)<<endl;
    //parse(myfile);
	*/
}

