#include <iostream>
#include <string>
#include <map>
#include <vector>
using namespace std;

int main (void) {
   int result, n, a, b, current, previous;
   string input;   
   bool taken[100];
   int _taken;

   cin >> n;

   for (int k = 0; k < n; k++) {
      map<string,int> engines;
      memset(taken, false, sizeof(bool)*100);
      previous = -1;
      result = 0;
      _taken = 0;

      cin >> a;
      getline(cin,input); // getting /n
      for (int i = 0; i < a; i++) {
	 getline(cin,input);
	 engines[input] = i;
      }

      cin >> b;
      getline(cin,input); // getting /n
      for (int i = 0; i < b; i++) {
	 getline(cin,input);
	 current = engines[input];

	 if (previous != current) {
	    if (taken[current] == false) {
	       if (_taken == a-1) {
		  result++;
		  memset(taken, false, sizeof(bool)*100);
		  _taken = 0;
	       }
	       taken[current] = true;
	       _taken++;
	    }
	 }

	 previous = current;
      }

      cout << "Case #" << k+1 << ": " << result << endl;
   }


   return 0;
}
