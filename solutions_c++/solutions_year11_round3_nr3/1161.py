#include <algorithm>
#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <string>
#include <cstdlib>
#include <cmath>
#include <sstream>
#include <cctype>

using namespace std;

int main(){

  freopen("C-small-attempt0.in","r",stdin);
  //freopen("B-large.in","r",stdin);
  freopen("outC.txt","w",stdout);
	
  int cases;
  cin >> cases;

  for(int i=1;i<=cases;i++){
    cout << "Case #"<<i<<": ";
    
    int players,lower,greatest;
    cin >> players >> lower >> greatest;
    
    vector<int> player;
    player.resize(players);
    for(int i=0;i<players;i++)
      cin >> player[i];
    
    stable_sort(player.begin(),player.end());

    bool status=true;
    
    vector<int> divisors;
    for(;lower<=greatest;lower++){
      status=true;
      for(int i=0;i<players;i++){
	if( player[i] % lower != 0 && lower%player[i]!=0 ){
	  status=false;
	  break;
	}
      }
      if(status)
	break;
    }
    
    if(status){
      cout << lower << endl;
    }else{
      cout << "NO" << endl;
    }
    
  }


  return 0;
}
