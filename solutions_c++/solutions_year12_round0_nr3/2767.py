#include<iostream>
#include<string>
#define MAXN 2300
using namespace std;

int ans , a , b;
//bool hash[ MAXN ][ MAXN ];

void count()
{
  int j , k;
  int len , num , nm;
  char s[ 20 ];
  int thash[ 10 ];
  bool exist;

  for( int i = a ; i <= b ; ++ i )
    {
      //num to str
      thash[ 0 ] = 0;
      len = 0;
      num = i;
      do{
        s[ len ++ ] = num % 10 + 48 ; 
        num /=10;
      }while( num );
      
      //str to num & trans
      for( j = len - 1 ; j > 0 ; -- j )
        {
          nm = 0;
          for( k = j - 1  ; k >= 0 ; -- k )
            nm = nm * 10 + ( s[ k ] - 48 );          
          for( k = len - 1 ; k >= j ; -- k )
            nm = nm * 10 + ( s[ k ] - 48 );
          //cout<<nm<<" "<<i<<"\n";
          exist = false;
          for( k = 1 ; k <= thash[ 0 ] ; ++ k )
            if( thash[ k ] == nm )
              { exist = true ; break; }
          if( not exist and nm > i and nm <= b )
            {
              thash[ ++ thash[ 0 ] ] = nm; 
              /*
              if( not hash[ i ][ nm ] )
                hash[ i ][ nm ] = true;
              else
                cout<<i<<" "<<nm<<"\n";
              */
              ++ ans;
            }
        }
    }
  return ;
}

int main()
{
  int t , cnt , i;
  
  //init();
  
  cin>>t;
  cnt = 1;
  while( cnt <= t )
    {
      cin>>a>>b;
      ans = 0;
      count();
      cout<<"Case #"<<cnt<<": "<<ans<<"\n";
      ++ cnt;
    }

  return 0;
}
