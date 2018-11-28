/* 2:00
   Rafael Schimassek
*/

#define MAX_HEIGHT 112
#define MAX_WIDTH 112

#include <iostream>

using namespace std;

int altmap [MAX_HEIGHT][MAX_WIDTH];
char namemap [MAX_HEIGHT][MAX_WIDTH];
char letters[] = "abcdefghijklmnopqrstuvwxyz";
int current_letter;


char iterateRiver(int y, int x, int height, int width) {

  //if this place already belongs to a basin then spread its letter
  if (namemap[y][x] != '\0')
    return namemap[y][x];
  
  char code;
  int next_y, next_x, a, yy, xx;
  int min = altmap[y][x];
  
  //search for lowest next destination, north > west > east > south
  for (a = 1; a <= 4; ++a) {
    switch (a) {
      case 1 : yy = y - 1; xx = x; break;
      case 2 : yy = y; xx = x - 1; break;
      case 3 : yy = y; xx = x + 1; break;
      case 4 : yy = y + 1; xx = x; break;
    }
    //if within the maps bounds
    if (yy >= 0 && yy < height && xx >= 0 && xx < width) {
      if (min > altmap[yy][xx]) {
        min = altmap[yy][xx];
        next_y = yy;
        next_x = xx;
      }
    }
  }
  
  //if a lower found, then proceed through there
  if (min < altmap[y][x])
    code = iterateRiver(next_y, next_x, height, width);
    
  //else it means this is an undiscovered sink, so get a code and spread it for adjacent sinks and backtrack
  else {
    code = letters[current_letter];
    ++current_letter;
  }
  
  //at least paint this square with the code and return it for backtracking
  namemap[y][x] = code;
  return code;
  
}
      


int main () {

  int x, y, cc;
  int num_maps, height, width;
  cin >> num_maps;
  
  //for each map
  for (cc = 0; cc < num_maps; ++cc) {
  
    current_letter = 0;
    
    //draw map
    cin >> height >> width;
    for (y = 0; y < height; ++y) {
      for (x = 0; x < width; ++x) {
        cin >> altmap[y][x];
        namemap[y][x] = '\0';
      }
    }
    
    //now start from the beginning and pass through all the map
    for (y = 0; y < height; ++y) {
      for (x = 0; x < width; ++x) {
        if (namemap[y][x] == '\0')
          iterateRiver(y, x, height, width);
      }
    }
    
    //and finally output it
    cout << "Case #"<<(cc+1)<<":\n";
    for (y = 0; y < height; ++y) {
      for (x = 0; x < width; ++x) {
        cout << namemap[y][x] << " ";
      }
      cout << '\n';
    }
    
  }
  
  return 0;
}
