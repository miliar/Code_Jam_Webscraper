/*
   Rafael Schimassek
*/

#define JAMLEN 19
#define LINELEN 600;

#include <iostream>
#include <string>

using namespace std;

char keyword[] = "welcome to code jam"; //'m' is index 18
int combo[JAMLEN];
char current;
string line;


int main () {

  int num_cases, cc, a, b, linesize;
  long long total;
  cin >> num_cases;
  cin.ignore();
  for (cc = 0; cc < num_cases; ++cc) {
    total = 0;
    getline(cin, line);
    linesize = line.length();
    
    //clear the combo array
    for (a = 0; a < JAMLEN; ++a)
      combo[a] = 0;
      
    //go through the whole string
    for (a = 0; a < linesize; ++a) {
      current = line[a];
      
      for (b = 0; b < JAMLEN; ++b) {
        if (current == keyword[b]) {
          if (b == 0)
            ++combo[0];
          else
            combo[b] += combo[b-1];
          
          //try to sum to total
          if (b == 18)
            total = (long long) total + combo[b-1];
        }
      }
    }
    
    printf("Case #%d: %04lld\n", (cc + 1), total );
    //cout << "Case #" << (cc+1) << ": " << total << '\n';
    
  }
  
  
  
  return 0;
  
}
