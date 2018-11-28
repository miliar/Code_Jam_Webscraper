
#include <tchar.h>
#include <fstream>
#include <iostream>

using namespace std;


int _tmain(int argc, _TCHAR* argv[])
{
  int T,H,W;
  int nMinLevel;
  char * aLabelMap = 0;
  int  * aLevelMap = 0;
  char cLabel;

  ifstream input;
  ofstream output;

  // initialize
  if ( argc != 3 ) return -1;
  input.open( argv[1] );
  if ( !input ) return -1;
  output.open( argv[2] );

  input >> T;

  // process maps
  for ( int i=0; i<T; i++ )
  {
    input >> H >> W;

    if ( aLabelMap ) delete [] aLabelMap;
    if ( aLevelMap ) delete [] aLevelMap;

    aLabelMap = new char[W*H];
    aLevelMap = new int[W*H];
    cLabel = 'a';

    for ( int j=0; j < H*W; j++ )
    {
      input >> aLevelMap[j];
      aLabelMap[j] = 0;
    }
    for ( int Y=0, y, dy; Y < H; Y++ )
    {
      for ( int X=0, x, dx; X < W; X++ )
      {
        x = X;
        y = Y;
        while (1)
        {
          nMinLevel = aLevelMap[x+y*W];
          if ( (y > 0)   && ( aLevelMap[x+(y-1)*W] < nMinLevel ) ) { nMinLevel = aLevelMap[x+(y-1)*W]; dx =  0; dy = -1; }
          if ( (x > 0)   && ( aLevelMap[x-1+y*W]   < nMinLevel ) ) { nMinLevel = aLevelMap[x-1+y*W]  ; dx = -1; dy =  0; }
          if ( (x < W-1) && ( aLevelMap[x+1+y*W]   < nMinLevel ) ) { nMinLevel = aLevelMap[x+1+y*W]  ; dx =  1; dy =  0; }
          if ( (y < H-1) && ( aLevelMap[x+(y+1)*W] < nMinLevel ) ) { nMinLevel = aLevelMap[x+(y+1)*W]; dx =  0; dy =  1; }
          if ( nMinLevel >= aLevelMap[x+y*W] ) break;
          x += dx;
          y += dy;
        }       
        if ( !aLabelMap[x+y*W] )
        {
          aLabelMap[x+y*W] = cLabel++;
        }
        aLabelMap[X+Y*W] = aLabelMap[x+y*W];
      }
    }
    output << "Case #" << i+1 << ":" << endl;

    for ( int y=0; y < H; y++ )
    {
      for ( int x=0; x < W; x++ )
      {
        output << aLabelMap[x+y*W] << " ";
      }
      output << endl;
    }
  }

  input.close();
  output.close();
  if ( aLabelMap ) delete [] aLabelMap;
  if ( aLevelMap ) delete [] aLevelMap;

	return 0;
}

