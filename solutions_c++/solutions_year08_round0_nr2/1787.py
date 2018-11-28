#include<fstream>
#include<vector>
#include<string>
#include<algorithm>
#include<stdlib.h>

using namespace std;

class myTime {
      private:
              int hh;
              int mm;
      public:
             myTime( string strh, string strm )
             {
                     hh = atoi( strh.c_str() );
                     mm = atoi( strm.c_str() );
             }
             ~myTime()
             {
             }
             void addTime( int mmt )
             {
                      mm += mmt;
                      while( mm >= 60 )
                      {
                             mm -= 60;
                             hh += 1;
                      }
             }
             int getH() const
             {
                 return hh;
             }
             int getM() const
             {
                 return mm;
             }
             bool isBefore( const myTime & t ) const
             {
                  if( hh < t.getH() )
                      return true;
                  if( ( hh == t.getH() ) && ( mm <= t.getM() ) )
                      return true;
                      
                  return false;
             }
};

bool myless( myTime t1, myTime t2 )
{
     return t1.isBefore( t2 );
}


int main()
{
    ifstream in("B-small-attempt0.in");
    ofstream out("B-small.out");
    
    int N, T, NA, NB;
    in >> N;
    
    for( int i = 1; i <= N; i++ )
    {
         in >> T;
         in >> NA >> NB;
         
         vector< myTime > leaveA;
         vector< myTime > arrivedB;
         vector< myTime > leaveB;
         vector< myTime > arrivedA;
         
         for( int j = 0; j < NA; j++ )
         {
              string lastr, abstr;
              in >> lastr >> abstr;
              
              myTime latime( lastr.substr( 0, 2 ), lastr.substr( 3, 2 ) );
              leaveA.push_back( latime );
              sort( leaveA.begin(), leaveA.end(), myless );
              
              myTime abtime( abstr.substr( 0, 2 ), abstr.substr( 3, 2 ) );
              abtime.addTime( T );
              arrivedB.push_back( abtime );
              sort( arrivedB.begin(), arrivedB.end(), myless );
              
         }
         
         for( int j = 0; j < NB; j++ )
         {
              string lbstr, aastr;
              in >> lbstr >> aastr;
              
              myTime lbtime( lbstr.substr( 0, 2 ), lbstr.substr( 3, 2 ) );
              leaveB.push_back( lbtime );
              sort( leaveB.begin(), leaveB.end(), myless );
              
              myTime aatime( aastr.substr( 0, 2 ), aastr.substr( 3, 2 ) );
              aatime.addTime( T );
              arrivedA.push_back( aatime );
              sort( arrivedA.begin(), arrivedA.end(), myless );
              
         }
         
         int startA = 0;
         int startB = 0;
         
         for( int j = 0; j < NA; j++ )
         {
              bool flag = false;
              
              int size = arrivedA.size();
              for( int k = 0; k < size; k++ )
              {
                   if( arrivedA[k].isBefore( leaveA[j] ) )
                   {
                       flag = true;
                       arrivedA.erase( arrivedA.begin()+k );
                       break;
                   }
              }
                   
              if( !flag )
                  startA++;
         }
         
         for( int j = 0; j < NB; j++ )
         {
              bool flag = false;
              
              int size = arrivedB.size();
              for( int k = 0; k < size; k++ )
              {
                   if( arrivedB[k].isBefore( leaveB[j] ) )
                   {
                       flag = true;
                       arrivedB.erase( arrivedB.begin()+k );
                       break;
                   }
              }
                   
              if( !flag )
                  startB++;
         }
         
         out << "Case #" << i << ": " << startA << " " << startB << endl;
         
    }
    
    return 0;
}
              
                  
