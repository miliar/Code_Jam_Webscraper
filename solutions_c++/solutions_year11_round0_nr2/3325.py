#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <ostream>
#include <vector>

using namespace std;

char NONE = '-';

char getTableMatch(char c, char d, vector<string> &tb) {
  
  for(int i = 0; i < tb.size(); i++) {
    string s = tb[i];
    if(s[0] == c && s[1] == d)
      return s[2];
  }
  return NONE;
}
bool isOpp(char c, char d, vector<string> &opp) {
  
  for(int i = 0; i < opp.size(); i++) {
    string s = opp[i];
    if(s[0] == c && s[1] == d)
      return true;
  }
  return false;
}

bool checkOpp(vector<char> &el, int i, vector<string> &opp) {
  for(int j = 0; j < i; j++) {
      if(isOpp(el[j],el[i],opp))
      return true;
  }
  return false;
}


int main() {
  int T;
  cin >> T;
  
  for(int k = 1; k <= T; k++) {
    vector<string> table;
    int C;
    cin >> C;
    for(int i = 0; i < C; i++) {
      char a,b,c;
      cin >> a;
      cin >> b;
      cin >> c;
      
      string s1 = "";
      s1.append(1,a);
      s1.append(1,b);
      s1.append(1,c);
      
      table.push_back(s1);
      
      string s2 = "";
      s2.append(1,b);
      s2.append(1,a);
      s2.append(1,c);
      
      table.push_back(s2);
      
    }
    
    vector<string> opp;
    
    int D;
    cin >> D;
    for(int i = 0; i < D; i++) {
      char a, b;
      cin >> a;
      cin >> b;     
      
      string s1 = "";
      s1.append(1,a);
      s1.append(1,b);
      
      opp.push_back(s1);
      
      string s2 = "";
      s2.append(1,b);
      s2.append(1,a);
      
      opp.push_back(s2);
      
      

    }  
    
    int N;
    cin >> N;
    
    vector<char> eList;
    
    for(int i = 0; i < N; i++) {
      char c;
      cin >> c;
      
      eList.push_back(c);
    }
  
  
    vector<char> output;
    
    for(int i = 0; i < eList.size(); i++) {
      char a = eList[i-1];
      if(i > 0) {
        char c = eList[i];
        char m = getTableMatch(a,c,table);
        if(m != NONE) {
          eList.erase(eList.begin()+i-1);
          eList[i-1] = m;
          i--;
          continue;
        }
      }
      if(checkOpp(eList, i, opp)) {
      for(int j = 0; j<=i; j++)
       eList.erase(eList.begin());    
          i=-1;
       continue;
      }

     }
    output = eList;
  // 
//     vector<char> output;
//     for(int i = 0; i < N; i++) {
//       char a = eList[i];
//       
//       if(i < N-1) {
//         char c = eList[i+1];
//         
//         char m = getTableMatch(a,c,table);
//         if(m != NONE) {
//           output.push_back(m);
//           i++;
//           continue;
//         }
//         
//         if(isOpp(a, c, opp)) {
//           i++;
//           continue;
//         }
//         
//         output.push_back(a);
//         
//         
//       } else {
//         output.push_back(a);
//       }
//     }
    
    cout << "Case #" << k << ": ";
    cout << '[';
    if(output.size() > 0)
      cout << output[0];
    for(int i = 1; i < output.size();i++) {
      cout << ", " << output[i];
    }
    cout << ']' << endl;
  
  }
  
  return 0;
}