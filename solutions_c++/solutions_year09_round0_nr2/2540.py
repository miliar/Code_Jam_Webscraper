#include <cstdlib>
#include <iostream>
#include <utility>
#include <fstream>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

inline int c(int x, int y, int W)
{
    return x + y*W;
}

inline void cb(int c, int W, int & x, int & y)
{
     x = c % W;
     y = c / W;
}


class Cell
{
   public:
         Cell(): altitude(0),x(0),y(0), sink_x(-1), sink_y(-1) {};
         Cell(int alt_in, int x_in, int y_in): altitude(alt_in),
            x(x_in), y(y_in), sink_x(-1), sink_y(-1) {};
          int ret_alt() const { return altitude; }
          int ret_sink_x() { return sink_x; }
          int ret_sink_y() { return sink_y; }

          void find_sink(vector<Cell> & map, int H, int W);
          void set_altitude(int alt_in){ altitude = alt_in; }
          void set_sink_x(int sink_x_in){ sink_x = sink_x_in; }
          void set_sink_y(int sink_y_in){ sink_y = sink_y_in; }
          int x, y;
   private:
      int altitude;
      int sink_x, sink_y;
};

void Cell::find_sink(vector<Cell> & map, int H, int W)
{
     Cell * tc;
     Cell * mc = &map[c(x,y,W)];
     int min_alt =50000;
     // Check south
     if ((y+1) < H)
     {
         tc = &map[c(x,y+1,W)];
         if (tc->ret_alt() < mc->ret_alt() && 
             tc->ret_sink_x() >= 0 &&
             tc->ret_alt() <= min_alt)
         {
            min_alt = tc->ret_alt();
            sink_x = tc->ret_sink_x();
            sink_y = tc->ret_sink_y();
         }
     }
     // Check east
     if ((x+1) < W)
     {
         tc = &map[c(x+1,y,W)];
         if (tc->ret_alt() < mc->ret_alt() && 
             tc->ret_sink_x() >= 0 &&
             tc->ret_alt() <= min_alt)
         {
            min_alt = tc->ret_alt();
            sink_x = tc->ret_sink_x();
            sink_y = tc->ret_sink_y();
         }
     }
     // Check west
     if ((x-1) >= 0)
     {
         tc = &map[c(x-1,y,W)];
         if (tc->ret_alt() < mc->ret_alt() && 
             tc->ret_sink_x() >= 0 &&
             tc->ret_alt() <= min_alt)
         {
            min_alt = tc->ret_alt();
            sink_x = tc->ret_sink_x();
            sink_y = tc->ret_sink_y();
         }
     }
     // Check north
     if ((y-1) >= 0)
     {
         tc = &map[c(x,y-1,W)];
         if (tc->ret_alt() < mc->ret_alt() && 
             tc->ret_sink_x() >= 0 &&
             tc->ret_alt() <= min_alt)
         {
            min_alt = tc->ret_alt();
            sink_x = tc->ret_sink_x();
            sink_y = tc->ret_sink_y();
         }
     }
     // check if we're the sink
     if (sink_x == -1)
     {
        sink_x = x;
        sink_y = y;
     }

}


inline bool Altitude_Compare (const Cell & A,const Cell & B)
{ 
     return (A.ret_alt() < B.ret_alt()); 
}


int main(int argc, char *argv[])
{
	ifstream infile;
    int T, H, W;
    vector<Cell> Cell_Process;
    vector<Cell> Cell_Map;
	infile.open(argv[1]);
	if (!infile)
	{
	   cout << "Invalid file name" << endl;
	   exit(1);
	}
    infile >> T;

	for (int i=0; i < T; i++)
	{
        infile >> H >> W;  

        int altitude;
        for (int y = 0; y < H; y++)
        {
            for (int x = 0; x < W; x++)
            {
                infile >> altitude;
                Cell temp_cell(altitude, x, y);
                Cell_Process.push_back(temp_cell);
                Cell_Map.push_back(temp_cell);
             }
        }
        sort(Cell_Process.begin(), Cell_Process.end(), Altitude_Compare);

        for(vector<Cell>::iterator it = Cell_Process.begin(); it != Cell_Process.end(); it++)
        {
           Cell_Map[c(it->x,it->y,W)].find_sink(Cell_Map, H, W);                        
        }

        Cell * tc;
        map<int,char> out_map;
        char current_char = 'a'-1;
		cout << "Case #" << i+1 << ": " << endl;

        for (int y = 0; y < H; y++)
        {
            for (int x = 0; x < W; x++)
            {
               tc = &Cell_Map[c(x,y,W)];
               if (out_map.count(c(tc->ret_sink_x(),tc->ret_sink_y(),W)))
                  cout << out_map[c(tc->ret_sink_x(),tc->ret_sink_y(),W)] << " ";
               else
               {
                   cout << ++current_char << " ";
                   out_map[c(tc->ret_sink_x(),tc->ret_sink_y(),W)] = current_char;
               }
               
            }
            cout << endl;
        }
        

        Cell_Process.clear();
        Cell_Map.clear();
    }

    return EXIT_SUCCESS;
}
