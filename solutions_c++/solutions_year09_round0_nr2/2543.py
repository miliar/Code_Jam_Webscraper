#include <iostream>
using namespace std;




typedef struct
{
  short alt;
  short drain; // index,  <0 == sink
  short sink;
} cell_t;


/// @return The index of the smallest altitude
short minalt( cell_t *cells, short *idx )
{
  short min, alt = 10000;
  for( int i=0; i<4; ++i )
  {
    if( idx[i] >= 0 && cells[idx[i]].alt < alt )
    {
      alt = cells[idx[i]].alt;
      min = i;
    }
  }
  return idx[min];
}


int main() {
  int maps, w, h, len, alt, minaltidx, from;
  int m, i;
  int tmp;
  short dirs[4]; // indecies (north, west, EAST, south)

  cin >> maps;
  cell_t *cells;
  for( m=0; m<maps; ++m ) 
  {
    cin >> h >> w;
    len = w*h;
    cells = new cell_t[len];

    for( i=0; i<len; ++i )
      cin >> cells[i].alt;

    for( i=0; i<len; ++i )
    {
      alt = cells[i].alt;

      dirs[0] = i-w;
      dirs[1] = i%w == 0 ? -1 : i-1;
      dirs[3] = i+w >= len ? -1 : i+w;
      dirs[2] = (i+1)%w == 0 ? -1 : i+1;

      minaltidx = minalt( cells, dirs );

      if( cells[minaltidx].alt < alt )
        cells[i].drain = minaltidx; // drains
      else
        cells[i].drain = -1; // tsasink
    }

    for( i=0; i<len; ++i )
    {
      from = i;
      while( (tmp = cells[from].drain) >= 0 )
        from = tmp;
      cells[i].sink = from;
    }

    int sinkcount = 0;
    cell_t *sink;
    cout << "Case #" << (m+1) << ":" << endl;
    for( i=0; i<len; ++i )
    {
      // first-time sink?
      sink = &cells[cells[i].sink]; 
      if( sink->drain == -1 )
      {
        ++sinkcount;
        sink->drain = -sinkcount - 1;
      }
      cout << (char)('a' - sink->drain - 2);
      if( (i+1) % w == 0 )
        cout << endl;
      else
        cout << " ";
    }

    delete [] cells;
  }

  return 0;
}

