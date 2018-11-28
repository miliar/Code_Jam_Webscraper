#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

const int MAX_N = 1000;

int main()
{
  int g[MAX_N];
  vector<bool> first;
  unsigned long int total;
  ifstream fin( "input" );
  ofstream fout( "output" );
  int T;
  fin >> T;
  for ( int t=1; t<=T; t++ )
    {
      total = 0;
      unsigned long int R, k;
      int N;
      fin >> R >> k >> N;
      for ( int i=0; i<N; i++ )
        {
          fin >> g[i];
        }
      int r = 0;
      int index = 0; // indice della fila
      int ote; // guadagno in un singolo giro
      int firstGroup;
      while ( r < R )
        {
          ote = 0;
          firstGroup = index;
	  for ( ;; )
            {
	      if ( ote + g[index] > k || ( index == firstGroup && ote )   ) // se la giostra è piena oppure sono finiti i gruppi
		break;
	      ote += g[index];
	      index = ( index + 1 ) % N;
	    }
	  r++;
          total += ote;
	}
      fout << "Case #" << t << ": " << total << "\n";
        
    }
    
  return 0;
}
