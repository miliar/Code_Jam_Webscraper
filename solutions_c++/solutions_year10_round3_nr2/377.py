#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main () {

  ifstream myfile("B-large.in");

  
  if (myfile.is_open())
  {
    int T;
    myfile >> T;
    string w;
    
    for (int i=0; i<T; ++i)
    {
        long long a, b, c;
        myfile >> a;
        myfile >> b;
        myfile >> c;
        
        int howmany;
        
        for (howmany = -1; a < b; howmany++) {
            a *= c;
        }
        
        
        long long ketto=1;
        int mo;
        for (mo = 0; ketto <= howmany; mo++) {
            ketto *= 2;
            
        }

        cout << "Case #" << i+1 << ": " << mo; 
        cout << endl;
     }
    
    myfile.close();
  }
  else cout << "Unable to open file"; 
  return 0;
}


