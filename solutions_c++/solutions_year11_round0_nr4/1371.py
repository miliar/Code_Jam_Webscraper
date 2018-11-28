#include <iostream>
#include <string>
#include <fstream>
#include <cstdlib>
#include <math.h>
#include <gmp.h>
#include <vector>
#include <algorithm>
using namespace std;


  

int main(int argc, char *argv[]){
  ifstream ifs(argv[1]);
  string str;

  ifs >> str;
  int T = atoi(str.c_str());

  for(int i = 0; i < T; i++){
    printf("Case #%d: ", i+1);

    ifs >> str;
    int N = atoi(str.c_str());
    vector<int> arr(N);
    vector<int> srt(N);

    for(int j = 0; j < N; j++){
      ifs >> str;
      arr[j] = atoi(str.c_str());
      srt[j] = atoi(str.c_str());
    }
    
    sort(srt.begin(), srt.end());

    int ans = 0;
    for(int j = 0; j < N; j++){
      if(arr[j] != srt[j]){
	ans++;
      }
    }
    cout << ans << ".000000" << endl;
  } // T
 

  return 0;
}
