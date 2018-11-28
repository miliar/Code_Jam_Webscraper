#include <iostream>
#include <string>
#include <sstream>
#include <math.h>
#include <vector>

using namespace std;

int main(int argc, char **argv) {
  
    int nbtests;
    cin >> nbtests;

    int n;
    for (int test = 0; test<nbtests; test++)
    {
      cin >> n;

      vector<int> A;
      vector<int> B;
      int a; int b;
      for (int i = 0 ; i < n; ++i) {
	cin >> a;
	A.push_back(a);
	cin >> b;
	B.push_back(b);
      }
      
      int inter = 0;
      
      for (int i = 0 ; i < n; ++i) {
	for (int j = 0 ; j < i; ++j) {
	  int da = A[i] - A[j];
	  int db = B[i] - B[j];
	  if( (da > 0 && db < 0) || (da < 0 && db > 0))
	    inter++;
	}
      }
      
      cout << "Case #" << test+1 <<": " << inter << endl;
      //cerr << test+1 << "/" << nbtests << endl;
    }

}
