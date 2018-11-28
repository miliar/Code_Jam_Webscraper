
#include <tchar.h>
#include <fstream>
#include <iostream>
#include <map>

using namespace std;

struct Offset {
  unsigned int nRounds, nEurosThis, nEurosBefore, nRemainder;
};

unsigned int R,k,N,nOffset,E=0;
unsigned int ai[1001];

Offset CreateOffset()
{
  unsigned int s=nOffset;
  int i=0, nRounds=0;
  Offset o;
  bool bWrapAround=false;

  o.nEurosBefore = E;
  o.nEurosThis = 0;

  while ( R && !bWrapAround )
  {
    while ( s+ai[i] <= k ) 
    {
      if ( i < N )
      {
        s += ai[i++];
      }
      else
      {
        bWrapAround = true;
        break;
      }
    }
    if ( !bWrapAround )
    {
      o.nEurosThis += s;
      s = 0;
      nRounds++;
      R--;
    }
  }

  o.nRemainder = s;
  o.nRounds = nRounds;
  return o;  
}


int _tmain(int argc, _TCHAR* argv[])
{
  int T;
  ifstream input;
  ofstream output;
  string s;
  map<unsigned int, Offset> m;
  map<unsigned int, Offset>::iterator it;
  Offset o;
  unsigned int sum;


  // initialize
  if ( argc != 3 ) return -1;
  input.open( argv[1] );
  if ( !input ) return -1;
  output.open( argv[2] );
  input >> T;

  for ( int t=0; t < T; t++ )
  {
    input >> R;
    input >> k;
    input >> N;
    m.clear();
    sum = 0;
    for ( int i=0; i < N; i++ )
    {
      input >> ai[i];
      sum += ai[i];
    }
    if ( sum <= k )
    {
      E = sum*R;
    }
    else
    {
      ai[N] = ai[0];
      nOffset = 0;
      E = 0;
      while (R)
      {
        it = m.find( nOffset );
        if ( it == m.end() )
        {
          o = CreateOffset();
          if ( R )
          {
            m[nOffset] = o;
            nOffset = o.nRemainder;
          }
          E += o.nEurosThis;
        }
        else
        {
          if ( it->second.nRounds <= R )
          {
            E += it->second.nEurosThis;
            R -= it->second.nRounds;
            nOffset = it->second.nRemainder;
          }
          else
          {
            o = CreateOffset();
            E += o.nEurosThis;
          }
        }
      }
    }

    output << "Case #" << t+1 << ": " << E << endl;  
  }
  input.close();
  output.close();


	return 0;
}

