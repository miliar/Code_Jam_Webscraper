#include<stdio.h>
#include<string>
#include<vector>
#include<map>
#include<set>
#include<list>
#include<algorithm>
#include<stdlib.h>
#include<queue>
#include<iostream>
typedef long long LL;
using namespace std;

#define MAXB 70
#define MAXSUM 2500

#define MOD 1000000007

long long inv( long long a )
{
  long long P = MOD;
  LL ret = 1;
  for( LL t = 1, x = a; t <= P-2; t <<= 1, x = (x * x) % P ){
    if( (P-2) & t )
      ret = (ret * x) % P;
  }
  return ret;
}

long long solveADP[MAXB+1][MAXB+1][MAXSUM];
int solveAvisited[MAXB+1][MAXB+1];

long long *solveA( int b, int B )
{
  long long *dp = solveADP[b][B];
  assert( 0 <= b && b <= MAXB );
  assert( 0 <= B && B <= b );
  if( solveAvisited[b][B] ) return dp;
  memset( dp, 0x00, sizeof(solveADP[b][B]) );
  solveAvisited[b][B] = 1;

  if( B == 0 ){ // b == 0
    dp[0] = 1;
    return dp;
  }
  if( B == 1 ){
    for( int i = 0; i < b; i ++ )
      dp[i] = 1;
    return dp;
  }
  // B >= 2
  for( int i = B-1; i < b; i ++ ){
    long long *dp2 = solveA( i, B-1 );
    for( int s = 0; s < MAXSUM-i; s ++ )
      dp[s+i] = (dp[s+i] + dp2[s]) % MOD;
  }
  return dp;
}

vector<long long> sum;

long long factTable[100];
long long combTable[128][128];
long long FACT(int N)
{
  assert( 0 <= N && N <= MAXB );
  return factTable[N];
}


long long COMB(int A, int B)
{
  assert( 0 <= B && B <= A && A <= MAXB );
  if( combTable[A][B] < 0 ){
    combTable[A][B] = FACT(A) * inv( FACT(B) * FACT(A-B) % MOD ) % MOD;
  }
  return combTable[A][B];
}
long long solveBDP[100][MAXB][MAXB+10];

long long solveB( int b,    const int pos, const int carry, const int num )
{
  assert( carry <= (b >> 1) );
  if( pos < 0 ){
    if( num == 0 && carry == 0 ) return 1;
    else return 0;
  }
  assert( pos < 100 );
  assert( carry < MAXB );
  assert( num <= MAXB );

  long long thisSum = sum[pos];
  if( num == 0 ){
    if( pos == 0 && carry == thisSum )
      return 1;
    else
      return 0;
  }
  // num >= 1

  if( solveBDP[pos][carry][num] >= 0 ) return solveBDP[pos][carry][num];
//  cerr << pos << " " << carry << " " << num << endl;

  long long ret = 0;

  // contain0
  for( int num2 = 1; num2 <= num; num2 ++ ){
    long long *dp = solveA( b - 1, num - 1 );
    for( int s = thisSum - carry - (num-1), carry2 = 0; s < MAXSUM; s += b, carry2 ++ ){
      if( s < 0 ) continue;
      long long v = (long long)dp[s];
      if( v == 0 ) continue;
      v = v * FACT(num2) % MOD;
      v = v * COMB(num - 1, num - num2) % MOD;
      if( v == 0 ) continue;
      v = v * solveB( b, pos - 1, carry2, num2 ) % MOD;
      ret = (ret + v) % MOD;
    }
  }
  
  // !contain0
  for( int num2 = 0; num2 <= num && num < b; num2 ++ ){
    long long *dp = solveA( b - 1, num );
    for( int s = thisSum - carry - (num), carry2 = 0; s < MAXSUM; s += b, carry2 ++ ){
      if( s < 0 ) continue;
      long long v = (long long)dp[s];
      assert(v >= 0);
      if( v == 0 ) continue;
      v = v * FACT(num2) % MOD;
      assert(v >= 0);
      v = v * COMB(num, num - num2) % MOD;
      assert(v >= 0);
      if( v == 0 ) continue;
      assert(v >= 0);
      v = v * solveB( b, pos - 1, carry2, num2 ) % MOD;
      assert(v >= 0);
      ret = (ret + v) % MOD;
      assert(ret >= 0);
    }
  }

  ret %= MOD;
  assert(ret >= 0);
  solveBDP[pos][carry][num] = ret;
//  cerr << pos << " " << carry << " " << num << " = " << solveBDP[pos][carry][num] << endl;
  return ret;
}

int main( void )
{
  memset( combTable, 0xff, sizeof(combTable) );
{
long long f = 1;
for( int i = 0; i <= MAXB; i ++ ){
  factTable[i] = f;
  cerr << i << " " << f << endl;
  f *= i+1;
  f %= MOD;
}
}

  memset( solveAvisited, 0x00, sizeof(solveAvisited) );
  for( int b = 0; b <= MAXB; b ++ ){
  for( int B = 0; B <= b; B ++ ){
    solveA( b, B );
    }
  }
/*
  for( int s = 0; s < MAXSUM; s ++ ){
    printf( "%d: %d\n", s, solveADP[70][70][s] );
  }
  for( int s = 0; s < MAXSUM; s ++ ){
    printf( "%d: %d\n", s, solveADP[70][35][s] );
  }
*/


 

  int T;
  cin >> T;
  for( int CC = 1; CC <= T; ++ CC ){
    long long N, B;
    cin >> N >> B;

    sum.clear();
    while( N > 0 ){
      sum.push_back( N % B );
      N /= B;
    }
    reverse( sum.begin(), sum.end() );

    long long ret = 0;
    memset( solveBDP, 0xff, sizeof(solveBDP) );
    for( int num = 1; num <= B; num ++ ){
//      cerr << num << endl;
      ret += solveB( B,   sum.size() - 1, 0, num );
      ret %= MOD;
    }
    printf( "Case #%d: %lld\n", CC, ret % MOD );
  }
}
