#include <cstdlib>
#include <iostream>
#include <vector>
#include <string>

using namespace std;


class travel {
 public:
       int start;
       int end;
   
   travel ( string s, string e ) {
          start = 0;
          start += (s[0]-'0' ) * 600;              
          start += (s[1]-'0' ) * 60;
          start += (s[3]-'0' ) * 10;
          start += (s[4]-'0');
          end = 0;
          end += (e[0]-'0' ) * 600;              
          end += (e[1]-'0' ) * 60;
          end += (e[3]-'0' ) * 10;
          end += (e[4]-'0');
   }    
   bool operator< ( const travel & sec ) const {
        return start < sec.start;
   }     
      
};



int main(int argc, char *argv[])
{
    int cases;
    cin >> cases;
    for ( int caseNo = 1; caseNo <= (int) cases; caseNo ++) {
        
        int turn;
        cin >> turn;

        int atra, btra;
        cin >> atra >> btra;
        vector < travel > atrav, btrav;
        
        // wczytujemy 
        for ( int i = 0; i < atra; i++) {
            string temp1, temp2;
            cin >> temp1 >> temp2;
            atrav.push_back ( travel ( temp1, temp2) );
        }
        for ( int i = 0; i < btra; i++) {
            string temp1, temp2;
            cin >> temp1 >> temp2;
            btrav.push_back ( travel ( temp1, temp2) );
        }
        sort ( atrav.begin(), atrav.end());
        sort ( btrav.begin(), btrav.end());
        
        
        int countera = 0;
        int counterb = 0;
        vector < int > arra ( 24*60+ 1000, 0);
        vector < int > arrb ( 24*60+ 1000, 0);
        int cura =0;
        int curb =0;
        int inda = 0;
        int indb = 0;
        for ( int time = 0; time < 24*60; time ++ ) {
          cura += arra [time];
          curb += arrb [time];  
          // wysylamy
          while ( inda < (int) atrav.size() && atrav[inda].start == time ) {
                if ( cura == 0)
                   countera ++;
                else 
                     cura --;
                arrb [ atrav[inda].end + turn ] += 1 ;
                //cout << " adding to " << atrav[inda].end + turn << endl;
                inda ++;
          }
          while ( indb < (int) btrav.size() && btrav[indb].start == time ) {
                if ( curb == 0)
                   counterb ++;
                else 
                     curb --;
                arra [ btrav[indb].end + turn ] += 1;
                indb ++;
          }  
        }
        
        
        cout << "Case #" << caseNo << ": " <<countera << " " << counterb << endl;    
    }
    //system("PAUSE");
    return EXIT_SUCCESS;
}
