#include<iostream>
#include<fstream>
#include<string>
using namespace std;

int cmap[ 26 ];
//int anti[ 26 ];

void work()
{
  string str;
  int i , len , cnt , t;
  
  cin>>t;
  getline( cin , str );
  cnt = 1;
  while( cnt <= t)
    {
      //cin>>str;
      getline( cin , str );
      len = str.size();
      //cout<<str<<"\n";
      cout<<"Case #"<<cnt<<": ";
      for( i = 0 ; i < len ; ++ i )
        if( str[ i ] not_eq ' ' )
          cout<<char( cmap[ str[ i ] - 'a' ] + 'a' );
        else
          cout<<' ';
      cout<<"\n";
      ++ cnt;
    }
  return ;
}

void init()
{
  string a[ 3 ] , b[ 3 ];
  int len , cnt;

  b[ 0 ] = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
  a[ 0 ] = "our language is impossible to understand";
  b[ 1 ] = "de kr kd eoya kw aej tysr re ujdr lkgc jv";
  a[ 1 ] = "so it is okay if you want to just give up";
  b[ 2 ] = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
  a[ 2 ] = "there are twenty six factorial possibilities";
 

  cnt = 0;
  while( cnt < 3 )
    {
      //getline( cin , a );
      //getline( cin , b );
      len = b[ cnt ].size();
      for( int i = 0 ; i < len ; ++ i )
        if( b[ cnt ][ i ] not_eq ' ' )
          {
            cmap[ b[ cnt ][ i ] - 'a' ] = a[ cnt ][ i ] - 'a';
            //anti[ a[ i ] - 'a' ] = b[ i ] - 'a';
          }
      ++ cnt;
    }
  //cmap[ 16 ] = 25;
  cmap[ 24 ] = 0;
  cmap[ 4 ] = 14;
  cmap[ 25 ] = 16;
  cmap[ 16 ] = 25;
  /*
  for( int i = 0 ; i < 26 ; ++ i )
    cout<<cmap[ i ]<<" ";
  cout<<"\n";
  */
  return ;
}

int main()
{
  init();
  /*
  for( int i = 0 ; i < 26 ; ++ i )
    cout<<anti[ i ]<<" ";
  cout<<"\n";
  */
  /*
  for( int i = 0 ; i < 26 ; ++ i )
    cout<<char( i + 'a' )<<"-"<<i<<" ";
  cout<<"\n";
  */
  work();

  return 0;
}
