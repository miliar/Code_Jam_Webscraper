#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main () {

  ifstream myfile("C-small-attempt0.in");
  
  if (myfile.is_open())
  {
    int C, R;
    myfile >> C;
    
    for (int c=0; c<C; ++c)
    {
        myfile >> R;
        int a[R][4];
        
        for (int j=0; j<R; ++j) {
            for (int k=0; k<4; ++k) {
                myfile >> a[j][k];
            }            
        }
        
 //        for (int j=0; j<R; ++j) {
//            for (int k=0; k<4; ++k) {
//                cout << a[j][k];
//             }
//             cout << endl;
//        }

       const int p = 100;
       int b[p][p];
    
       for (int j=0; j<p; ++j) {
            for (int k=0; k<p; ++k) {
                b[j][k] = 0;
             }
        }
        
        for (int j=0; j<R; ++j) {
            for (int k=a[j][0]-1; k<a[j][2]; ++k) {
                 for (int l=a[j][1]-1; l<a[j][3]; ++l) {
                     b[k][l] = 1;
                 }
             }
        }

//         for (int j=0; j<p; ++j) {
//            for (int k=0; k<p; ++k) {
//                cout << b[k][j];
//             }
//             cout << endl;
//        }

       int mo = 0;
       int mom[p][p];
       bool finished = false;
       
       while (!finished) {
           finished = true;
           for (int j=0; j<p; ++j) {
                for (int k=0; k<p; ++k) {
                    if (b[j][k] == 1) {
                           finished = false;
                           break;
                    }
                }
           }
          if (finished) break;
          else {
               mo++;
               }          
       
          for (int j=0; j<p; ++j) {
            for (int k=0; k<p; ++k) {
                if ((b[j][k] == 1) && ((j?b[j-1][k]:0) == 0) && ((k?b[j][k-1]:0) == 0)) mom[j][k] = 0; else
                   if ((b[j][k] == 0) && ((j?b[j-1][k]:0) == 1) && ((k?b[j][k-1]:0) == 1)) mom[j][k] = 1; else
                      mom[j][k] = b[j][k];
             }
          }
          
          
        for (int j=0; j<p; ++j) {
            for (int k=0; k<p; ++k) {
                b[j][k] = mom[j][k];
             }
        }         


//        for (int j=0; j<p; ++j) {
//            for (int k=0; k<p; ++k) {
//                cout << b[k][j];
//             }
//             cout << endl;
//        }     
       }


       
        cout << "Case #" << c+1 << ": " << mo;
        cout << endl;
     }
    
    myfile.close();
  }
  else cout << "Unable to open file"; 
  return 0;
}


