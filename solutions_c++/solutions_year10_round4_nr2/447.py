#include<iostream>
#include<string>
#include<cstring>
using namespace std;

long long reqd[2048];
long long cache[12][1050];
long long gameCost[1050];
long long ncases;
long long P;

const long long maxCost = 9999999999ll;

long long teams(){
  return 1<<P;
}

long long maxReqd( long long game ){
  return max( reqd[(game*2)-teams()], reqd[((game*2)+1)-teams()] );
}

bool isFirstGame( long long game ){
  return ( game >= (1<<(P-1)) );
}

long long minCost( long long game, long long taken ){
  if( isFirstGame( game ) ){
    long long most = maxReqd(game);
    if( taken+1<most ){
      return maxCost;
    } else if( taken+1 == most ){
      return gameCost[game];
    } else {
      return 0;
    }
  }
  if( cache[taken][game] != -1 ){
    return cache[taken][game];
  }
  long long takenScore = gameCost[game] + minCost( game*2, taken+1 ) + minCost( (game*2)+1, taken+1 );
  long long notTakenScore = minCost( game*2, taken ) + minCost( (game*2)+1, taken );
  long long ret = min( takenScore, notTakenScore );
  cache[taken][game] = ret;
  return ret;
}


int main(){
  cin >> ncases;
  for( int ncase=1; ncase<=ncases; ncase++ ){
    cin >> P;
    memset( reqd, -1, sizeof( reqd ) );
    memset( gameCost, -1, sizeof( gameCost ) );
    memset( cache, -1, sizeof( cache ) );
    for( long long i=0; i< (1<<P); i++ ){
      long long temp;
      cin >> temp;
      reqd[i] = P-temp;
    }
    // for line of length 2^(P-i)
    for( long long i=1; i<=P; i++ ){
      for( long long n=(1<<(P-i)); n<(1<<P-i+1); n++ ){
	cin >> gameCost[n];
      }
    }
    cout << "Case #" << ncase << ": " << minCost( 1, 0 ) << endl;
  }
}
