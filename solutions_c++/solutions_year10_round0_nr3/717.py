#include<iostream>
#include<string>
using namespace std;

long long T, k, R, N;
long long groups[1010];
long long before[1010];
int nextIndex[1010];
long long allPeople;

int startIndex, endIndex;

bool canIncreaseEnd(){
  long long weightSoFar;
  long long moreWeight = groups[endIndex];
  if( startIndex == endIndex ){
    return false;
  }
  if( endIndex < startIndex ){
    // [sandy] wrap-around has happened
    weightSoFar = allPeople - before[startIndex] + before[endIndex];
  } else {
    weightSoFar = before[endIndex] - before[startIndex];
  }
  return ( weightSoFar + moreWeight <= k );
}

int succ( int i ){
  if( i == N-1 ){
    return 0;
  } else {
    return i+1;
  }
}

int main(){
  cin >> T;
  for( int t=1; t<=T; t++ ){
    cin >> R >> k >> N;
    memset( groups, -1, sizeof( groups ) );
    memset( before, -1, sizeof( before ) );
    memset( nextIndex, -1, sizeof( nextIndex ) );
    for( int g=0; g<N; g++ ){
      cin >> groups[g];
    }
    long long sum = 0;
    for( int g=0; g<N; g++ ){
      before[g] = sum;
      sum += groups[g];
    }
    allPeople = before[N-1] + groups[N-1];
    // [sandy] init two pointers
    endIndex = 0;
    for( startIndex = 0; startIndex<N; startIndex++ ){
      if( endIndex == startIndex ){
	endIndex = succ( endIndex );
      }
      while( canIncreaseEnd() ){
	endIndex = succ( endIndex );
      }
      nextIndex[startIndex] = endIndex;
    }
    int ticker = 0;
    long long wraps = 0;
    for( long long r=0; r<R; r++ ){
      if( nextIndex[ticker] <= ticker ){
	wraps++;
      }
      ticker = nextIndex[ticker];
    }
    cout << "Case #" << t << ": " << ( ( allPeople*wraps ) + before[ticker] ) << endl;
  }
}
