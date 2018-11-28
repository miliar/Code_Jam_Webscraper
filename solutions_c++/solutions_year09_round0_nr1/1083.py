#include <cstdlib>
#include <iostream>
#include <deque>
#include <queue>
#include <algorithm>
#include <vector>
#include <string>



using namespace std;

int main(int argc, char *argv[])
{
    int L, D, N;
    cin >> L >> D >> N;
    vector < string > slowa;
    
    for ( int slowo = 0; slowo < D; slowo ++) {
        string temp;
        cin >> temp;
        slowa.push_back ( temp );
        
    }
    for ( int caseno = 1 ; caseno <= N; caseno ++) {
        
        vector < int > flag ( slowa.size(), 1);
        
        string temp;
        cin >> temp;
        // load into a vector <string>
        vector < string > v (L, "");
        int cur = 0;
        int curletter = 0;
        int inside = 0;
        while ( cur < temp.size()) {
            if ( temp [cur] == '(')
                inside = 1;
            if ( temp [ cur] == ')')
                inside = 0;
                
            if ( temp [cur] >= 'a' && temp[cur] <= 'z')
                v[curletter] += temp[cur];
            
            if ( ! inside)
                curletter ++;
            cur ++;    
        }
        
       /* for ( int letter = 0; letter < L; letter++)
            cerr << ": " << v[letter] << endl;
         */   
        for ( int letter = 0; letter < L; letter ++ ) {
            
            vector < int > flag1 ( D, 0);
            //
            for ( int possib = 0; possib < v[letter].size(); possib ++) {
                
                for ( int slowo = 0; slowo < slowa.size(); slowo++) {
                    if ( slowa[slowo][letter] == v[letter][possib] )
                        flag1 [slowo] = 1;    
                }
                            
            }
            
            for ( int i = 0; i < flag1.size(); i++)
                if ( flag1[i] == 0)
                    flag[i] = 0;
            
        }    
        int count = 0;
            for ( int slowo = 0; slowo < flag.size(); slowo ++)
                if ( flag[slowo] == 1)
                    count ++;
            
            cout << "Case #" << caseno << ": " << count << endl;       
        
    }
    

    return EXIT_SUCCESS;
}
