#include <iostream>
#include <map>
#include <set>
#include <string>
#include <utility>
#include <vector>

using namespace std;

int main(void) { 
   int CASES; cin >> CASES;
   for ( int tt=1; tt<=CASES; ++tt ) { // caret here
      int N, K; cin >> N >> K;
      int mask = (1<<N)-1;
      bool on = (K & mask) == mask;
      cout << "Case #" << tt << ": " << (on ? "ON" : "OFF") << "\n";
   }
   return 0;
} 
