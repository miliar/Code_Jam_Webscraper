
#include <tchar.h>
#include <fstream>
#include <iostream>
#include <iomanip>

using namespace std;


class MyBigNum 
{
private:
  #define nDigits 9
  int aDigits[nDigits];

public:
  MyBigNum() 
  {
    Clear();
  };
  MyBigNum( const MyBigNum & rhs )
  {
    for (int i=0; i<nDigits; i++) 
    {
      aDigits[i]=rhs.aDigits[i];
    }
  }
  MyBigNum & operator=( const MyBigNum & rhs )
  {
    if ( &rhs == this ) return *this;
    for (int i=0; i<nDigits; i++) 
    {
      aDigits[i]=rhs.aDigits[i];
    }
    return *this;
  }
  bool operator<( MyBigNum & rhs )
  {
    for ( int i=nDigits-1; i>=0; i-- )
    {
      if ( aDigits[i] < rhs.aDigits[i] ) return true;
      if ( aDigits[i] > rhs.aDigits[i] ) return false;
    }
    return false;
  }
  bool operator==( MyBigNum & rhs )
  {
    for ( int i=0; i<nDigits; i++ )
    {
      if ( aDigits[i] != rhs.aDigits[i] ) return false;
    }
    return true;
  }
  bool operator!=( MyBigNum & rhs )
  {
    for ( int i=0; i<nDigits; i++ )
    {
      if ( aDigits[i] != rhs.aDigits[i] ) return true;
    }
    return false;
  }
  void Subtract( MyBigNum &x )
  {
    int iCarry=0;
    for ( int i=0; i<nDigits;i++ )
    {
      aDigits[i] -= (x.aDigits[i]+iCarry);
      if ( aDigits[i] < 0 )
      {
        aDigits[i] += 1000000;
        iCarry = 1;
      }
      else
      {
        iCarry = 0;
      }
    }
  }
  void Clear() 
  {
    for (int i=0; i<nDigits; i++) aDigits[i]=0;
  };
  void ShiftIn( int c )
  {
    int iCarry;
    for (int i=0; i<nDigits; i++) 
    {
      aDigits[i] *= 10;
      aDigits[i] += i ? iCarry : c;
      if ( aDigits[i] > 999999 )
      {
        iCarry = aDigits[i] / 1000000;
        aDigits[i] -= iCarry * 1000000;
      }
      else 
      {
        iCarry=0;
      }
    }
  };
  void ShiftLeft()
  {
    for ( int i=nDigits-1; i>0; i-- )
    {
      aDigits[i] = aDigits[i-1];
    }
  }
  void ShiftRight()
  {
    for ( int i=0; i<nDigits-1; i++ )
    {
      aDigits[i] = aDigits[i+1];
    }
  }
  void ReadNumber( ifstream & input )
  {
    char c = 0;
    while ( c < '0' || c > '9' )
    {
      input.read( &c, 1);
    }
    while ( c >= '0' && c <= '9' )
    {
      ShiftIn( c-'0' );
      input.read( &c, 1);
      //input >> c;
    }
  };
  void WriteNumber( ofstream & output )
  {
     int i = nDigits-1;
     while ( aDigits[i] == 0 && i>0 ) i--;
     output << aDigits[i--];
     for ( ; i>=0; i-- )
     {
       output << setw(6) << setfill('0') << aDigits[i];
     }
  };
};

MyBigNum num[1000];
MyBigNum dnum[1000];

int kk=0;

MyBigNum GetGCD( int n, MyBigNum *a )
{
  bool bFound = false;
  MyBigNum *pMin,d;

  while ( !bFound )
  {
    kk++;
    bFound = true;
    for ( int i=1; i<n; i++ )
    {
      if ( a[i] != a[0] )
      {
        bFound = false;
        break;
      }
    }
    if ( bFound ) break;

    pMin = &a[0];
    for ( int i=1; i<n; i++ )
    {
      if ( a[i] < *pMin )
      {
        pMin = &a[i];
      }
    }
    for ( int i=0; i<n; i++ )
    {
      if ( *pMin < a[i] )
      {
        d = *pMin;
        while ( d < a[i] ) d.ShiftLeft();
        d.ShiftRight();
        a[i].Subtract( d );
      }
    }
  }
  return a[0];
}

int _tmain(int argc, _TCHAR* argv[])
{
  int T;
  ifstream input;
  ofstream output;
  string s;
  unsigned int N, N2;
  MyBigNum *pbnMin,k,v,k2,x;
  int iMin;
  bool bDublicate;

  // initialize
  if ( argc != 3 ) return -1;
  input.open( argv[1] );
  if ( !input ) return -1;
  output.open( argv[2] );
  input >> T;

  for ( int t=0; t < T; t++ )
  {
    input >> N;
    N2 = 0;

    for ( int i=0; i< N; i++ )
    {
      x.Clear();
      x.ReadNumber( input );
      bDublicate = false;
      for ( int j=0; j < N2; j++ )
      {
        if ( x == num[j] )
        {
          bDublicate = true;
          break;
        }
      }
      if ( !bDublicate )
      {
        num[N2++] = x;
      }
    }
    
    pbnMin = &num[0];
    iMin = 0;
    for (int i=1; i<N2; i++ )
    {
      if ( num[i] < *pbnMin  ) 
      {
        pbnMin=&num[i];
        iMin = i;
      }
    }
    if ( N2 == 2 )
    {
      k = num[1-iMin];
      k.Subtract(num[iMin]);
    }
    else
    {
      for ( int i=0, int j=0; i<N2; i++ )
      {
        if ( i != iMin )
        {
          dnum[j] = num[i];
          dnum[j].Subtract(num[iMin]);
          j++;
        }
      }
      k = GetGCD( N2-1, dnum );
    }

    v = num[0];
    while ( k < v )
    {
      k2 = k;
      k2.ShiftLeft();
      while ( k2 < v )
      {
        k2.ShiftLeft();
      }
      k2.ShiftRight();
      v.Subtract( k2 );
    }
  //  k.Subtract( v );

   /*   output << "k =";
      k.WriteNumber( output );
      output << " - ";
      v.WriteNumber( output );
      output << " -> ";*/
      k.Subtract( v );
    /*  k.WriteNumber( output );
      output << "\n";*/



/*
    for ( int i=0; i<N-1; i++ )
    {
      dnum[i].WriteNumber( output );
      output << "\n";
    }*/


    /*
    for ( int i=0; i< N; i++ )
    {
      num[i].WriteNumber( output );
      output << "\n";
    }
    */


    output << "Case #" << t+1 << ": ";
    k.WriteNumber( output );
    output << endl;  
  }
  input.close();
  output.close();


	return 0;
}

