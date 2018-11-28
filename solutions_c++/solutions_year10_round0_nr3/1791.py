/*
 * Google code jam 2010 / Qualification round 
 * Task C: Theme Park
 *
 * Created by Krisztian Balog on 5/8/10.
 */

#include <iostream>
#include <vector>
using namespace std;

int main(int argc, char* argv[]) {
  
  int T = 0;
  cin >> T;
  
  for (int i=0;i<T;i++) {
    
    // input    
    int R; // rounds
    int k; // roller coaster size
    int N; // number of groups
    
    cin >> R;
    cin >> k;
    cin >> N;
    
    vector< int > g; // group sizes
    for (int j=0;j<N;j++) {
      int tmp;
      cin >> tmp;
      g.push_back( tmp );
    }
         
    // some caching
    vector< long > gm; // how much money we can make if this group stands at the front of the queue
    vector< int > gn; // which is the next group
    
    for (int j=0;j<N;j++) {      
      long group_money = 0;      
      int group_next = j; // group pointer
      int g_n = 0; // this many groups included
      int g_k = 0; // #people in the roller coaster
      
      while (g_n+1 <= N && g_k+g[group_next] <= k) {
        g_n++;
        g_k += g[group_next];
        group_money += g[group_next];
        
        group_next++;
        if (group_next == N) group_next = 0;
      }
            
      gm.push_back( group_money );
      gn.push_back( group_next );
    }
    
    // simulation -- brute force
    long money = 0;
    int group_next = 0;
    
    for (int j=0;j<R;j++) {
      money += gm[group_next];
      group_next = gn[group_next];
    }    
    
    // output
    cout << "Case #" << (i+1) << ": " << money << endl;
  }
  
  return 0;
}
