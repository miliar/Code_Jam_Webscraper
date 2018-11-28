#include <map>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
int tab [ 1024][1024];

int main(int argc, char *argv[])
{

    
    int testCases;
    cin >> testCases;

    for ( int testCase = 1; testCase <= testCases; testCase ++ ) {
        int engines;
        
        cin >> engines;
        
        char buf [ 1024]; 
        vector < string > engs;
        cin.getline ( buf, 1023);
        
        for ( int engine = 0; engine < engines; engine ++) {
            
            cin.getline(buf, 1023);
            string eng ( buf);
            engs.push_back( eng );
            
        } 
        sort ( engs.begin(), engs.end() );
        map < string , int > mapa;
        for ( int i = 0; i < engs.size(); i++)
            mapa[engs[i] ] = i;
            
        
        
        int counter = 0;    
        int queries;
        cin >> queries;
      // cout << queries << endl; 
        
        cin.getline ( buf, 1023);
        vector <string> qv;
        int count = 0;
        int query = 0;
        if ( queries == 0) {
           cout << "Case #" << testCase << ": 0" << endl;
           continue;
        }
        for (  query = 0; query < queries; query ++ ) {
            
            cin.getline ( buf, 1023 );
            string temp1 ( buf);
            int qno = mapa [ temp1];
            qv.push_back ( string (buf));
      //      cout << "query" << endl;    
        }
      //  cout << "case" << endl;
       
        for ( int eno = 0; eno < (int)engs.size(); eno++)
            if ( qv[0] == engs[eno] )
               tab[0][eno] = 999999;
            else
               tab[0][eno] = 0;
               
        int lastSmallest = 0;       
        int currentSmallest = 0;
        for ( int qno = 1; qno < queries; qno++) {
            currentSmallest = 999999;
            for ( int eno = 0; eno < (int)engs.size(); eno ++) {
                if ( engs[eno] == qv[qno] )
                   tab[qno][eno] = 999999;
                else if (lastSmallest + 1 < tab[qno-1][eno] ) {
                     tab[qno][eno] = lastSmallest + 1;
                     currentSmallest = ( tab[qno][eno] < currentSmallest)?tab[qno][eno]:currentSmallest;
                }
                else {
                     tab[qno][eno] = tab[qno-1][eno];
                     currentSmallest = ( tab[qno][eno] < currentSmallest)?tab[qno][eno]:currentSmallest;
                }    
            }
            lastSmallest = currentSmallest;    
        }
        cout << "Case #" << testCase << ": "<< lastSmallest << endl;
    }
    //cout << "done";

    
    
    return 0;
}
