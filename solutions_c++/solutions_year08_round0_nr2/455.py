#include <iostream>
#include <cstdio>
#include <queue>
#include <iostream>

using namespace std ;

struct trajet
{
  int start ;
  int end ;
  bool gare ;
  
  const bool operator<( const trajet & tr ) const
  {
    return start < tr.start ;
  }

};

struct train
{
  int end ;
  bool gare ;
  
  const bool operator<( const train & t ) const
  {
    return end > t.end ;
  }

};

trajet trajets[1000] ;
priority_queue<train> trainToArrive ;

int main()
{
  int N = 0 ;

  scanf("%d",&N );

  for( int n = 0 ; n < N ; n ++ )
    {
      int T = 0 ;
      scanf("%d", &T );

      while( ! trainToArrive.empty() )
        trainToArrive.pop();
      
      int NA, NB ;
      scanf("%d%d",&NA,&NB );
      for( int tr = 0 ; tr < NA+NB; tr ++ )
        {
          int h1, m1, h2, m2 ;
          scanf("%d:%d %d:%d", &h1, &m1, &h2, &m2 );
          
          trajets[tr].start = h1*60+m1 ;
          trajets[tr].end = h2*60+m2 + T ;
          trajets[tr].gare = (tr >= NA) ;
        }
      sort( &trajets[0], &trajets[NA+NB] );

      /*
      for( int tr = 0 ; tr < NA + NB ; tr++ )
        {
          cout << trajets[tr].start << " " << trajets[tr].end << " " << trajets[tr].gare << endl ;
        }
      */

      int trainsNec[2] ;
      int trainsAvail[2] ;
      
      for( int gare = 0 ; gare < 2 ; gare ++ )
        {
          trainsNec[gare] = 0 ;
          trainsAvail[gare] = 0 ;
        }

      for( int tr = 0 ; tr < NA+NB; tr ++ )
        {
          trajet & curTrajet = trajets[tr] ;
          while( ! trainToArrive.empty() )
            {
              const train & lastTrain = trainToArrive.top();
              if( lastTrain.end > curTrajet.start ) 
                break ;
              else
                {
                  trainsAvail[ lastTrain.gare ] ++ ;
                  trainToArrive.pop();
                }
            }
          
          bool nowGare = curTrajet.gare ;
          if( trainsAvail[ nowGare ] == 0 )
            trainsNec[ nowGare ] ++ ;
          else
            trainsAvail[nowGare] -- ;

          train newTrain ;
          newTrain.end = curTrajet.end ;
          newTrain.gare = ! curTrajet.gare ;
          trainToArrive.push( newTrain );
          
        }
        
      cout << "Case #" << (n+1) << ": "<< trainsNec[0]  << " " << trainsNec[1]  << endl ;
    }

}
