#include <iostream>
#include <cstring>
#include <cctype>
//#include <fstream>
//#include <map>
//#include <vector>
//#include <list>

using namespace std;

int min4(int a, int b, int c, int d) {
  int min = a;
  if (b < min)
    min = b;
  if (c < min)
    min = c;
  if (d < min)
    min = d;
  return min;
}

void update(int *tempbasin, int old, int n_ew, int H, int W) {
  for (int i = 0; i < H * W; i++) {
    if (tempbasin[i] == old)
	  tempbasin[i] = n_ew;
  }
}

int main()
{
  int T, H, W;
  char *basin;        //final alphabetical basin map
  int *tempbasin;     //intermediary map for assigning basin values
  int *alt;           //altitude map
  int here,n,w,e,s;   //current altitudes
  
  cin >> T;    // number of maps
  
  //loop through all the maps in input file
  for (int i = 0; i < T; i++) {
    int count = 1;      //current basin value
    cin >> H;   // height
	cin >> W;   // width
    
	// initialize tempbasin to hold all counts of 0
    tempbasin = new int[H * W];
    for (int j = 0; j < H *W; j++)
      tempbasin[j] = 0;
    
	// loop to get all the altitudes
	alt = new int[H * W];
	for (int j = 0; j < H; j++) {
	  for (int k = 0; k < W; k++)
	    cin >> alt[j * W + k];
    }
	
	// loop through the maps to mark basins
	for (int row = 0; row < H; row++) {
	  for (int col = 0; col < W; col++) {
	    // find all relevant altitudes
	    here = alt[row * W + col];
		n = w = e = s = 10001;    // initialize altitudes to disregard them
		if (row > 0)
          n = alt[(row-1) * W + col];
		if (row < H-1)
		  s = alt[(row+1) * W + col];
		if (col > 0)
		  w = alt[row * W + (col-1)];
		if (col < W-1)
		  e = alt[row * W + (col+1)];
		// Case1: no lower surroudings (sink)
		int min = min4(s,n,w,e);
		bool here0 = (tempbasin[row * W + col] == 0);
		if (here <= min) {
		  if (here0) {
		    tempbasin[row * W + col] = count;
		    count ++;
		  }
		}
		// Case2: flows to neighboring place
		else if (n == min) {
		  if (here0)
		    tempbasin[row * W + col] = tempbasin[(row-1) * W + col];
	      else
		    update(tempbasin, tempbasin[row * W + col], tempbasin[(row-1) * W + col], H, W);
		}
		else if (w == min) {
		  if (here0)
		    tempbasin[row * W + col] = tempbasin[row * W + (col-1)];
		  else
		    update(tempbasin, tempbasin[row * W + col], tempbasin[row * W + (col-1)], H, W);
	    }
		else if (e == min) {
		  bool e0 = (tempbasin[row * W + (col+1)] == 0);
		  if (here0) {
		    if (e0) {
			  tempbasin[row * W + col] = tempbasin[row * W + (col+1)] = count;
			  count ++;
			} else
			  tempbasin[row * W + col] = tempbasin[row * W + (col+1)];
		  } else {
		    if (e0)
			  tempbasin[row * W + (col+1)] = tempbasin[row * W + col];
			else
			  update(tempbasin, tempbasin[row * W + col], tempbasin[row * W + (col+1)], H, W);
		  }
		}
		else if (s == min) {
		  if (here0) {
			  tempbasin[row * W + col] = tempbasin[(row+1) * W + col] = count;
			  count ++;
		  } else {
			  tempbasin[(row+1) * W + col] = tempbasin[row * W + col];
		  }
		}
	  }
	}
	
	// loop through tempbasin converting it to the alphabet in basin
	int ascii = 'a';
	for (int j = 0; j < H * W; j++) {
	  count = tempbasin[j];
	  if (count != 0) {
	    for (int k = 0; k < H * W; k++) {
		  if (tempbasin[k] == count) {
		    basin[k] = (char)ascii;
			tempbasin[k] = 0;
		  }
		}
		ascii++;
	  }
	}

	// display the map
	cout << "Case #" << i+1 << ":" << endl;
	for (int j = 0; j < H; j++) {
	  for (int k = 0; k < W; k++)
	    cout << basin[j * W + k] << " ";
	  cout << endl;
	}
  }
  return 0;
}
