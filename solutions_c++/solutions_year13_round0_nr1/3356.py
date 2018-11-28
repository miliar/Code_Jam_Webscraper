#include <cstdio>
#include <cstdint>
#include <cstring>
#include <cassert>
#include <vector>
#include <algorithm>
#include <unordered_map>
#include <iostream>
#include <sstream>

bool won(char* f, char toCheck)
{
  for ( int i = 0; i < 4; ++i )
  {
    // right left
    int j = 0;
    for (;j<4;++j)
      if ( ! ( *(f+j+i*4) == toCheck || *(f+j+i*4) == 'T' ) ) break;
    if ( j == 4 )
      return true;
    j = 0;
    for (;j<4;++j)
      if ( ! ( *(f+i+j*4) == toCheck || *(f+i+j*4) == 'T' ) ) break;
    if ( j == 4 )
      return true;
  }
  int j = 0;
  for (;j<4;++j)
    if ( ! ( *(f+5*j) == toCheck || *(f+j*5) == 'T' ) ) break;
  if ( j == 4 )
    return true;
  j = 0;
  for (;j<4;++j)
    if ( ! ( *(f+3+3*j) == toCheck || *(f+3+j*3) == 'T' ) ) break;
  if ( j == 4 )
    return true;
  return false;
}

const char *res[] = { "X won", "O won", "Draw", "Game has not completed" };

int main( int argn, char** argv )
{
  int ncases;
  scanf("%d",&ncases);
  for ( int icase = 0; icase<ncases; ++icase )
  {
    char f[17];
    for ( int i=0;i<4;++i)
      scanf("%s",f+i*4);
    
    const char* pres = "";
    if ( won( f, 'X' ) )
      pres = res[0];
    else if ( won( f, 'O' ) )
      pres = res[1];
    else if ( strchr( f, '.' ) == NULL )
      pres = res[2];
    else
      pres = res[3];
    printf("Case #%d: %s\n",icase+1,pres);
  }
  return 0;
}
