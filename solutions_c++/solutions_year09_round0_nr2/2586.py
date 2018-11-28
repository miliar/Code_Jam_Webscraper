#include <iostream>
#include <vector>

using namespace std;

class Cell {

      public:
      int altitude;
      char label;

      Cell() {
	    altitude = -1;
	    label = '-';
      }

      void Reset() {
	    altitude = -1;
	    label = '-';
      }
};

class Basin {

       public:
       int r;
       int c;
       int altitude;

};

int main() {

      Cell cellMap[100][100];

      int T = 0;	// Contains the number of maps

      int H = 0;	// Contains the height of the map

      int W = 0;	// Contains the width of the map

      cin >> T;

      // Read the T maps

      for( int i=0; i < T; i++ ) {


	    // Initially reset the cellMap values
	    for( int r = 0; r < 100; r++ ) {

		  for( int c = 0; c < 100; c++ ) {
			
			cellMap[r][c].Reset();
		  }

	    }
	    cin >> H;
	    cin >> W;

	    // Read the cell map altitude
	    for( int r = 0; r < H; r++ ) {

		  for( int c = 0; c < W; c++ ) {
			
			cin >> cellMap[r][c].altitude;
		  }
	    }

	    cellMap[0][0].label = 'a';	// The basin of the most North-Western cell is always labeled 'a'.
	     
	    char nextAlpha = 'a';

	    Basin objBasin;	// Temporary object to find basin of cell

	    for( int r = 0; r < H; r++ ) {

		  //cout << "W in for loop " << W << endl;
		  for( int c = 0; c < W; c++ ) {


			//cout << "C in for loop " << c << endl;

			objBasin.altitude = cellMap[r][c].altitude;
			objBasin.r = r;
			objBasin.c = c;

		  	// Find the basin among the neighbours
			
			// north	
			if((r-1) >= 0 ) {

			      if( cellMap[r-1][c].altitude < objBasin.altitude ) {

				    objBasin.r = r-1;
				    objBasin.c =c;
				    objBasin.altitude = cellMap[r-1][c].altitude;
			      }
			}

			// west
			if((c-1) >= 0 ) {

			      if( cellMap[r][c-1].altitude < objBasin.altitude ) {
				    objBasin.r = r;
				    objBasin.c =c-1;
				    objBasin.altitude = cellMap[r][c-1].altitude;
			      }
			}

			// East
			if((c+1) < W ) {

			      if( cellMap[r][c+1].altitude < objBasin.altitude ) {
				    objBasin.r = r;
				    objBasin.c = c+1;
				    objBasin.altitude = cellMap[r][c+1].altitude;
			      }
			}

			// south	
			if((r+1) < H ) {

			      if( cellMap[r+1][c].altitude < objBasin.altitude ) {
				    objBasin.r = r+1;
				    objBasin.c =c;
				    objBasin.altitude = cellMap[r+1][c].altitude;
			      }
			}

			if( cellMap[r][c].label == '-' ) {

			      if( cellMap[objBasin.r][objBasin.c].label != '-' ) {

				 cellMap[r][c].label = cellMap[objBasin.r][objBasin.c].label; 

			      } else {

				    nextAlpha++;
				    cellMap[r][c].label = nextAlpha;
				    cellMap[objBasin.r][objBasin.c].label = nextAlpha;
			      }

			} else {

			      if( cellMap[objBasin.r][objBasin.c].label == '-' ) {

				  cellMap[objBasin.r][objBasin.c].label = cellMap[r][c].label; 

			      } else {

				    if( cellMap[objBasin.r][objBasin.c].label != cellMap[r][c].label) {

					  if( cellMap[objBasin.r][objBasin.c].label < cellMap[r][c].label )
					  {
						nextAlpha--;
						for( int x= 0; x < H; x++ ) {
						      for( int y = 0; y < W; y++ ) {

							 if((x == r) && ( y == c))
							       continue;

							 if( cellMap[x][y].label == cellMap[r][c].label )
							 cellMap[x][y].label = cellMap[objBasin.r][objBasin.c].label;
							 else if(cellMap[x][y].label > cellMap[r][c].label )
							 cellMap[x][y].label= cellMap[x][y].label  - 1;
						      }
						}
						 cellMap[r][c].label = cellMap[objBasin.r][objBasin.c].label;

					  } else if( cellMap[objBasin.r][objBasin.c].label > cellMap[r][c].label )
					    {
						  nextAlpha--;
						  //cout << "SOMETHING WRONG" << endl;
						  for( int x= 0; x < H; x++ ) {
						      for( int y = 0; y < W; y++ ) {

							 if((x == objBasin.r) && ( y == objBasin.c))
							       continue;

							if( cellMap[x][y].label == cellMap[objBasin.r][objBasin.c].label  )
							     cellMap[x][y].label = cellMap[r][c].label  ;
						else if( cellMap[x][y].label > cellMap[objBasin.r][objBasin.c].label  )
							 cellMap[x][y].label= cellMap[x][y].label  - 1;
						      }
						}
						 cellMap[objBasin.r][objBasin.c].label = cellMap[r][c].label;
					    }

				    }
			      }

			}
			
		  }
	    } // End of map generation

	    cout << "Case #" << i+1 << ":" << endl;
	    for( int r= 0; r < H ; r++ ) {

		  for( int c=0; c < W; c++ ) {

			cout << cellMap[r][c].label << " ";
		  }
		  cout << endl;
	    }

	    

      } // End of reading maps for loop
} // End of main
