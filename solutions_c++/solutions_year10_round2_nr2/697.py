#include <string.h>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <list>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>
#include <queue>
#include <sstream>
#include <fstream>
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
#define SZ(x) (int)(x.size())

#define for0n(i,n) for(i=0;i<n;i++)
#define for1n(i,n) for(i=1;i<=n;i++)
#define forn(i,j,n) for(i=j;i<n;i++)

const int inf = 2100000000;
const double pi = atan(1.0)*4.0;
const double eps = 1e-8;

int i, j, k, l, ans;
int N, K, B, T;
int nCases;
int d, n;

class Chicken {
public:
  int speed;
  int position;
  bool canMakeIt;
  int swapsRequired;
};

Chicken chicks[50];

int main (int argc, char **argv)
{
  if (argc < 2) {
    printf("Specify input file\n");
    return -1;
  }

  fstream inFile(argv[1], fstream::in);
  fstream outFile("output.txt", fstream::out);

  inFile >> nCases;
  cout << nCases << endl;
  for0n(i,nCases) {
    Chicken temp;
    int inBarn = 0;
    int canMakeIt = 0;

    inFile >> N >> K >> B >> T;
    for0n(j,N) {
      inFile >> chicks[j].position;
    }

    for0n(j,N) {
      inFile >> chicks[j].speed;
      chicks[j].canMakeIt = 
        (((float)B-(float)chicks[j].position)/(float)chicks[j].speed) <= (float)T;
      if (chicks[j].canMakeIt) {
        canMakeIt++;
      }
      chicks[j].swapsRequired = 0;
      //cout << (chicks[j].canMakeIt ? "T" : "F") << " ";
    }
    //cout << endl;
    for0n(j,N) {
      if (!chicks[j].canMakeIt){
        chicks[j].swapsRequired = inf;
        continue;
      }
      for(k = j+1; k < N; k++) {
        if ((chicks[k].speed < chicks[j].speed) &&
             !chicks[k].canMakeIt) {
          chicks[j].swapsRequired++;
        }
      }
      //cout << chicks[j].swapsRequired << " ";
    }
    //cout << endl;

#if 0
    for0n(j,T) {
      int n = N;
      int next = B;
      for0n(k,n) {
        //cout << chicks[N-k-1].position << " " ;
        if(chicks[N-k-1].position == B) {
          continue;
        }
        chicks[N-k-1].position += chicks[N-k-1].speed;
        //cout << chicks[N-k-1].position << " " ;
        if (chicks[N-k-1].position >= B) {
          chicks[N-k-1].position = B;
          inBarn++;
        } else if (chicks[N-k-1].position > next) {
          chicks[N-k-1].position = next;
        } else {
          next = chicks[N-k-1].position;
        }
        //cout << chicks[N-k-1].position << endl;
      }
      for0n(k,N) {
        cout << chicks[k].position << " ";
      }      
      cout << endl;
    }
    if (inBarn >= K) {
      cout << "Enough in barn" << endl;
    }
#endif
    if (canMakeIt < K) {
      outFile << "Case #" << i+1 << ": " << "IMPOSSIBLE" << endl;
    } else {
      ans = 0;
      inBarn = 0;
      for0n(j,N) {
        if (inBarn >= K){
          break;
        }
        if (chicks[N-j-1].canMakeIt) {
          ans += chicks[N-j-1].swapsRequired;
          inBarn++;
        }
      }
      outFile << "Case #" << i+1 << ": " << ans << endl;
    }
  }

  outFile.close();
  return 0;
}
