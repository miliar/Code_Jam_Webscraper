#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int intersect(int left1, int right1, int left2, int right2)
{
     if ((left1 < left2 && right1 > right2) || (left1 > left2 && right1 < right2))
        return true;
     return false;
}

int main () {

  ifstream myfile("A-large.in");
  int left[1000];
  int right[1000];
  int size = 0;
  
  if (myfile.is_open())
  {
    int T, N;
    myfile >> T;
    string w;
    
    for (int i=0; i<T; ++i)
    {
        myfile >> N;
        int next;
        for (int j=0; j<N; ++j) {
           myfile >> next;
           left[j] = next;
           myfile >> next;
           right[j] = next;
           size++;
//           cout << left[j] << " " << right[j] << endl;
        }
        
        int mo = 0;
        for (int j=0; j<N; ++j) {
           for (int i=j+1; i<N; ++i) {
               if (intersect(left[j], right[j], left[i], right[i])) mo++;
           }
        }
        
        cout << "Case #" << i+1 << ": " << mo; 
        cout << endl;
     }
    
    myfile.close();
  }
  else cout << "Unable to open file"; 
  return 0;
}


