//B. Train Timetable
#include <cstdio>
#include <algorithm>
#define FIRST 0
#define SECOND 1
#define MAX_N 100+10
#define MAX_NX 100+10
using namespace std;

struct Timetable
{
  int t[ 2 ];  //column: 0-departure, 1-arrival
  
  int getColumn(int nr)
  {
    return t[ nr ];
  }
  
  void set(int departure, int arrival)
  {
    t[ 0 ] = departure;
    t[ 1 ] = arrival;
  }
};


void getColumn(int tsize, int columnNumber, int tnew[], Timetable t[])
{
  for(int x=0; x<tsize; x++)
    tnew[ x ] = t[ x ].getColumn( columnNumber );
}


int cnt_before(int TAsize, int TA[], int TBsize, int TB[])  //TB - main
{
  if( TAsize == 0 )
    return 0;
  
  sort( TA, TA + TAsize );
  sort( TB, TB + TBsize );
  
  int ans = 0;
  int a = 0;
  for(int b=0; b<TBsize; b++)
  {
    if( TB[ b ] >= TA[ a ] )
    {
      ans++;
      a++;
      if( a >= TAsize )
        break;
    }
  }
  
  return ans;
}


inline int toNumber(char a)
{
  return a - '0';
}


int toMinutes(char t[])
{
  int h1 = toNumber( t[ 0 ] );
  int h2 = toNumber( t[ 1 ] );
  int m1 = toNumber( t[ 3 ] );
  int m2 = toNumber( t[ 4 ] );
  return ( h1 * 10 + h2 ) * 60 + m1 * 10 + m2;
}

void readDataToTable(int count, int T, Timetable t[])
{
  char departureTime[ 5 + 4 ];
  char arrivalTime[ 5 + 4 ];
  for(int x=0; x<count; x++)
  {
    scanf("%s%s", departureTime, arrivalTime);
    int iDepartureTime = toMinutes( departureTime );
    int iArrivalTime = toMinutes( arrivalTime ) + T;
    t[ x ].set( iDepartureTime, iArrivalTime );
  }
}


int main()
{
  Timetable TA[ MAX_NX ];
  Timetable TB[ MAX_NX ];
  
  int ilz;
  scanf("%i", &ilz);
  for(int xz=0; xz<ilz; xz++)
  {
    int T;  //turnaround time
    scanf("%i", &T);
    
    int NA, NB;
    scanf("%i%i", &NA, &NB);
    
    readDataToTable(NA, T, TA);
    readDataToTable(NB, T, TB);
    
    int tnew1[ MAX_NX ];
    int tnew2[ MAX_NX ];
    
    getColumn( NA, SECOND, tnew1, TA );
    getColumn( NB, FIRST, tnew2, TB );
    int ansNB = NB - cnt_before( NA, tnew1, NB, tnew2 );
    
    getColumn( NB, SECOND, tnew1, TB );
    getColumn( NA, FIRST, tnew2, TA );
    int ansNA = NA - cnt_before( NB, tnew1, NA, tnew2 );
    
    printf("Case #%i: %i %i\n", xz + 1, ansNA, ansNB);
  }
  return 0;
}
