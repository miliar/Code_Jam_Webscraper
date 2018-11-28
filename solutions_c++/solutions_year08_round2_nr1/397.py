#include <cstdio>
#include <iostream>
#define MAXN 100000+10
using namespace std;
typedef long long LL;

LL t[ 9 ];

void clear()
{
  for(int x=0; x<9; x++)
    t[ x ] = 0;
}

inline void add(LL x, LL y)
{
  int modX = x % 3;
  int modY = y % 3;
  t[ modX * 3 + modY ]++;
}


LL computeAdd(int X, int Y, int Z)
{
  int Xx = X / 3;
  int Xy = X % 3;
  
  int Yx = Y / 3;
  int Yy = Y % 3;
  
  int Zx = Z / 3;
  int Zy = Z % 3;
  
  if( ( Xx + Yx + Zx ) % 3 != 0 )
    return 0;
  
  if( ( Xy + Yy + Zy ) % 3 != 0 )
    return 0;
  
  int stop = 0;
  if( X == Y  &&  X == Z )
    return t[ X ] * ( t[ X ] - 1 ) * ( t[ X ] - 2 );
  
  if( X == Y )
    return t[ X ] * ( t[ X ] - 1 ) * t[ Z ];
  
  if( X == Z )
    return t[ X ] * ( t[ X ] - 1 ) * t[ Y ];
  
  if( Y == Z )
    return t[ Y ] * ( t[ Y ] - 1 ) * t[ X ];
  
  return t[ X ] * t[ Y ] * t[ Z ];
}


LL compute()
{
  LL ans = 0;
  for(int x=0; x<9; x++)
    for(int y=0; y<9; y++)
      for(int z=0; z<9; z++)
        ans += computeAdd(x, y, z);
  return ans;
}


int main()
{
  int ilz;
  scanf("%i", &ilz);
  for(int xz=1; xz<=ilz; xz++)
  {
    int n, A, B, C, D, x0, y0, M;
    scanf("%i", &n);
    scanf("%i%i%i%i", &A, &B, &C, &D);
    scanf("%i%i", &x0, &y0);
    scanf("%i", &M);
    
    clear();
    
    LL _X = x0;
    LL _Y = y0;
    add(_X, _Y);
    for(int i=1; i<=n-1; i++)
    {
      _X = (A * _X + B) % M;
      _Y = (C * _Y + D) % M;
      add(_X, _Y);
    }
    
    LL ans = compute() / 6;
    cout << "Case #" << xz << ": " << ans << endl;
  }
  return 0; 
}
