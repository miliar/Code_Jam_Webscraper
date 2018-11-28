#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <queue>
#include <map>
#include <sstream>
#include <algorithm>
#include <cmath>
#include <numeric>
using namespace std;
int F[50000000+1]; 
 void build_failure_function(string pattern)
  {
    int m = pattern.size();  
    F[0] = F[1] = 0;
    int i, j;
    for(i = 2; i <= m; i++) {
    j = F[i - 1];
    for( ; ; ) {
      if(pattern[j] == pattern[i - 1]) { 
      F[i] = j + 1; break; 
      }
      if(j == 0) { F[i] = 0; break; }
      
      j = F[j];
    }
    }   
  }
  int Knuth_Morris_Pratt(string text,string pattern)
  {
    int n = text.size();
    int m = pattern.size();
    int num = 0;
    build_failure_function(pattern); 
    int i, j;
    i = 0;
    j = 0;
    for( ; ; ) {
    if(j == n) break;
    if(text[j] == pattern[i]) {
      i++;
      j++;
      if(i == m) num++;
    }
    else if(i > 0) i = F[i];
    else j++;
    }
    return num;
  }

int main()
{
    string a(50000000,'a');
    string b=a;
   cout<< Knuth_Morris_Pratt(a,b)<<endl;
    
   system("pause");
   return 0;
}
