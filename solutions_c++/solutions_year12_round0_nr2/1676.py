#include <iostream>

using namespace std;

// dancers.cpp : Defines the entry point for the console application.
//

int main(int argc, char* argv[])
{
  int ntest;
  cin >> ntest;

  for(int itest = 0; itest < ntest; ++itest){

    int ndancer;
    cin >> ndancer;

    int nsurprise;
    cin >> nsurprise;

    int p;
    cin >> p;

    int npass = ndancer;
    for(int idancer = 0; idancer < ndancer; ++idancer){
      int tscore;
      cin >> tscore;

      int min_result = p - 1;
      if(min_result < 0)
        min_result = 0;
      if(tscore >= p + min_result + min_result)
        continue;

      if(nsurprise > 0){
        int min_result2 = p - 2;
        if(min_result2 < 0)
          min_result2 = 0;
        if(tscore >= p + min_result2 + min_result2){
          nsurprise--;
          continue;
        }
      }

      npass--;
    }

    cout << "Case #" << itest + 1 << ": " << npass << endl;
  }

	return 0;
}

