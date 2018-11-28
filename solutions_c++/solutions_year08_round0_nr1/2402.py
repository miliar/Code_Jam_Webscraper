#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main()
{
    int n, s, q;
    vector <string> traz, upiti;
    vector <int> rj;
    
    scanf ( "%d\n", &n );
    
    for ( int k = 0; k < n; k++ )
    {
        traz.clear();
        upiti.clear();
        
        scanf ( "%d\n", &s );
        for ( int i = 0; i < s; i++ )
        {
            string tmp;
            getline ( cin, tmp );
            
            traz.push_back ( tmp );
        }
        
        scanf ( "%d\n", &q );
        for ( int i = 0; i < q; i++ )
        {
            string tmp;
            getline ( cin, tmp );
            
            upiti.push_back ( tmp );
        }
        
        int rez = -1, poz = 0;
        int next = 0;
        
        if ( q == 0 ) rez = 0;
              
        while ( poz < q )
        {
              rez ++;
              
              for ( int i = 0; i < s; i++ )
              {
                  int j;
                  
                  for ( j = poz; ( j < q ) && ( upiti[j] != traz[i] ); j++ );
                 
                  if ( j > next ) next = j;
              }
              poz = next;
        }
        
        rj.push_back ( rez );
    }
    
    for ( int i = 0; i < rj.size(); i++ )
        printf ( "Case #%d: %d\n", i+1, rj[i] );
    
    
    return 0;
}                 
        
        
        
        
           
            
    
