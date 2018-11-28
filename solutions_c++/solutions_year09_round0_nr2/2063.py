#include <iostream>
#include <string>
#include <vector>
#include <set>
using namespace std;

#define MIN(X,Y) ((X) < (Y) ? (X) : (Y))

int ** land;
int * land_arr;
char ** basin_id;
char * basin_arr;
int W;
int H;
int altitude;
int last_basin = 0;

int get_sink_id(int row, int column) {
  if (basin_id[row][column] < 30)
    return basin_id[row][column];
  
  int neighbors[4];
  for (int i = 0; i < 4; i++) {
    neighbors[i] = 10001;
  } 
  
  if (row > 0) 
     neighbors[0] = land[row-1][column];
  if (column > 0)
     neighbors[1] = land[row][column-1];
  if (column < W-1)
     neighbors[2] = land[row][column+1];
  if (row < H-1)
     neighbors[3] = land[row+1][column];
  
  int min_altitude = MIN(MIN(neighbors[0], neighbors[1]),
			 MIN(neighbors[2], neighbors[3]) );
  
  // basin_id = 255 at this point
  if (land[row][column] <= min_altitude) {
     basin_id[row][column] = last_basin++;
     return basin_id[row][column];
  }
  
  // at this point too
  int row0 = row;
  int column0 = column;
  
  if (neighbors[0] == min_altitude && neighbors[0] < land[row][column])
     row0--;
  else if (neighbors[1] == min_altitude && neighbors[1] < land[row][column])
     column0--;
  else if (neighbors[2] == min_altitude && neighbors[2] < land[row][column])
     column0++;
  else if (neighbors[3] == min_altitude && neighbors[3] < land[row][column])
     row0++;

  basin_id[row][column] = get_sink_id(row0, column0);
  return basin_id[row][column];
}

int main() {
   int T; // lands, height, width
   cin >> T;

   for (int i = 0; i < T; i++) {
      last_basin = 0;
      cin >> H >> W;
      land_arr = new int[H*W];
      basin_arr = new char[H*W];
      land = new int*[H];
      basin_id = new char*[H];
      for (int j = 0; j < H; j++) {
        land[j] = land_arr + j * W;
        basin_id[j] = basin_arr + j * W;
      }
      memset(basin_arr, 30, H*W);
      for (int j = 0; j < H; j++) {
    	 for (int k = 0; k < W; k++) {
  	     cin >> land[j][k];
    	 }
      }
      

      for (int j = 0; j < H; j++) {
    	  for (int k = 0; k < W; k++) {
	     basin_id[j][k] = get_sink_id(j, k);
        }
      }

      cout << "Case #" << i+1 << ":" << endl;
      for (int j = 0; j < H; j++) {
    	  for (int k = 0; k < W; k++) {
  	      cout << static_cast<char>(basin_id[j][k] + 'a');
   	      if (k < W-1) cout << " ";
    	  }
    	  cout << endl;
      }
      delete [] land;
      delete [] land_arr;
      delete [] basin_id;
      delete [] basin_arr;
   }
}
