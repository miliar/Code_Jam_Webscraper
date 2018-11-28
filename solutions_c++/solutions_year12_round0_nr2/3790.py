#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;
int main(){
  int m,n,s,p;
  cin >> m;
  for(int i=0; i<m; i++){
    int result;
    cin >> n;
    cin >> s;
    cin >> p;
    result = 0;
    vector<int> scs;
    
    for(int j=0; j<n; j++){
      int sc;
      cin >> sc;
      scs.push_back(sc);
    }
    sort( scs.begin(),scs.end(),greater<int>() ); 

    for(int j=0; j<n; j++){
      int maxs;
      int sc;
      sc = scs[j];

      if(sc %3 == 1){
        maxs = ( sc - (sc%3) ) / 3 + 1;
      }else if(sc %3 == 2){
        maxs = ( sc - (sc%3) ) / 3 + 1;
        if( s>0 && maxs+1 >= p && maxs < p){
          maxs++;
          s--;
        }
      }else if(sc == 0){
        maxs = 0;
      }else{
        maxs = sc / 3;
        if( s>0 && maxs+1 >= p && maxs < p){
          maxs++;
          s--;
        }
      }
      if( maxs >= p)
        result++ ;
    }

    cout << "Case #" << i+1 << ": " << result << endl;
  }
};
