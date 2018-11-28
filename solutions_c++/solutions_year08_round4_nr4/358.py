#include <map>
#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>


using namespace std;
int taken [ 10];
string str;
  int k;
int perm [ 10];
int minim = 99999;
string str2;

void dfs ( int post ) {
     if ( post == k ) {
               str2 = str;
               
               for ( int i = 0; i < str2.size(); i++) {
                   str2 [ i ] = str [ i - (i % k) +perm[i%k] ];    
               }
              
               int count = 1;
               int last = str2[0];
               for ( int i = 0 ; i < str2.size(); i ++) {
                     if ( str2[i] != last)
                        count ++;
                     last = str2[i];
                   }
               if ( count < minim )
                  minim = count;
               // cout << str2 << " = " << count << endl;
            // loblicz to!
               return;
            }
     for ( int i = 0; i < k ; i++) {
         if ( ! taken[i] ) {
              
            taken [i] = 1;
            perm [ post] = i;
            dfs ( post +1);
            
            taken [i] = 0;
                
         }
     }
}
int main(int argc, char *argv[])
{

    
    int testCases;
    cin >> testCases;

    for ( int testCase = 1; testCase <= testCases; testCase ++ ) {
       
         minim = 99999;
         cin >> k;
         cin >> str;
         
         // permutations
         memset ( taken, 0 , sizeof ( taken ));
         dfs ( 0 );
                  
         cout << "Case #" << testCase << ": " << minim << endl;
       
    }
    //cout << "done";

    
    
    return 0;
}
