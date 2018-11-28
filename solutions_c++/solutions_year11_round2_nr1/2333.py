#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>
#include <cstring>


using namespace std;

int main(){
   int n_case;
   cin >> n_case;
   for( int i = 0 ; i < n_case ; i++ ){
      int n_team;
      cin >> n_team;
      long double table[n_team][n_team];
      long double n_wins[n_team];
      long double n_oponents[n_team];
      vector<string> data;
      memset( table, 0 , sizeof(table) );
      memset( n_wins, 0, sizeof(n_wins) );
      memset( n_oponents, 0 , sizeof(n_oponents) );
      for( int j = 0 ; j < n_team ; j++ ){
         int n_battle = 0;
         int n_win=0;
         string line;
         cin >> line;
         for( int k = 0 ; k < n_team ; k++ ){
            if( line[k] != '.' ){
               if( line[k] == '1' ){
                  n_win++;
               }
               n_battle++;
            }
         }
         n_oponents[j] = (long double)n_battle;
         n_wins[j] = (long double)n_win;
         for( int k = 0 ; k < n_team ; k++ ){
            if( line[k] == '1' )
               table[j][k] = (long double) (n_win-1);
            if( line[k] == '0' )
               table[j][k] = (long double) n_win;
         }
         data.push_back(line);
      }
      /*
      for( int j = 0 ; j < n_team ; j++ ){
         for( int k = 0 ; k < n_team ; k++ ){
            cout << table[j][k] << " ";
         }
         cout << endl;
      }
      */
      long double owps[n_team];
      memset( owps , 0 , sizeof(owps) );
      for( int j = 0 ; j < n_team ;j++ ){
         long double owp = 0.0;
         for( int k = 0 ; k < n_team; k++ ){
            if(data[j][k] != '.' ){
               owp += table[k][j]/(n_oponents[k]-1);
            }
         }
         owps[j] = owp;
      }
      cout << "Case #" << i+1 << ": " << endl;
         cout.setf(ios::fixed, ios::floatfield);
         cout.precision(12);

      for( int j = 0 ; j < n_team; j++ ){
         long double WP = n_wins[j];
         long double OWP = owps[j];
         long double OOWP = 0.0;
         for( int k = 0 ; k < n_team; k++ ){
            if( data[j][k] != '.' ) {
               OOWP += owps[k]/(n_oponents[k]);
            }
         }
         //cout << WP <<" "<< OWP<< " " << OOWP << endl;
         cout << (WP+2*OWP+OOWP)/(4*n_oponents[j]) << endl;
      }
   }
   return 0;
}
