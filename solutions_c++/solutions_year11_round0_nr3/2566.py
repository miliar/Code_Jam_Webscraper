
#include <cstdlib>
#include <iostream>
#include <ctime>
#include <queue>
#include <cstdio>
#include <cstdarg>
#include <fstream>
#include <map>
#include <cstring>
#include <set>
#include <list>
#include <vector>
#include <algorithm>

using namespace std;

int main(int argc, char** argv){
  ifstream cin("in.txt");
  ofstream cout("out.txt");

  int nCase;

  cin >> nCase;
  for(int i = 0; i < nCase; i++){

    int n;
    cin >> n;
    vector<int> piece(n);
    for(int j = 0; j < n; j++) cin >> piece[j];

    int min, realSum = 0, unSum = 0;
    for(int j = 0; j < n; j++){
      realSum += piece[j];
      unSum ^= piece[j];
    }

    if(!unSum){
      min = *min_element(piece.begin(),piece.end());
    }

    cout << "Case #" << i+1 << ": ";

    if(unSum) cout << "NO";
    else cout << realSum - min;

    cout << "\n";
  }

  return 0;
}

