#include <iostream>
#include <map>
#include <string>
using namespace std;

int main() {
  int testCases, currCase = 1;
  cin >> testCases;
  while (currCase <= testCases){
    char side = 'L';
    map<string,char> strMap;
    map<string,char>::iterator mi;
    string input;
    int n, switches=0;
    cin >> n; 
    cin.get();
    for (int i = 0; i < n; i++ ){
      getline(cin, input);
      strMap[input] = 'L';
    }
    int n2;
    cin >> n2;
    cin.get();
    for (int i = 0; i < n2; i++){
      getline(cin,input); 
      if (strMap[input] == side){
        if (side == 'L') strMap[input] = 'R';
        else strMap[input] = 'L';
      }
      int countSide = 0;
      for(mi = strMap.begin(); mi != strMap.end(); mi++)
        if (mi->second == side) countSide++;
      if (countSide == 0){
        strMap[input] = side;
        if (side == 'L') side = 'R';
        else side = 'L';
        switches ++;  
      }
    }
    cout << "Case #" << currCase << ": " << switches << endl;
    currCase ++;
  }
  return 0;
}
